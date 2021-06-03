import pyttsx3 as sp
import PyPDF2 as pdf

book = open('oob.pdf', 'rb')
pdfreader =pdf.PdfFileReader(book)

pages = pdfreader.numPages
speaker = sp.init()
page = pdfreader.getPage(7)

###############################
speaker.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
###################################
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
speaker.stop()