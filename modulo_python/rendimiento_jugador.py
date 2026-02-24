estadisticas_partido = {
    "minutos_jugados": 90,
    "distancia_km": 11.2,
    "pases_acertados": 45,
    "tarjeta_amarilla": False
}

estadisticas_partido["minutos_jugados"] = 75
efectividad_pases = estadisticas_partido["pases_acertados"] / estadisticas_partido["minutos_jugados"]

print(estadisticas_partido["distancia_km"])
print(f"Efectividad por minuto: {efectividad_pases}")