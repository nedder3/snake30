"""
Este módulo imprime un mensaje en consola.
"""

#imprimir un mensaje en consola

print ("Hello Cat")

#en caso de tener un condicional se usa identación

if 5 > 2 :
    print("Five is greater than two!")

#un condicional doble se veria asi, simpre salto de linea al final 

if 3 > 2 :
    print("Three is greather than two!")

if 2 < 3 :
    print("Two is greather than 3")

#una variable se declararia asi, si fueran constantes deberian ser mayusculas
X = 5

Y ="Hello,world"

print(X)
print(Y)

#no hace falta definir los tipos de datos al final pueden ir cambiando todo el tiempo
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#si quiero especificar el tipo de dato debo casterlo

x = str(3) # x sera '3'
y = int(3) # y sera  3
z = float(3) #z sera 3.0

#si quiero obtener el tipo de dato , se pueden usar comilla simples o dobles

x = 5
y = "Jhon"
print (type(x))
print (type(y))

#los nombres de variables son case sensitive

a = 4
A = "Sally"

#existe la asignación multiple

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#se puede asignar el valor a muchas variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

#si quiero imprimir por consola la mejor manera de hacerlo es asi

x = 5
y = "John"
print(x, y)

#si quiero usar una variable global usar la palabra reservada 'global'
#si no solo basta declararla arriba e ir declarando funciones

#luego tenemos diferentes tipos de datos
x = True
y = bool(5) #cualquier numero distinto de 0 es True
