import pyttsx3
import PyPDF2
book = open('book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages


reader = pyttsx3.init()
rate = reader.getProperty('rate')
print (rate)
reader.setProperty('rate', 200)
print (rate)

for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
