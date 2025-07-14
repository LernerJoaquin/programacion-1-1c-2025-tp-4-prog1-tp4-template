def leap_year():
    # Un año es bisiesto si es divisible por 4 y no es divisible por 100,
    # o si es divisible por 400
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False
        # Programa principal
anio = int(input("Ingrese un año: "))

if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} no es bisiesto")
