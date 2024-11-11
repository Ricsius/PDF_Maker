from fpdf import FPDF
import pandas as pd

PAGES_KEY = "Pages"
TOPIC_KEY = "Topic"
A4_WIDTH = 210
A4_HEIGHT = 297
MARGIN = 10
HEADER_HEIGHT = 12
FOOTER_HEIGHT = 10
LINE_DISTANCE = 10
DATA_PATH = "topics.csv"
OUTPUT_PATH = "output.pdf"

def inser_header(pdf, text):
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=HEADER_HEIGHT, txt=text, align="L", ln=1)

def insert_footer(pdf, text, lines):
    pdf.ln(lines)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=FOOTER_HEIGHT, txt=text, align="R")

def draw_lines(pdf, start_y, end_y):
    for current_y in range(start_y, end_y, LINE_DISTANCE):
        pdf.line(MARGIN, current_y, A4_WIDTH - MARGIN, current_y)

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_auto_page_break(auto=False, margin=0)

data = pd.read_csv(DATA_PATH)

for index, row in data.iterrows():
    topic = row[TOPIC_KEY]

    pdf.add_page()
    inser_header(pdf, topic)
    draw_lines(pdf, 21, A4_HEIGHT - FOOTER_HEIGHT)
    insert_footer(pdf, topic, 265)

    remaining_pages = row[PAGES_KEY] - 1

    for i in range(remaining_pages):
        pdf.add_page()
        draw_lines(pdf, 21, A4_HEIGHT - FOOTER_HEIGHT)
        insert_footer(pdf, topic, 277)

pdf.output(OUTPUT_PATH)