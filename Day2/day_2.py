"""
Modulo correspondiente al dia 2:  if , else, elif (no es la novela)
"""

#Al parecer los condicionales son como en la mayoria de los lenguajes

#a == b
#a != b
#a < b
#a <= b
#a > b
#a >= b

#luego tenemos el if 

a = 33
b = 200
if b > a:
    print("b is greather than a")

#los if funcionan con identacion , sino se rompe el if y tira error
# al PARECER hay una palabra reservada que sirve para equiparar al else-if , que se llama elif

a = 33
b = 33
if b > a:
    print("b is greather than a ")
elif a == b:
    print("a and b are equals")

#luego tenemos el else que serviria como bifurcador de decisiones
#se puede usar elif como intermedio para finalizar con un else, asumo que se pueden usar varios elif

a = 200
b = 33

if b > a:
    print("b is greather than a ")
elif a == b:
    print("a and b are equals")
elif b == a:
    print("b and a are equals") #mi teoria era cierta 
else:
    print("a is greather than b ")

#luego tenemos el condicional clasico if - else

a = 200
b = 33
if b > a:
    print ("b is greather than a")
else:
    print("b is not greather than a")

#tambien puedo hacer la version "inline", aunque no le gusta mucho al compilador al parecer

if a > b: print("a is greather than b")

#tambien tenemos la version inline de if - else, aunque TAMPOCO LE GUSTA

a = 2
b = 320
print("A") if a > b else print("B")

#tambien existen los ternarios, pero oh sorpresa menos le van a gustar
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#luego pasamos a la palabra reservada "and" seria el equivalente a "&&"

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

#la palabra reservada "or" seria equivalente a "||" 
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

#tenemos el "not" que seria el equivalente a "!"

a = 33
b = 200
if not a > b:  #este no es el mejor ejemplo porque esto podria cambiarse por "<="
    print ("a is NOT greather than b")

#pasamos a los if anidados
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20.")

#la palabra reservada "pass" se usa cuando se tiene un if vacio, 
# y se quiere poner algo nulo, en java lo mas cercano seria un try - catch

a = 33
b = 200

if b > a:
    pass

#vamos a hacer un ejercio "Calculadora de calificaciones"
calificacion = int(input("ingresa tu calificacion de (0-100) : "))
if calificacion >= 90 and calificacion <= 100:  # esto puede escribirse asi tambien if 90 <= calificacion <= 100:
    letra ="A"
elif 80 <= calificacion < 90: # se ve rari , pero al parecer es menos boilerplate
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
elif 0 <= calificacion < 60:
    letra = "F"
else:
    letra =  "Calificacion no valida"

#ahora imprimo con formato , al parece el formato me permite concatenar la variable

print (f"Tu calificacion es : {letra}")

#si efectivamente la f, es formated strings literals, conocida como "f-strings" que justamente nos permite hacer esto