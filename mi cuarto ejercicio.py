#vamos a crear un codigo que realice por pantalla un calculo de variable, que nos permita sumar restar y hacer operaciones para mostrar la final un resultado de cada operacion y a su vez crear una tabla de la verdad y cada una de las operacion usandop "bool o usando and y or"
print ("no se hizo con chat gpt") 
a= int(input("deme un numero en pantalla  "))
b= int(input("deme un numero mayor que el anteriror  "))
a= str(a)
b= str(b)
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a%b)
print ("la tabla de la verdad todo lo relacionado con and o y ")
#print ((str(a==a)) + " and " + str(a==a) + " ===> " + str (a==a))
#print ((str(a==a)) + " and " + str(a==b) + " ===> " + str (a==b))
#print ((str(a==b)) + " and " + str(b==b) + " ===> " + str (a==a))
#print ((str(a==b)) + " and " + str(b==a) + " ===> " + str (a==a))

print (bool(a==b))
print (bool(a==a))
print (bool(b==a))
print (bool(b==b))