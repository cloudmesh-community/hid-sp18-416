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


clean:
	rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut *bcf *idx *run.xml
	cd paper; rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut *bcf *idx *run.xml
	cd project-paper; rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut *bcf *idx *run.xml
	cd technology; rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut *bcf *idx *run.xml
