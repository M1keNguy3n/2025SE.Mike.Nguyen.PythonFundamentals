from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image(
    "/workspaces/2025SE.Mike.Nguyen.PythonFundamentals/8-OOP/shirtificate/shirtificate.png",
    h=pdf.eph,
    w=pdf.epw,
)
pdf.output("pdf-with-image.pdf")
