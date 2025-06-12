from pdf2docx import Converter

pdf_file = 'sample.pdf'
docx_file = 'result.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()