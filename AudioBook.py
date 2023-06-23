#pip install pyttsx3
#pip install PyPDF2

import pyttsx3
import PyPDF2

file=open("HRDOB_mcq.pdf",mode="rb")
pdf_reader = PyPDF2.PdfReader(file)
page=len(pdf_reader.pages)
#print(page)
coco=pyttsx3.init()
for i in range(0,page):

    read_page=pdf_reader.pages[i]
    text=read_page.extract_text()
    coco.say(text)
coco.runAndWait()