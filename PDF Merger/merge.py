import os
import glob
from PyPDF2 import PdfFileMerger

textfile = []
for file in glob.glob("*.pdf"):
        textfile.append(file)

        
#files = os.listdir(".pdf")
print(textfile)
##pdfs = [ 'hp1.pdf','hp2.pdf', 'hp3.pdf', 'hp4.pdf',  'hp55.pdf','hp5.pdf', 'hp6.pdf', 'hp7.pdf', 'hp8.pdf', 'hp9.pdf','hp10.pdf', 'hp11.pdf', 'hp12.pdf', 'hp13.pdf', 'hp14.pdf' ]
##
pdfs = textfile
merger = PdfFileMerger()

for pdf in pdfs:
	merger.append(pdf)

merger.write("Test1.pdf")

merger.close()
