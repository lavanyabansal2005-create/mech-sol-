# Word edition build scripts

These scripts produce `../ME_F211_Study_Guide_Ch1-6.docx` and `../ME_F211_Study_Guide_Ch1-6.pdf` from the chapter Markdown files.

- `extract.py` crops the original problem figures from the slide PDFs and question papers. `crop_book.py` crops the figures of the Crandall end-of-chapter problems from the scanned textbook pages.
- `figlib.py` and `make_figs.py` draw the worked diagrams with matplotlib: FBDs, truss force maps, SFD/BMD, axial and torque diagrams, load–deflection and design curves, Mohr's circles and stress elements.
- `build.py` inserts the figures into the Markdown files and tidies the text for pandoc.
- `finish.sh` converts the result to .docx with pandoc, using `ref.docx` for page size and styles. Equations become native Word equations. `fixxml.py` then puts pandoc's XML into the order the Office schema expects.
- `tocfill.py` writes the table of contents into the file, because pandoc leaves it empty until Word refreshes it.
- `make_all.sh` runs the whole chain: Word file, PDF (LibreOffice), contents page numbers, then a schema check.

The paths inside the scripts point at the session scratch folder. Change `D`, `G` and `IMG` at the top of each script (and the paths in the shell scripts) to re-run them elsewhere.
