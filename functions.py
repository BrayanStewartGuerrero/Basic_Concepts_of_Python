print("hello world")

x = 10
dir(x)

type(12)

#Creando una funcion
def hello(name = "person"):
    print("Hello " + name)

hello("Ryan")

#Funcion para sumar
def sumar(n1,n2):
    return n1 + n2

print(sumar(20,30))

#Funcion escrita en una sola linea de codigo
add = lambda n1, n2: n1 + n2