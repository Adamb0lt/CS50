# Documentation literally gave me all the code I needed
# just needed to make small adjustments

from fpdf import FPDF


class PDF(FPDF):
    #name correlates to the ask from main
    def __init__(self,name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Times", size=24)
        self._pdf.cell(0, 40, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w = self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x = 47, y = 140, txt = f"{name} took CS50")
        self._pdf.output("shirtificate.pdf")


def main():
    ask = input("Name: ")
    PDF(ask)



if __name__ == "__main__":
    main()
