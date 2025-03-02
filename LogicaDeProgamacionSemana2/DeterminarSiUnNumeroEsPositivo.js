let numero = parseFloat(promt("Ingrese un numero:"));
if (numero > 0 ) {
    console.log(`${numero} es positivo`);
} else if (numero < 0) {
    console.log(`${numero} es negativo`);
} else {
    console.log ("El numero es cero");
}