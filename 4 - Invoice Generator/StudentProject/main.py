from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("textfiles/*.txt")
pdf =  FPDF(orientation="P",unit="mm",format="A4")


for index,filepath in enumerate(filepaths):
    pdf.add_page()
    filename = Path(filepath).stem.capitalize()
    pdf.set_font(family="Times",size=24,style="B")
    pdf.cell(w=50,h=8,txt=f"{filename}",ln=1)
    pdf.set_font(family="Times",size=10)

    #Content
    with open(filepath) as file:
        content = file.read()
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"PDFs/output.pdf")
