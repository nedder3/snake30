"""
Modulo correspondiente al dia 4:  funciones
"""
#se usa la palabra reservada def

def my_function():
    print("hola desde una funcion")

my_function() #se llama de esta manera

#si quiero pasarle argumentos lo hago de esta manera

# la sobrecarga brilla por su ausencia
def my_functionn(fname):
    print(fname +" Rfsnes")
    
my_functionn("emi")
my_functionn("Tobi")
my_functionn("lars")

#se pueden crear con varios argumentos

def my_function3(fname, lname):
    print(fname + " " + lname)

my_function3("Emil", "Refsnes")

# lo que se puede hacer es usar '*' para n cantidad de argumentos

def my_function4(*kids):
  print("The youngest child is " + kids[2])

my_function4("Emil", "Tobias", "Linus")

#se puede usar una expresion 'clave-valor' para la sintaxis tambien

def my_function5(child3, child2, child1):
  print("The youngest child is " + child3)

my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#otra feature interesante es la de las 'kwargs' , sirve para cuando tenemos un diccionario de argumentos

def my_function6(**kid):
  print("His last name is " + kid["lname"])

my_function6(fname = "Tobias", lname = "Refsnes")

#tenemos la opcion de poner un parametro por default 

def my_function7(country = "Norway"):
  print("I am from " + country)

my_function7("Sweden")
my_function7("India")
my_function7()
my_function7("Brazil")

#se puede pasar una lista como argumento

def my_function8(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function8(fruits)

#podemos retornar valores de la siguiente manera
def my_function9(x):
  return 5 * x

print(my_function9(3))
print(my_function9(5))
print(my_function9(9))

#podemos usar 'pass' porque las funciones no deben estar vacias

def myfunction10():
  pass

#se pueden usar argumentos posicionales tambien 

def my_function11(x, /):
  print(x)

my_function11(3)

#si no usamos ,/ , la funcion esperará el argumento de la siguente manera
def my_function12(x):
  print(x)

my_function12(x = 3) #si le agrego ,/ estando de esta manera arroja error

#se pueden usar argumentos del tipo keyword
#sirve para especificar que solo puede tener un argumento keyword, hay que agregar *, antes de los argumentos

def my_function13(*, x):
  print(x)

my_function13(x = 3)

#ahora se puede combinar los posicionales con los keywoard

def my_function14(a, b, /, *, c, d):
  print(a + b + c + d)

my_function14(5, 6, c = 7, d = 8)