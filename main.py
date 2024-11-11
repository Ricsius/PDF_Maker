from fpdf import FPDF
import pandas as pd

PAGES_KEY = "Pages"
TOPIC_KEY = "Topic"

def inser_header(pdf, text):
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=text, align="L", ln=1)
    pdf.line(10, 21, 200, 21)

def insert_footer(pdf, text, lines):
    pdf.ln(lines)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=text, align="R")

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_auto_page_break(auto=False, margin=0)

data = pd.read_csv("topics.csv")

for index, row in data.iterrows():
    topic = row[TOPIC_KEY]

    pdf.add_page()
    inser_header(pdf, topic)
    insert_footer(pdf, topic, 265)

    remaining_pages = row[PAGES_KEY] - 1

    for i in range(remaining_pages):
        pdf.add_page()
        insert_footer(pdf, topic, 277)

pdf.output("output.pdf")