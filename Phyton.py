# en este apartado estamos definiendo variables
var1="xaloc"   #variable de tipo string y esta entre comillas
var2=4      #variable con valor entero
var3=5        #variable de valor entero
var4=1.8     #variable de tipo float o decimal

# este es un ejemplo de como no tengo que definir una variable var 3= "no es correcto"

print("este mensaje se visualizara por pantalla")

resultado=var2+var3

print(resultado)

#print deja ver en pantalla contenido que tu quieras
#A continuación hacemos uso de la función input, que permite capturar un valor introducido por el usuario
#via teclado.
#Recuerda que en la instrucción input podemos introducir un mensaje informativo entre comillas.
nombre=input("introduce tu dombre")
apellido1=input("introduce tu primer apellido")
apellido2=input("introduce tu segundo apellido")

nombre_completo= nombre + " " + apellido1 + " " + apellido2
print(nombre_completo)

suma= var2 + var3
print(f"la suma de var2 y var3 es igual a", suma)
resta=var2 - var3
print(f"la resta de var2 y var3 es igual a", resta)
multiplicacion=var2 * var3
print(f"la multiplicacion de var2 y var3 es igual a", multiplicacion)
division=var2 / var3
print(f"la division de var2 y var3 es igual a", division)
division_entera=var2 // var3
print(f"la division entera de var2 y var3 es igual a", division_entera)
modulo=var2 % var3
print(f"el modulo de var2 y var3 es igual a", modulo)
potencia=var2 ** var3
print(f"la potencia de var2 y var3 es igual a", potencia)
