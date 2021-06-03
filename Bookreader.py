import pyttsx3 as sp
import PyPDF2 as pdf

book = open('oob.pdf', 'rb')
pdfreader =pdf.PdfFileReader(book)

pages = pdfreader.numPages
speaker = sp.init()
page = pdfreader.getPage(7)

text = page.extractText()
speaker.say(text)
speaker.runAndWait()
speaker.stop()