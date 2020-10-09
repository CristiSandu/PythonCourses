import pyttsx3
import PyPDF2

book = open("The Silmarillion (Illustrated ebook).pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(4)
text = page.extractText()
speaker.setProperty('rate', 300)
print(text)
speaker.say(text)
speaker.runAndWait()