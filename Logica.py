#un cajero automatico

usuario = list()

usuario.append("Linda Aleman")
usuario.append("12345")
usuario.append(1000)

recibo = list()
recibo.append(["123", 600])
recibo.append(["124", 845])
recibo.append(["125", 67])
recibo.append(["126", 500])
recibo.append(["127", 100])
recibo.append(["128", 1000])

acciones = list()
acciones.append("Depositar")
acciones.append("Pago de recibo")
acciones.append("Retirar")



usuario2 = list()
usuario2.append("Elida")
usuario2.append("1234")
usuario2.append(1500)

def registrar ():
    usuarioRegistrado = list()
    usuarioC = input ("Ingrese su nombre:")
    usuarioRegistrado = input("Ingrese su password:")

    if usuarioC == usuario[0] and usuarioRegistrado == usuario[1]:
        print("Bienvenido al cajero automatico")
    
    else:
        print("usuario o contraseña incorrecta")
        return registrar()