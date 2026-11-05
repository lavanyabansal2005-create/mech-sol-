"""Put pandoc's docx XML into OOXML schema order (run inside the unzipped docx folder)."""
import lxml.etree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
ORDER = {
    (W, "pPr"): "pStyle keepNext keepLines pageBreakBefore framePr widowControl numPr suppressLineNumbers pBdr shd tabs "
                "suppressAutoHyphens kinsoku wordWrap overflowPunct topLinePunct autoSpaceDE autoSpaceDN bidi adjustRightInd "
                "snapToGrid spacing ind contextualSpacing mirrorIndents suppressOverlap jc textDirection textAlignment "
                "textboxTightWrap outlineLvl divId cnfStyle rPr sectPr pPrChange",
    (W, "tblPr"): "tblStyle tblpPr tblOverlap bidiVisual tblStyleRowBandSize tblStyleColBandSize tblW jc tblCellSpacing "
                  "tblInd tblBorders shd tblLayout tblCellMar tblLook tblCaption tblDescription tblPrChange",
    (W, "tcPr"): "cnfStyle tcW gridSpan hMerge vMerge tcBorders shd noWrap tcMar textDirection tcFitText vAlign hideMark "
                 "headers cellIns cellDel cellMerge tcPrChange",
    (W, "style"): "name aliases basedOn next link autoRedefine hidden uiPriority semiHidden unhideWhenUsed qFormat locked "
                  "personal personalCompose personalReply rsid pPr rPr tblPr trPr tcPr tblStylePr",
    (M, "dPr"): "begChr sepChr endChr grow shp ctrlPr",
    (M, "mcPr"): "count mcJc",
}
ORDER = {k: {t: i for i, t in enumerate(v.split())} for k, v in ORDER.items()}


def fix(path):
    tree = ET.parse(path)
    n = 0
    for el in tree.iter():
        if not isinstance(el.tag, str):
            continue
        q = ET.QName(el)
        key = (q.namespace, q.localname)
        if key in ORDER:
            rank = ORDER[key]
            kids = list(el)
            new = sorted(kids, key=lambda c: rank.get(ET.QName(c).localname, 999) if isinstance(c.tag, str) else 999)
            if new != kids:
                for c in kids:
                    el.remove(c)
                el.extend(new)
                n += 1
        # math run: <m:nor/> and <m:sty/> may not both appear; with nor the text is already upright
        if key == (M, "rPr"):
            nor = el.find(f"{{{M}}}nor")
            sty = el.find(f"{{{M}}}sty")
            if nor is not None and sty is not None and sty.get(f"{{{M}}}val") == "p":
                el.remove(sty)
                n += 1
        # numbering ids must be 8 hex digits
        if key == (W, "nsid"):
            v = el.get(f"{{{W}}}val")
            if v and len(v) < 8:
                el.set(f"{{{W}}}val", v.zfill(8))
                n += 1
    tree.write(path, xml_declaration=True, encoding="UTF-8", standalone=True)
    return n


for p in ["word/document.xml", "word/styles.xml", "word/numbering.xml"]:
    print(p, fix(p), "fixes")
