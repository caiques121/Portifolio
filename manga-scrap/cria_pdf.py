import img2pdf
import os

def cria_pdf(capitulo):
    import glob
    list_of_files = sorted(glob.glob('output/*.png'), key=os.path.getmtime)

    with open("pdfs/" + str(capitulo) + ".pdf", "wb") as f:
        f.write(img2pdf.convert(list_of_files))