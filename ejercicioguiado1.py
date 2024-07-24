#Diagrama de flujo
#Paso 1
#Realizar una tabla para desglosar el problema en tres partes:
#● datos de entrada
import math
#variables
numero1 = float(input("ingrese un numero del 1 al 100: \n>"))
numero2 = float(input("ingrese un numero del 1 al 100: \n>"))
#● proceso
suma = numero1 + numero2
suma = math.ceil(suma)
#● datos de salida
print(f"La suma de ambos numero es: {suma}")

