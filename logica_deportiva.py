puntos_actuales = 15
historial_resultados = []

print("--- INICIANDO SIMULADOR---")

while True:
    resultado_partido = input("Ingresa resultado (ganar/empatar/perder o 'salir'): ").lower()
    

    if resultado_partido == "salir":
        print(f"Simulacion terminada. Puntos finales: {puntos_actuales}")
        print(f"Historial de la temporada: {historial_resultados}")
        break # Esta instruccion destruye el ciclo while y termina el programa

    if resultado_partido == "ganar":
        puntos_actuales = puntos_actuales + 3
        historial_resultados.append(resultado_partido)
    elif resultado_partido == "empatar":
        puntos_actuales = puntos_actuales + 1
        historial_resultados.append(resultado_partido)
    elif resultado_partido == "perder":
        puntos_actuales = puntos_actuales + 0
        historial_resultados.append(resultado_partido)
    else:
        print("ERROR: Dato no reconocido. No se sumaron puntos")

    print(f"Marcador temporal: {puntos_actuales} puntos\n")
