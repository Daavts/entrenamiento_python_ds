dia_semana = input("¿Qué día es hoy? (Ej. Lunes, Domingo): ").capitalize()
if dia_semana == "Domingo":
    print(f"DESCANSO TOTAL")
else:
    asistencia_oficina = input("¿Vas a la oficina hoy? (si/no): ").lower()
    if asistencia_oficina == "si":
        print(f"Rutina de supervivencia postural (Cero impacto)")
    else:    
        fatiga = int(input("Nivel de fatiga (1-10): "))
        if fatiga >= 8:
            print(f"Recuperacion activa")
        else:
            print("--- EVALUANDO CARGA FÍSICA ---")
            print(f"Acondicionamiento Box to Box (Alta intensidad)")






    
   
       
        