bandera = True
edad = input("Dime tu edad: ")
if int(edad) >= 18:
    nombre = input("¿Cómo te llamas? ")
    while bandera:
        peso = input("Dime tu peso: ")
        print(peso+" kg. ¿Es correcto?")
        condicion = input("S/N: ").upper()
        if condicion == "S":
            bandera = False

    bandera = True
    while bandera:
        altura = input("Dime tu altura (en centímetros): ")
        alt = float(altura)/100
        print(alt," m. ¿Es correcto?")
        condicion = input("S/N: ").upper()
        if condicion == "S":
            bandera = False
    imc = round(float(peso) / (alt**2),2)
    if imc <= 15.99 :
        print ("Delgadez severa")
    elif imc <= 16.99 :
        print ("Delgadez moderada")
    elif imc <= 18.49:
        print ("Delgadez leve")
    elif imc <= 24.99 :
        print ("Normal")
    elif imc <= 29.99:
        print ("Sobrepeso")
    elif imc <= 34.99:
        print ("obesidad leve")
    elif imc <= 39.00:
        print ("obesidad media")
    elif imc >= 40.00:
        print ("obesidad morbida")

else:
    print("Lo siento. Eres menor de edad.")    



