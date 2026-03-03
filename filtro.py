rendimiento = [85, 92, 60, "lesionado", 78, 99]

for valor in rendimiento:
    
    if valor == "lesionado":
        print(f"Dato corrupto")

    elif valor >= 90:
        print(f"Nivel Élite")

    elif valor < 69:
        print(f"Requiere descanso")

    else:
        print(f"Óptimo")
