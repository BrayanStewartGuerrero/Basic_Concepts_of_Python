product = {
    "Name":"book",
    "Quantity":3
    "Price":4.99
}

person = {
    "firstName":"Ryan",
    "lastName":"Ray"
}

print(type(person))

#Valores de las claves
print(person.keys())

#Valores de los items
print(person.items())

person.clear()
print(person)

products = {
    {"name":'book', "price":10.99}
    {"name":'laptop', "prince":9.87}
}