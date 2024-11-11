from fpdf import FPDF
import pandas as pd

PAGES_KEY = "Pages"
TOPIC_KEY = "Topic"

pdf = FPDF(orientation="P", unit="mm", format="A4")
data = pd.read_csv("topics.csv")

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row[TOPIC_KEY], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    remaining_pages = row[PAGES_KEY] - 1

    for i in range(remaining_pages):
        pdf.add_page()

pdf.output("output.pdf")