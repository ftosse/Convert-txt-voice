import pyttsx3
import PyPDF2

# Inicializar el motor de voz
engine = pyttsx3.init()

# Abrir el archivo PDF
with open('lectura.pdf', 'rb') as f:
    pdf = PyPDF2.PdfFileReader(f)
    text = ""
    # Iterar a través de todas las páginas del PDF
    for page in range(pdf.getNumPages()):
        text += pdf.getPage(page).extractText()

# Decir el texto
engine.say(text)

# Ejecutar el motor de voz
engine.runAndWait()