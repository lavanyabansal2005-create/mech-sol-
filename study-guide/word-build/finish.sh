set -e
cd /tmp/claude-0/-home-user-mech-sol-/5e236ef2-e171-5cb2-82aa-007544f55ba5/scratchpad/docx
python3 build.py
cat meta.yaml combined.md > full.md
pandoc full.md -f markdown+tex_math_dollars -o guide.docx --reference-doc=ref.docx --toc --toc-depth=2
rm -rf gx && mkdir gx && cd gx && unzip -q ../guide.docx
python3 - <<'PY'
import re
s=open('word/settings.xml').read()
head=s[:s.index('>',s.index('<w:settings'))+1]; body=s[len(head):s.rindex('</w:settings>')]
# split top-level children
kids=[]; i=0
while i<len(body):
    j=body.find('<',i)
    if j<0: break
    m=re.match(r'<([\w:]+)',body[j:]); tag=m.group(1)
    end_self=body.find('/>',j); end_open=body.find('>',j)
    if body[end_open-1]=='/': k=end_open+1
    else: k=body.index('</'+tag+'>',j)+len(tag)+3
    kids.append((tag,body[j:k])); i=k
kids.append(('w:updateFields','<w:updateFields w:val="true"/>'))
order=['w:writeProtection','w:view','w:zoom','w:removePersonalInformation','w:removeDateAndTime','w:doNotDisplayPageBoundaries','w:displayBackgroundShape','w:printPostScriptOverText','w:printFractionalCharacterWidth','w:printFormsData','w:embedTrueTypeFonts','w:embedSystemFonts','w:saveSubsetFonts','w:saveFormsData','w:mirrorMargins','w:alignBordersAndEdges','w:bordersDoNotSurroundHeader','w:bordersDoNotSurroundFooter','w:gutterAtTop','w:hideSpellingErrors','w:hideGrammaticalErrors','w:activeWritingStyle','w:proofState','w:formsDesign','w:attachedTemplate','w:linkStyles','w:stylePaneFormatFilter','w:stylePaneSortMethod','w:documentType','w:mailMerge','w:revisionView','w:trackRevisions','w:doNotTrackMoves','w:doNotTrackFormatting','w:documentProtection','w:autoFormatOverride','w:styleLockTheme','w:styleLockQFSet','w:defaultTabStop','w:autoHyphenation','w:consecutiveHyphenLimit','w:hyphenationZone','w:doNotHyphenateCaps','w:showEnvelope','w:summaryLength','w:clickAndTypeStyle','w:defaultTableStyle','w:evenAndOddHeaders','w:bookFoldRevPrinting','w:bookFoldPrinting','w:bookFoldPrintingSheets','w:drawingGridHorizontalSpacing','w:drawingGridVerticalSpacing','w:displayHorizontalDrawingGridEvery','w:displayVerticalDrawingGridEvery','w:doNotUseMarginsForDrawingGridOrigin','w:drawingGridHorizontalOrigin','w:drawingGridVerticalOrigin','w:doNotShadeFormData','w:noPunctuationKerning','w:characterSpacingControl','w:printTwoOnOne','w:strictFirstAndLastChars','w:noLineBreaksAfter','w:noLineBreaksBefore','w:savePreviewPicture','w:doNotValidateAgainstSchema','w:saveInvalidXml','w:ignoreMixedContent','w:alwaysShowPlaceholderText','w:doNotDemarcateInvalidXml','w:saveXmlDataOnly','w:useXSLTWhenSaving','w:saveThroughXslt','w:showXMLTags','w:alwaysMergeEmptyNamespace','w:updateFields','w:hdrShapeDefaults','w:footnotePr','w:endnotePr','w:compat','w:docVars','w:rsids','m:mathPr','w:attachedSchema','w:themeFontLang','w:clrSchemeMapping','w:doNotIncludeSubdocsInStats','w:doNotAutoCompressPictures','w:forceUpgrade','w:captions','w:readModeInkLockDown','w:smartTagType','sl:schemaLibrary','w:shapeDefaults','w:doNotEmbedSmartTags','w:decimalSymbol','w:listSeparator']
rank={t:i for i,t in enumerate(order)}
kids.sort(key=lambda k: rank.get(k[0],999))
open('word/settings.xml','w').write(head+''.join(k[1] for k in kids)+'</w:settings>')
s='updateFields' 
d=open('word/document.xml').read()
# keep figure images with their captions
open('word/document.xml','w').write(d)
print('updateFields' in s)
PY
python3 -c "p='[Content_Types].xml';s=open(p).read();s=s.replace('<Default Extension=\"xml\"','<Default Extension=\"png\" ContentType=\"image/png\"/><Default Extension=\"jpg\" ContentType=\"image/jpeg\"/><Default Extension=\"xml\"',1) if 'Extension=\"png\"' not in s else s;open(p,'w').write(s)"
rm -f ../guide.docx && zip -qrX ../guide.docx . && cd ..
