import pandas
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("textfiles/*.txt")
pdf =  FPDF(orientation="P",unit="mm",format="A4")


for filepath in filepaths:
    df = pandas.read_csv(filepath)
    pdf.add_page()
    filename = Path(filepath).stem.capitalize()
    pdf.set_font(family="Times",size=24,style="B")
    pdf.cell(w=50,h=8,txt=f"{filename}")
    pdf.set_font(family="Times",size=12,style="B")
    pdf.cell(w=50,h=8,txt=f"{df}")

pdf.output(f"PDFs/output.pdf")