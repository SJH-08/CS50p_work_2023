from fpdf import FPDF

class PDF(FPDF):
        def __init__(self, name):
                #Orientation of PDF = portrait
                #Format of PDF = A4 (210 mm wide x 297 mm tall)
                super().__init__(orientation="P", unit="mm", format="A4")
                self.add_page()
                self.name = name


#Top part = text centered hz "CS50 shirtficate"
        def header(self):
                #Set font
                self.set_font("Helvetica", size=50)
                #Set color text
                self.set_text_color(0, 0, 0)
                #Print title
                self.cell(0, 25, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
                #Line break
                self.ln(20)


#Shirt image centered hz
        def set_image(self):
                self.image("shirtificate.png", w=self.epw)


#User name on top of the shirt in white text
        def chapter_body(self, name):
                #Set font
                self.set_font("Helvetica", size=30)
                #Set color background
                self.set_text_color(255, 255, 255)
                #Print title
                self.cell(20, 270, f'{name}' + " took CS50",new_x="LMARGIN", new_y="NEXT", align="C")



#Prompt user for name
name = input("Name: ")
name = PDF(name)
name.output("shirtificate.pdf")

