import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia



id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELETokens\TTS_MS_ES-ES_HELENA_11.0"



# Escuchar

def transformar_audio():

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause = 0.5

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
    engine.setProperty("voice", id2)

    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():

    dia = datetime.date.today()

    dia_semana = dia.weekday()

    calendario = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    hablar(f"Hola Horacio. ¿Como estas?, hoy es {calendario[dia_semana]}")

def pedir_Hora():
    hora = datetime.datetime.now()

    oracion = f"En este momento son las {hora.hour} horas con {hora.minute} minutos"

    hablar(oracion)

def saludo_inicial():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 23:
        momento = "Buen dia"
    else:
        momento = "Buenas tardes"
    hablar(f"{momento} soy Helena, tu asistente personal. Por favor, dime en que te puedo ayudar")


def pedir_cosas():

    saludo_inicial()

    comenzar = True

    while comenzar:
        pedido = transformar_audio().lower()

        if 'abrir youtube' in pedido:
            hablar("Con gusto, estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abrir navegador" in pedido:
            hablar("Estoy en eso")
            webbrowser.open("https://www.google.com/?hl=es")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_Hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando en wikipedia...")
            pedido = pedido.replace("busca en wikipedia", "")

            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)

            hablar("Wikipedia dice lo siguiente: ")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("Ya mismo estoy en eso")
            pedido = pedido.replace("busca en internet", "")

            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("Reproduciendo...")
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido or "chiste" in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera =  {
                "apple":"APPL",
                "amazon": "AMZN",
                "google": "GOOGL"
            }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontré, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdon pero no la he encontrada")
                continue
        elif "adiós" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break



pedir_cosas()








