print("bienvenidos dinos los precio, ganancia y impuesto")
#escribir leer
precio = input("ingrese el precio:")
precio = float(precio)

ganancia = input("ingrese el ganancia:")
ganancia = float(ganancia)

impuesto = input ("ingrese el impuesto:")
impuesto = float(impuesto)

#funcion nombre de l variable ()
def calcularimpuesto(impuesto, precio): 
    return impuesto * precio

def calcularganancia(ganancia, precio): 
    return ganancia * precio

def calcularpreciofinal(precio, impuesto, ganancia):
    precio1 = calcularganancia(ganancia, precio) + precio
    impuestoventa = calcularimpuesto(impuesto, precio1)
    return precio1 + impuestoventa

print(calcularpreciofinal(precio, impuesto, ganancia))