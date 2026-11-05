"""Fill the Word table of contents (pandoc leaves the TOC field empty) so every viewer shows it.

  python3 tocfill.py              entries with placeholder page numbers
  python3 tocfill.py PDFTEXT      page numbers found by locating each heading in PDFTEXT (pdftotext -layout output)

Works on gx/ (the unzipped docx), always starting from the untouched gx/word/document.orig.xml, then re-zips
guide.docx. The field stays marked dirty, so Word refreshes it with its own page numbers when the file opens.
"""
import os, re, shutil, subprocess, sys

DOC, ORIG, STY = "gx/word/document.xml", "gx/word/document.orig.xml", "gx/word/styles.xml"
if not os.path.exists(ORIG):
    shutil.copy(DOC, ORIG)
d = open(ORIG).read()

heads = re.findall(r'<w:bookmarkStart w:id="\d+" w:name="([^"]+)"/><w:p><w:pPr><w:pStyle w:val="(Heading[12])"/>(.*?)</w:p>', d)
heads = [(b, s, "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", body))) for b, s, body in heads]


def key(s):
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'")
    return re.sub(r"\s+", "", s)


if len(sys.argv) > 1:
    # drop the TOC's own lines (dot leaders) so only the headings themselves are found
    pages = [key("\n".join(l for l in p.split("\n") if not re.search(r"\.{4,}\s*\d+\s*$", l)))
             for p in open(sys.argv[1]).read().split("\f")]
    nums, at = [], 0
    for b, s, t in heads:
        k = key(t)[:30]
        at = next(i for i in range(at, len(pages)) if k in pages[i])
        nums.append(at + 1)
else:
    nums = [888] * len(heads)

TAB = 9746  # text width in twips: A4 (11906) minus two 1080 margins
paras = []
for i, ((b, s, t), pg) in enumerate(zip(heads, nums)):
    start = ('<w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
             '<w:r><w:instrText xml:space="preserve">TOC \\o "1-2" \\h \\z \\u</w:instrText></w:r>'
             '<w:r><w:fldChar w:fldCharType="separate"/></w:r>') if i == 0 else ""
    end = '<w:r><w:fldChar w:fldCharType="end"/></w:r>' if i == len(heads) - 1 else ""
    paras.append(
        f'<w:p><w:pPr><w:pStyle w:val="TOC{s[-1]}"/><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="{TAB}"/></w:tabs></w:pPr>'
        f'{start}<w:hyperlink w:anchor="{b}" w:history="1"><w:r><w:t xml:space="preserve">{t}</w:t></w:r>'
        f'<w:r><w:tab/></w:r><w:r><w:t>{pg}</w:t></w:r></w:hyperlink>{end}</w:p>')

old = ('<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve">TOC \\o "1-2" \\h \\z \\u'
       '</w:instrText><w:fldChar w:fldCharType="separate"/><w:fldChar w:fldCharType="end"/></w:r></w:p>')
assert d.count(old) == 1, "empty TOC field not found"
open(DOC, "w").write(d.replace(old, "".join(paras)))

st = open(STY).read()
if 'w:styleId="TOC1"' not in st:
    st = st.replace("</w:styles>",
        '<w:style w:type="paragraph" w:styleId="TOC1"><w:name w:val="toc 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>'
        '<w:uiPriority w:val="39"/><w:unhideWhenUsed/><w:pPr><w:spacing w:before="100" w:after="20"/></w:pPr><w:rPr><w:b/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="TOC2"><w:name w:val="toc 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>'
        '<w:uiPriority w:val="39"/><w:unhideWhenUsed/><w:pPr><w:spacing w:before="0" w:after="20"/><w:ind w:left="240"/></w:pPr></w:style>'
        "</w:styles>")
    open(STY, "w").write(st)

# document.orig.xml must not go into the package
subprocess.run("cd gx && rm -f ../guide.docx && zip -qrX ../guide.docx . -x word/document.orig.xml", shell=True, check=True)
print("TOC entries:", len(paras), "pages:", nums[:6], "...", nums[-3:])
