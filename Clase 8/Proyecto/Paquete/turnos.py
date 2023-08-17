
def generar_turno(tipo):
    num = 1
    while True:
        yield print(f"{tipo} - {num}")
        num += 1

