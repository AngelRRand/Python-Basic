def mensaje(dia, lista, count, tiempo):
    ticket = f"""
----------------------------------------------------
Fecha de búsqueda: {dia}

    ARCHIVO		NRO. SERIE
    -------		----------
"""
    print(ticket)

    for dic in lista:

        for t, a in dic.items():
            print(f"""
    {t}      {a}
""")


    ticketTop = f"""
Números encontrados: {count}
Duración de la búsqueda: {tiempo} segundos
----------------------------------------------------
"""
    print(ticketTop)