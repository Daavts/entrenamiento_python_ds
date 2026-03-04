rendimiento = [85, 92, 60, "lesionado", 78, 99]
clasificados = []

for valor in rendimiento:
    
    if valor == "lesionado":
        print(f"Dato corrupto")

    elif valor >= 90:
        clasificados.append(valor)
        print(f"Nivel Élite")

    elif valor < 70:
        print(f"Requiere descanso")

    else:
        clasificados.append(valor)
        print(f"Óptimo")

print(clasificados)