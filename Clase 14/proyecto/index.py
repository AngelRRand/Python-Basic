import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

ruta = "Empleados"
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta}\{nombre}")
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


def codificar(imagenes):
    lista_codificada = []

    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        codificado = fr.face_encodings(imagen)[0]

        lista_codificada.append(codificado)

    return lista_codificada


def registrar_ingresos(persona):

    f = open("registro.csv", "r+")
    lista_datos = f.readline()
    nombres_registrado = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registrado.append(ingreso[0])

        if persona not in nombres_registrado:
            ahora = datetime.now()
            string_ahora = ahora.strftime('%H:%M:%S')
            f.writelines(f'\n{persona}, {string_ahora}')

lista_empleados_codificada = codificar(mis_imagenes)


captura = cv2.VideoCapture(0)

exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):

        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        indice_coincidencia = numpy.argmin(distancias)

        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ningun empleado")
        else:
            print("Bienvenido al trabajo")

            nombre = nombres_empleados[indice_coincidencia]

            registrar_ingresos(nombre)






