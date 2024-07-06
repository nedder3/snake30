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