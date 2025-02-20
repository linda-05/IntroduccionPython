def calculadora ():
    print("Selecciones una accion")
    print("Selecciones una accion")

    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. salir")

    opcion = input("ingrese la opcion : ")

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Ingrese el primer numero:"))
        num2 = float(input("Ingrese el segundo numero:"))
        