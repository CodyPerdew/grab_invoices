import PyPDF2
import re
import os
from PyPDF2 import PdfFileWriter, PdfFileWriter
from pathlib import Path

#Goes through a folder of PDFs, copies page 1 of each PDF to a new document.




billreq = PdfFileWriter()       #create a new empty PDF
pdffolder = str(input('Please type the path to the folder. Make sure it only contains PDFs'))   #specify the directory

for item in os.listdir(pdffolder):      #iterate through the folder

    pdfFileObj = open(pdffolder+'/'+item, 'rb') #Specify each PDF as a pdfFileObject
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)    #run pdfFileReader on each 

    inv = pdfReader.getPage(0)      #copies page 1

    billreq.addPage(inv)            #adds page 1 to our previously created PDF



with Path("BillReq.pdf").open(mode="wb") as output_file:    #writes our previously created PDF to a new file
    billreq.write(output_file)
