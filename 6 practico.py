#-------------------------------ejercicio practico---------------------------------
print("-------------------------------- inicio de registro --------------------------------")
print(" bienvenido a la red de inteligencia del gobierno")
input(" registre su nombre: ")
input(" registre su apellido: ")
print("-------------------------------- datos personales --------------------------------")
EDAD2= int (input(" ¿cual es su edad?: ")) 
if EDAD2 < 18:
    print("eres menor de edad")
else:
    print("eres mayor de edad")
input("ingrese su fecha de nacimiento(D/M/A): ")
pais= str(input("¿ en que pais nacio?: "))
pais_de_origen = "colombia"
if pais_de_origen == pais.lower():
    print("eres colombiano")
else:
    print("eres extrangero")


print("-------------------------------- modulo de seguridad --------------------------------")
input("ingrese su correo: ")
print(" en unos momentos su contraseña ya se enviara a su correo ")
clave_mayor_de_edad = "alinares2510"
contraseña = input("ingrese su contraseña que fue enviada a su correo ")
if clave_mayor_de_edad == contraseña.lower ():
    print("Contraseña correcta")
else:
    print ("Contraseña incorrecta")

print("-------------------------------- modulo de interaccion --------------------------------")
print (" escriba una frase o palabra para seguir adelante en la autentificacion")

frase = input (" introduce una frase ")
# si se desea remplazar ka contraseña, solicite al usuario escribir diferentes letras o numeros la nueva contraseña o simplemente solicite un parametro de validacion
vocal = input ("introduzca una vocal en minusculas ")
letra = input ("introduzaca una letra en minusculas ")
frase2 = input ("introduzca la frase en minusculas ")
print (frase.replace(vocal, vocal.upper()))

print (" usted a completado los tres modulos de autentificacion / puede seguir adelante con el pago")