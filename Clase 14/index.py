import cv2

import face_recognition as fr

""" Carga dos fotos """
foto_control = fr.load_image_file("fotoA.jpg")
foto_prueba = fr.load_image_file("fotoB.jpg")

""" Cambia el formato de colores """
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)


""" Localizacion de la cara """
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]


""" Dibujo de rectangulo """
cv2.rectangle(
    foto_control,
    (lugar_cara_A[3], lugar_cara_A[0]),
    (lugar_cara_A[1], lugar_cara_A[2]),
    (0, 255, 0),
    2,
)

cv2.rectangle(
    foto_control,
    (lugar_cara_B[3], lugar_cara_B[0]),
    (lugar_cara_B[1], lugar_cara_B[2]),
    (0, 255, 0),
    2,
)

""" Compara las dos fotos """
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)

""" Medir distancia """
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

""" mostrar resultado """
cv2.putText(
    foto_prueba,
    f"{resultado} {distancia.round(2)}",
    (50, 50),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (0, 255, 0),
    2,
)

cv2.imshow("foto control", foto_control)
cv2.imshow("foto prueba", foto_prueba)


cv2.waitKey(0)
