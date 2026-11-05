# Word edition build scripts

These scripts produce `../ME_F211_Study_Guide_Ch1-6.docx` from the chapter Markdown files.

- `extract.py` crops the original problem figures from the slide PDFs and question papers.
- `figlib.py` and `make_figs.py` draw the worked diagrams with matplotlib: FBDs, truss force maps, SFD/BMD, axial and torque diagrams, Mohr's circles and stress elements.
- `build.py` inserts the figures into the Markdown files. `finish.sh` then converts the result to .docx with pandoc. Equations become native Word equations.

The paths inside the scripts point at the session scratch folder. Change `D`, `G` and `IMG` at the top of each script to re-run them elsewhere.
