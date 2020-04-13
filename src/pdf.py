from fpdf import FPDF 
import pandas as pd
from plot import *
from merge_data import *
from adq_api import *
import functions as f



def pdf_generator(pdf):
    pdf = FPDF(format='letter', unit='in')
    pdf.l_margin = pdf.l_margin*4.0
    pdf.r_margin = pdf.r_margin*4.0
    pdf.t_margin = pdf.t_margin*4.0
    pdf.b_margin = pdf.b_margin*4.0
    pdf.add_page()

    effective_page_width = pdf.w - 2*pdf.l_margin

    epw = pdf.w - pdf.l_margin - pdf.r_margin
    eph = pdf.h - pdf.t_margin - pdf.b_margin

    pdf.set_font("helvetica", size=15)
    pdf.multi_cell(effective_page_width, 0.25,'Movie Report')
    pdf.ln(0.30)

    movie = f.get_api()
    text = f.json_to_text(movie)

    pdf.set_font('helvetica', 'B', 10.0)
    pdf.cell(1.0, 0.15, 'Requested Movie:')
    pdf.ln(0.30)

    pdf.set_font('helvetica', '', 10.0)
    pdf.multi_cell(effective_page_width, 0.15, text)
    pdf.ln(0.30)

    pdf.set_font('helvetica', 'B', 10.0)
    pdf.cell(1.0, 0.15, 'Movie Rating by Database:')
    pdf.ln(0.30)

    plot = ratings_plot()
    pdf.image("../OUTPUT/plot.png", w=pdf.w/2.0, h=pdf.h/4.0)
    pdf.ln(0.10)

    pdf.set_font('helvetica', 'B', 10.0)
    pdf.cell(1.0, 0.15, 'Additional Info:')
    pdf.ln(0.30)

    imdb = check_imdb()
    pdf.set_font("helvetica", 'I', size=8)
    pdf.multi_cell(effective_page_width, 0.15, imdb)
    pdf.ln(0.25)

    oscars = check_oscars()
    pdf.set_font("helvetica", 'I', size=8)
    pdf.multi_cell(effective_page_width, 0.15, oscars)
    pdf.ln(0.25)

    pdf.output('../OUTPUT/report.pdf', 'F')
