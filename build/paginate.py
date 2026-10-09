#!/usr/bin/env python3
"""Estimates the rendered page on which each chapter begins.

No LibreOffice/Word renderer is available in this environment, so page numbers
for the Contents are derived from a layout model that walks the document body
in order and accumulates height in points.
"""
import math, os
from docx import Document
from docx.oxml.ns import qn
from PIL import Image

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# A4 11906x16838 twips, margins 1300 top / 1300 bottom / 1440 each side
TEXT_H_PT = (16838 - 1300 - 1300) / 20.0          # 711.9 pt
TEXT_W_TW = 11906 - 1440 - 1440                   # 9026 twips
TEXT_W_IN = TEXT_W_TW / 1440.0                    # 6.268 in

# average glyph advance for Times New Roman, as a fraction of point size
GLYPH = 0.415   # Times New Roman average advance (~96 chars on a 6.5in line)


def chars_per_line(width_tw, size_pt):
    width_pt = width_tw / 20.0
    return max(8, int(width_pt / (size_pt * GLYPH)))


def para_height(p):
    """Height in points of a w:p element."""
    pPr = p.find(qn("w:pPr"))
    size = 12.0
    line_tw = 240.0
    after_tw = 0.0
    before_tw = 0.0
    ind_left = 0
    if pPr is not None:
        sp = pPr.find(qn("w:spacing"))
        if sp is not None:
            if sp.get(qn("w:line")):
                line_tw = float(sp.get(qn("w:line")))
            if sp.get(qn("w:after")):
                after_tw = float(sp.get(qn("w:after")))
            if sp.get(qn("w:before")):
                before_tw = float(sp.get(qn("w:before")))
        ind = pPr.find(qn("w:ind"))
        if ind is not None and ind.get(qn("w:left")):
            ind_left = int(ind.get(qn("w:left")))
    text = ""
    has_img = False
    for r in p.findall(qn("w:r")):
        for t in r.findall(qn("w:t")):
            text += t.text or ""
        szs = r.findall(qn("w:rPr") + "/" + qn("w:sz"))
        if szs:
            size = float(szs[0].get(qn("w:val"))) / 2.0
        if r.findall(".//" + qn("w:drawing")):
            has_img = True
    h = before_tw / 20.0 + after_tw / 20.0
    if has_img:
        return h + IMG_H.get(len(IMG_H), 0) or h
    cpl = chars_per_line(TEXT_W_TW - ind_left, size)
    lines = max(1, math.ceil(len(text) / cpl)) if text else 1
    # line_tw is "auto" multiple-of-240 spacing
    line_pt = (line_tw / 240.0) * size * 1.15
    return h + lines * line_pt


IMG_H = {}


def para_height2(p, img_iter):
    pPr = p.find(qn("w:pPr"))
    size = 12.0
    line_tw = 240.0
    after_tw = before_tw = 0.0
    ind_left = 0
    if pPr is not None:
        sp = pPr.find(qn("w:spacing"))
        if sp is not None:
            if sp.get(qn("w:line")):
                line_tw = float(sp.get(qn("w:line")))
            if sp.get(qn("w:after")):
                after_tw = float(sp.get(qn("w:after")))
            if sp.get(qn("w:before")):
                before_tw = float(sp.get(qn("w:before")))
        ind = pPr.find(qn("w:ind"))
        if ind is not None and ind.get(qn("w:left")):
            ind_left = int(ind.get(qn("w:left")))
    text = ""
    imgs = []
    for r in p.findall(qn("w:r")):
        for t in r.findall(qn("w:t")):
            text += t.text or ""
        szel = r.find(qn("w:rPr") + "/" + qn("w:sz"))
        if szel is not None:
            size = float(szel.get(qn("w:val"))) / 2.0
        for ext in r.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent"):
            imgs.append(ext)
    h = (before_tw + after_tw) / 20.0
    if imgs:
        for ext in imgs:
            h += int(ext.get("cy")) / 12700.0   # EMU -> pt
        return h
    cpl = chars_per_line(TEXT_W_TW - ind_left, size)
    lines = max(1, math.ceil(len(text) / cpl)) if text else 1
    line_pt = (line_tw / 240.0) * size * 1.15
    return h + lines * line_pt


def table_height(tbl):
    grid = [int(g.get(qn("w:w"))) for g in
            tbl.findall(qn("w:tblGrid") + "/" + qn("w:gridCol"))]
    h = 0.0
    for tr in tbl.findall(qn("w:tr")):
        rowmax = 0.0
        for i, tc in enumerate(tr.findall(qn("w:tc"))):
            w_tw = grid[i] if i < len(grid) else 1500
            cellh = 0.0
            for p in tc.findall(qn("w:p")):
                size = 10.5
                txt = ""
                for r in p.findall(qn("w:r")):
                    for t in r.findall(qn("w:t")):
                        txt += t.text or ""
                    szel = r.find(qn("w:rPr") + "/" + qn("w:sz"))
                    if szel is not None:
                        size = float(szel.get(qn("w:val"))) / 2.0
                txt = txt.replace("\n", " " * 40)
                cpl = chars_per_line(w_tw - 160, size)
                lines = max(1, math.ceil(len(txt) / cpl)) if txt else 1
                cellh += lines * size * 1.22
            rowmax = max(rowmax, cellh)
        h += rowmax + 4.0   # cell margins top+bottom 40tw each = 4pt
    return h


def paginate(path):
    doc = Document(path)
    body = doc.element.body
    page = 1
    used = 0.0
    marks = []          # (page, text) for chapter/front-matter headings
    for child in body.iterchildren():
        tag = child.tag
        if tag == W + "p":
            pPr = child.find(qn("w:pPr"))
            brk = pPr is not None and pPr.find(qn("w:pageBreakBefore")) is not None
            txt = "".join(t.text or "" for t in child.findall(".//" + qn("w:t")))
            if brk:
                page += 1
                used = 0.0
            h = para_height2(child, None)
            if used + h > TEXT_H_PT:
                page += 1
                used = 0.0
            if txt.strip():
                marks.append((page, txt.strip()))
            used += h
        elif tag == W + "tbl":
            h = table_height(child)
            if h > TEXT_H_PT:
                # table spans pages
                full = int(h // TEXT_H_PT)
                if used + (h - full * TEXT_H_PT) > TEXT_H_PT:
                    page += 1
                    used = 0
                page += full
                used = h - full * TEXT_H_PT
            else:
                if used + h > TEXT_H_PT:
                    page += 1
                    used = 0.0
                used += h
        elif tag == W + "sectPr":
            pass
    return page, marks


if __name__ == "__main__":
    import sys, re
    total, marks = paginate("/home/user/SIP/Rosy_Blue_Securities_Black_Book.docx")
    print("estimated total pages:", total)
    want = ["CERTIFICATE", "EXPERIENCE CERTIFICATE", "DECLARATION", "ACKNOWLEDGEMENT",
            "EXECUTIVE SUMMARY", "CONTENTS", "CHAPTER 1", "CHAPTER 2", "CHAPTER 3",
            "CHAPTER 4", "CHAPTER 5", "CHAPTER 6", "CHAPTER 7", "CHAPTER 8",
            "ANNEXURE A", "ANNEXURE B", "ANNEXURE C"]
    seen = set()
    for pg, t in marks:
        if t in want and t not in seen:
            seen.add(t)
            print(f"  {t:24s} page {pg}")
    # section-level starts inside chapters
    print("\nsection starts:")
    for pg, t in marks:
        if re.match(r"^\d+\.\d+ [A-Z]", t):
            print(f"  p{pg:3d}  {t[:70]}")
