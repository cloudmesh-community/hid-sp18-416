FILE=report
LATEX=pdflatex
BIBTEX=bibtex

all: clean iureport 
	$(LATEX) ${FILE}
	$(BIBTEX) ${FILE}
	$(LATEX) ${FILE}
	$(LATEX) ${FILE}

iureport:
	cp ../../hid-sample/tex/format/iureport.cls .
	cp ../../hid-sample/tex/format/ACM-Reference-Format.bst .

check:
	chktex -q -n 13 -n 8 content.tex

clean:
	rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut *bcf *idx *run.xml *.bst *.cls
	cd paper; rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut *bcf *idx *run.xml
	cd project-paper; rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut *bcf *idx *run.xml
	cd technology; rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut *bcf *idx *run.xml
