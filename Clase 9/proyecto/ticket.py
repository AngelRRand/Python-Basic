def mensaje(dia, lista, count, tiempo):
    ticket = f"""
----------------------------------------------------
Fecha de búsqueda: {dia}

    ARCHIVO		NRO. SERIE
    -------		----------
"""
    print(ticket)
    for t, a in lista:
            print(f"""
    {t}      {a}
""")
    ticketTop = f"""
Números encontrados: {count}
Duración de la búsqueda: {tiempo} segundos
----------------------------------------------------
"""
    print(ticketTop)