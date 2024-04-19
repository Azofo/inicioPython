primero = int(input("Escribe el primer número:"))
segundo = int(input("Escribe el segundo número:"))

calculo = 6

while calculo != 0:

    print("Elige la operación a realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("0. Salir")

    calculo = int(input("Opción: "))

    match calculo:

        case 1:
            print("El resultado de la suma es:", primero + segundo)
        case 2:
            print("El resultado de la resta es:", primero - segundo)
        case 3:
            print("El resultado de la multiplicación es:", primero * segundo)
        case 4:
            if segundo == 0:
                print("División entre 0. Imposible de calcular")
            else:
                print("El resultado de la división es:", primero / segundo)
        case 0:
            print("¡Hasta otra!")
        case _:
            print("Escribe una opción válida")