MAIN_FILE = DYI_Main

PDFLATEX = pdflatex
PSTOPDF = ps2pdf

MACRO_GENERATOR = ./gen_Current_Macros.py
MACRO_INPUTES = gen_config.py           \
                gen_holidays.py
CHARTS_GENERATOR = ./gen_charts.py

FILES_TEX = DYI_Main.tex                \
            DYI_Year_Calendar.tex       \
            DYI_Monthly_Planner.tex     \
            DYI_Weekly_Planner.tex

# generated files
FILES_TEX_GEN = DYI_i18n.tex                   \
                DYI_Month_Tables.tex           \
                DYI_Monthly_Planner_Tables.tex \
                DYI_Weekly_Planner_Tables.tex

CHARTS_TEX_GEN = ascii.tex \
				 hex.tex

GNUPLOT_INPUT = 52wks.gnuplot daily.gnuplot
GNUPLOT_TEX = 52wks.tex \
			  daily.tex
GNUPLOT_INTERMEDIATE = 52wks.eps \
					   daily.eps
GNUPLOT_OUTPUT = 52wks.pdf \
				 daily.pdf \
				 52wks.tex \
				 daily.tex \
				 52wks-eps-converted-to.pdf \
				 daily-eps-converted-to.pdf
GNUPLOT = gnuplot -c

DEFAULT: $(FILES_TEX) $(FILES_TEX_GEN) $(GNUPLOT_TEX) $(GNUPLOT_OUTPUT) $(CHARTS_TEX_GEN)
	$(PDFLATEX) $(MAIN_FILE)

$(CHARTS_TEX_GEN): $(CHARTS_GENERATOR)
	$(CHARTS_GENERATOR)

$(FILES_TEX_GEN): $(MACRO_GENERATOR) $(MACRO_INPUTES)
	$(MACRO_GENERATOR)

$(GNUPLOT_OUTPUT): $(GNUPLOT_INPUT)

%.tex: %.gnuplot
	$(GNUPLOT) $(@:.tex=.gnuplot)

clean:
	rm -f $(FILES_TEX:.tex=.dvi)
	rm -f $(FILES_TEX:.tex=.aux)
	rm -f $(FILES_TEX_GEN:.tex=.aux)
	rm -f $(FILES_TEX_GEN)
	rm -f $(GNUPLOT_OUTPUT)
	rm -f $(GNUPLOT_INTERMEDIATE)
	rm -f $(MAIN_FILE).log
	rm -f *~

realclean: clean
	rm -f $(MAIN_FILE).pdf

dist: clean
	cd .. ; \
	tar -czvf DIY_Organizer-dist_`date +%F`.tar.gz DIY_Organizer

realdist: realclean
	cd .. ; \
	tar -czvf DIY_Organizer-realdist_`date +%F`.tar.gz DIY_Organizer

