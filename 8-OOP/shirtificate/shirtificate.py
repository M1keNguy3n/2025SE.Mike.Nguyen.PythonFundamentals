from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_right_margin(0)
pdf.set_font("helvetica", "B", 30)

pdf.image(
    name="/workspaces/2025SE.Mike.Nguyen.PythonFundamentals/8-OOP/shirtificate/shirtificate.png",
    y=70,
    x=16.5,
    w=180,
)
pdf.cell(75, 200)
pdf.cell(w=45, h=50, text="CS50 Shirtificate", align="C")
pdf.set_x(0)
pdf.set_y(0)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(w=0, h=pdf.eph, text="Mike Nguyen finished CS50.", align="C")


pdf.output("image.pdf")
