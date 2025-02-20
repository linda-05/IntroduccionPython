
print("bienvenidos dinos los precio, ganacia y impuesto")
#escribir leer
precio = input("ingrese el precio:")
precio = float(Precio)

ganancia = input("ingrese el ganacia:")
ganancia = float(ganacia)

impuesto = input ("ingrese el impuesto:")
impuesto = float(impuesto)

#funcion nombre de l variable ()
def calcularimpuesto(impuesto, precio): 
    return impuesto * precio

def calcularganacia(ganacia, precio): 
    return ganacia * precio

def calcularpreciofinal(precio, impuesto):
    precio1 = calcularganacia(ganacia, precio) + precio
    impuestventa = calcularimpuesto(impuesto, precio1)
    return precio1 + impuestventa

print(calcularpreciofinal(precio, impuesto, ganancia))