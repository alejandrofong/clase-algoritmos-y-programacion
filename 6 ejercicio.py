#este progrma va a tener como finalidad mezclar varios elementos que pueda solicitar el usuario o vamos a colocar diferentes metodos para poder realizar actividades simples o secuencias 
#del mismo modo permitira realizar salidas de informacion sujetas a condiciones logicas 

print("-------------------------------- inicio de programa --------------------------------")
EDAD1= int (input(" ¿cual es su edad? ")) 
if EDAD1 < 18:
    print("eres menor de edad")
else:
    print("eres mayor de edad")

print("-------------------------------- modulo de seguridad --------------------------------")

print(" su contraseña ya se envio a su correo ")
clave_mayor_de_edad = "contraseña"
contraseña = input("ingrese su contraseña que fue enviada a su correo ")
if clave_mayor_de_edad == contraseña.lower ():
    print("Contraseña correcta")
else:
    print ("Contraseña incorrecta")

print("-------------------------------- modulo de interaccion --------------------------------")
print (" escriba una frase o plabra para seguir adelante en la autentificacion")

frase = input (" introduce una frase ")
# si se desea remplazar ka contraseña, solicite al usuario escribir diferentes letras o numeros la nueva contraseña o simplemente solicite un parametro de validacion
vocal = input ("introduzca una vocal en minusculas ")
print (frase.replace(vocal, vocal.upper()))

print (" usted a completado los tres modulos de autentificacion / puede seguir adelante con el pago")

#-------------------------------ejercicio practico---------------------------------
print("-------------------------------- inicio de programa --------------------------------")
print(" bienvenido a la red de inteligencia del gobierno")
EDAD2= int (input(" ¿cual es su edad?")) 
if EDAD2 < 18:
    print("eres menor de edad")
else:
    print("eres mayor de edad")

print("-------------------------------- modulo de seguridad --------------------------------")

print(" su contraseña ya se envio a su correo ")
clave_mayor_de_edad = "contraseña"
contraseña = input("ingrese su contraseña que fue enviada a su correo ")
if clave_mayor_de_edad == contraseña.lower ():
    print("Contraseña correcta")
else:
    print ("Contraseña incorrecta")

print("-------------------------------- modulo de interaccion --------------------------------")
print (" escriba una frase o plabra para seguir adelante en la autentificacion")

frase = input (" introduce una frase ")
# si se desea remplazar ka contraseña, solicite al usuario escribir diferentes letras o numeros la nueva contraseña o simplemente solicite un parametro de validacion
vocal = input ("introduzca una vocal en minusculas ")
letra = input ("introduzaca una letra en minusculas ")
frase2 = input ("introduzca la frase en minusculas ")
print (frase.replace(vocal, vocal.upper()))

print (" usted a completado los tres modulos de autentificacion / puede seguir adelante con el pago")
