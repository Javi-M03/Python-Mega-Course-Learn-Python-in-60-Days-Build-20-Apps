from fpdf import FPDF
import pandas 

df = pandas.read_csv("../topics.csv")

pdf = FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

for index,row in df.iterrows():
    pdf.add_page()
        #Set the header
    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"], align="L",ln=1)
    
    for i in range(20,298,10):
        pdf.line(10,i,200,i)
    
    

    
    #Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"], align="R")
    



    for i in range(row["Pages"] - 1):
        pdf.add_page()
        #Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times",style="I",size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row["Topic"], align="R")

        for i in range(20,298,10):
            pdf.line(10,i,200,i)



pdf.output("student_output.pdf")