serie = 'N-02'


match serie:
    case "N-02":
        print("Samsung")





cliente = {
    "nombre": "Federico",
    "edad": 45,
    "ocupacion": "instructor"
}



pelicula = {
    "titulo": "Matrix",
    "ficha_tecnica": {
        "protagonista": "Keanu",
        "director": "Lana"
    }
}

elementos = [cliente, pelicula, 'libro']

for e in elementos :
    match e:
        case {
            "nombre": nombre,
            "edad": edad,
            "ocupacion": ocupacion
        }:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {
            "titulo": titulo,
            "ficha_tecnica": {
                "protagonista": protagonista,
                "director": director
            }
        }: 
            print("Es un pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")