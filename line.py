def line():
    # Ingreso de datos
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))

    # Cálculo de Y1 e Y2 usando la ecuación Y = AX + B
    Y1 = A * X1 + B
    Y2 = A * X2 + B

    # Cálculo de distancia entre los dos puntos
    distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

    # Mostrar resultados
    print(f"\nEl coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")

    print(f"\nPara la siguiente ecuación:\n\tY = {A}X + {B}")

    print(f"\nDados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})")

    print(f"\nLa distancia entre ellos es: {distancia}")

