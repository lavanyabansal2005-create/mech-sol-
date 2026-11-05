set -e
cd /tmp/claude-0/-home-user-mech-sol-/5e236ef2-e171-5cb2-82aa-007544f55ba5/scratchpad/docx
OFFICE=/root/.claude/skills/synced/d96b4960-6118-4779-8644-4eee6d869c7d_31e9c7db-a397-4adc-97ac-efc82b59059d/docx/scripts/office
topdf() { rm -rf pv && mkdir pv && timeout 590 python3 $OFFICE/soffice.py --headless --convert-to pdf --outdir pv guide.docx > /dev/null 2>&1; pdftotext -layout pv/guide.pdf pv/guide.txt; }
bash finish.sh
python3 tocfill.py              # placeholder page numbers, same layout as the final TOC
topdf
python3 tocfill.py pv/guide.txt # real page numbers
topdf
python3 tocfill.py pv/guide.txt # check: numbers must not change
python3 $OFFICE/validate.py guide.docx | tail -1
pdfinfo pv/guide.pdf | grep Pages
