import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia






# Escuchar

def transformar_audio():

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause = 0.8

        # Informar que comenzo la grabacion
        print("Habla")

        # guardar lo que escuche
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # Prueba lo ingresado

            print(f"Dijiste: {pedido}")

            return pedido
        
        # En caso de que no comprenda el audio
        except sr.UnknownValueError:

            # Prueba de que no comprendio el audio

            print("No entiendo")
            return "Sigo esperando"
        
        # En caso de no resolver el audio
        except sr.RequestError:

            # Prueba de que no comprendio el audio
            print("No hay servicio")
            return "Sigo esperando"
        
        # Error inesperado
        except:

            # Prueba de que no comprendio el audio
            print("Algo salio mal")
            return "Sigo esperando"
        

def hablar(mensaje):

    engine = pyttsx3.init()

    engine.say(mensaje)
    engine.runAndWait()


hablar("I am Horacio")


