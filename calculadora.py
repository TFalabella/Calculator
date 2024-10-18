# Calculadora. TP Final Mes 1.

def sumar (a, b):
    return a + b

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero."

while True:
    print ("\n--- Calculadora ---")
    print ("1. Sumar")
    print ("2. Restar")
    print ("3. Multiplicar")
    print ("4. Dividir")
    print ("5. Salir")

    opcion = input ("Selecciona una opción (1-5:)")

    if opcion == '5':
        print ("Saliendo...")
        break

    num1 = float (input("Introduce el primer número: "))
    num2 = float (input("Introduce el segundo número: "))

    if opcion == '1':
        print ("Resultado:", sumar(num1, num2))
    elif opcion == '2':
        print ("Resultado:", restar(num1, num2))
    elif opcion == '3':
        print ("Resultado:", multiplicar(num1, num2))
    elif opcion == '4':
        print ("Resultado:", dividir(num1, num2))
    else:
        print ("Opción no válida.")

