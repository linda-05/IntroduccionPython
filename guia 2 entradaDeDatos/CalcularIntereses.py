import math
def calcularIntereses(precio, interes):
    return precio * interes

def calcularPrecio(precio, ganancia):
    return precio + (ganancia * precio)

def precioVenta(precio, interes, ganancia):
    total = calcularPrecio(precio,ganancia)
    interes = calcularIntereses (total, interes)
    return total + interes

interes = float(input("Ingrese el interes:"))
precio = float(input("Ingrese el precio:"))
ganancia = float(input("Ingrese la ganancia:"))

print(precioVenta(precio, interes, ganancia))


