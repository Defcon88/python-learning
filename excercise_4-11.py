pizzas = ["Peperoni", "Supreme", "Meat Lovers"]
friend_pizzas=pizzas[:]

for pizza in pizzas: 
	print("I love "+pizza+" pizza.")

print("\nFuuuuuck I love Pizza!!!!!\n")

pizzas.append("Hawaiian")
friend_pizzas.append("Sausage")

print("My pizzas:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's pizzas:")
for pizza in friend_pizzas:
	print(pizza)
