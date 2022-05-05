import PyPDF2

# create file object variable
# opening method will be rb
pdffileobj = open('./Priyanka.pdf', 'rb')

# create reader variable that will read the pdffileobj
pdfreader = PyPDF2.PdfFileReader(pdffileobj)

# This will store the number of pages of this pdf file
x = pdfreader.numPages

# create a variable that will select the selected number of pages
pageobj = pdfreader.getPage(0)

text = pageobj.extractText()

file1 = open(
    r"./priyank.txt", "a")
file1.writelines(text)
