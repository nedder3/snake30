"""
Modulo correspondiente al dia 3: bucles for , while y listas .
"""
#En python las listas son similares a otros lenguajes
mylist = ["apple","banana","cherry"]

# hay otros 3 tipos que son las tuplas, los sets y diccionarios

thislist =["apple","banana","cherry"]
print(thislist)

#las listas son ordenadas, mutables y admiten valores duplicados
#en python las listas empiezan en [0]
#al ser lista le afectan metodos como sort, append ,index,reverse, etc


thislist =["apple","banana","cherry","apple","cherry"]
print(thislist)

#puedo utilizar len() para saber cuantos elementos tiene la lista

thislist = ["apple","banana","cherry"]
print(len(thislist))

#las listas pueden ser de distintos tipo

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#una lista tambien puede tener distintos datos mixtos por ejemplo:

list1 = ["abc", 34, True, 40, "male"]

#para python las listas son definidas mediante un tipo


mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#tenemos contructores de list() por ejemplo

thislist= list(("apple","banana","cherry")) #se usa doble parentesis
print(thislist)

#luego veremos mas en profundidad list, tuplas, set y diccionarios


#En python hay 2 primitivas para loops que es el while y el for
#aca tambien hay que tener cuidado con el loop infinito 
# asi que poner siempre el incremento

i = 1
while i < 6:
    print(i)
    i += 1

#el while siempre requiere que la variable este inicializada/seteada

#por otro lado podemos usar un break para frenar si una condicion es verdadera por ej

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#por contraparte tenemos el 'continue' que sirve para frenar la iteracion y seguir en otro lado

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# en este caso el numero 3 no se imprimirá 

#tambien se puede anexar un 'else' para cuando la condicion ya no sea verdadera

i = 1
while i < 6:
    print (i)
    i += 1
else:
 print("i is no longer less than 6")

#ahora veremos los loops 'for', se puede iterar sobre items en una lista, tupla, set,etc

fruits =["apple","banana","cherry"]
for x in fruits:
    print(x)

#ahora loopearemos a traves de un string

for x in "banana" :
    print(x)

#como es un iterador tambien podemos usar 'break'

fruits = ["apple","banana","cherry"]
for x in fruits:
    print (x)
    if x == "banana":
        break

# en un caso similar podemos cortar el loop antes que x = banana

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#podemos usar continue tambien y saltearnos "banana"
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#tenemos una func 'range()' lo que hace es determinar distancia ej: 0 -6 . rango = 5

for x in range (6):
    print(x)

#podemos definir rangos tambien con parametro de inicio y finalizacion

for x in range(2,6):
    print(x)

#podemos añadir un parametro de incremento , como tercer parametro
#en este caso usamos el numero 3

for x in  range(2, 30, 3):
    print(x)

#tambien podemos usar un else en el loop

for x in range (6):
    print(x)
else:
    print("Finally finished")

#si hay un 'break' presente el bloque no será ejecutado
for x in range(6):
    if x == 3: break
    print(x)
else:
 print("Finally finished")


#tenemos loops anidados tambien . en este caso hara las 9 combinaciones posibles
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

#podemos usar 'pass" para usar bucles vacios sin que nos dé error

for x in [0,1,2]:
    pass

#Ejercicio: Suma de Números
#Objetivo: Escribir un programa que pida al usuario un número entero positivo
#n y calcule la suma de todos los números enteros desde 1 hasta
#n inclusive, utilizando tanto un bucle for como un bucle while
