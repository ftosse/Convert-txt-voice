import pyttsx3
import PyPDF2

def convert_pdf_to_audio(pdf_file):
    # Inicializar el motor de voz
    engine = pyttsx3.init()

    # Abrir el archivo PDF
    with open(pdf_file, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        text = ""
        # Iterar a través de todas las páginas del PDF
        for page in range(pdf.getNumPages()):
            text += pdf.getPage(page).extractText()

    # Decir el texto
    engine.say(text)

    # Ejecutar el motor de voz
    engine.runAndWait()


def convert_pdf_to_audio_id(pdf_file, voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'):
    # Inicializar el motor de voz
    engine = pyttsx3.init()
    
    #set the language and accent
    engine.setProperty('voice', voice_id)
    
    #Identificar la voz, el id, genero e idioma utilizado
    voices=engine.getProperty('voices')
    for voice in voices:
        print("Nombre: " + voice.name)
        print("Identificador: " + voice.id)
        print("")
    
    
    # Abrir el archivo PDF
    with open(pdf_file, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        text = ""
        # Iterar a través de todas las páginas del PDF
        for page in range(pdf.getNumPages()):
            text += pdf.getPage(page).extractText()

    # Decir el texto
    engine.say(text)

    # Ejecutar el motor de voz
    engine.runAndWait()

def convert_pdf_to_audio_name(pdf_file, voice_name='Microsoft David Desktop'):
    # Inicializar el motor de voz
    engine = pyttsx3.init()
    
    #set the language and accent
    #engine.setProperty('voice', voice_id)
    engine.setProperty('voice', voice_name)

    #Identificar la voz, el id, genero e idioma utilizado
    voices=engine.getProperty('voices')
    for voice in voices:
        print("Nombre: " + voice.name)
        print("Identificador: " + voice.id)
        #print("Género: " + voice.gender)
        #print("Idioma: " + voice.languages[0])
        print("")
    
    
    # Abrir el archivo PDF
    with open(pdf_file, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        text = ""
        # Iterar a través de todas las páginas del PDF
        for page in range(pdf.getNumPages()):
            text += pdf.getPage(page).extractText()

    # Decir el texto
    engine.say(text)

    # Ejecutar el motor de voz
    engine.runAndWait()



if __name__=="__main__":
	# Funciones validadas
    #convert_pdf_to_audio('lectura.pdf')
    convert_pdf_to_audio_id('lectura.pdf', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
    
    #Falta sin validar
    #convert_pdf_to_audio_name('lectura.pdf','Microsoft David Desktop')
else:
	print("Modulo Importado: [", os.path.basename(__file__), "]")

    