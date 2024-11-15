from fpdf import FPDF
import pandas as pd

df = pd.read_csv("articles.csv", dtype={"id":str})

class Receipt:
    def __init__(self):
        pass

    def generate(self,article_name,article_price):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.1", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {article_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {article_price}", ln=1)

        pdf.output("receipt.pdf")


class Articles:
    def __init__(self, receipt_id):
        self.receipt_id = receipt_id
        self.name =  df.loc[df["id"] == self.receipt_id,"name"].squeeze()
        self.price = df.loc[df["id"] == self.receipt_id,"price"].squeeze()
        

    def reduce(self):
        self.stock = df.loc[df["id"] == self.receipt_id,"in stock"].squeeze()
        df.loc[df["id"] == self.receipt_id] = self.stock -1
        df.to_csv("articles.csv", index=False)


    
    

print(df)
article_ID = input("Choose an article to buy : ")
article = Articles(article_ID)
receipt = Receipt()
receipt.generate(article.name,article.price)
article.reduce()

