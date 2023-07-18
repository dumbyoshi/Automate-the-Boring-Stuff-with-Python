import PyPDF2
import os
os.chdir('F:\Books\Self help')
pdfFile = open('Make it Stick The Science of Successful Learning.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFile)
print(pdfFile)
page = reader.pages(6)
page.extractText()