names = ['Brett', 'Lee', 'Dan']
print("Hello " +names[0]+". I would like to invite you to dinner.")
print("Hello " +names[1]+". I would like to invite you to dinner.")
print("Hello " +names[2]+". I would like to invite you to dinner.")

print("\nOh Shit!!! "+names[1]+" can't make it!")
names[1]= "Tasha"
print("\n")
print("Hello " +names[0]+". I would like to invite you to dinner.")
print("Hello " +names[1]+". I would like to invite you to dinner.")
print("Hello " +names[2]+". I would like to invite you to dinner.")

print("\nHoly Fuck!! I just got us a fucking huge table everyone!")

names.insert(0, "Eva")
names.insert(2, "Angela")
names.append("Nichole")

print("\n")

print("Hello " +names[0]+". I would like to invite you to dinner.")
print("Hello " +names[1]+". I would like to invite you to dinner.")
print("Hello " +names[2]+". I would like to invite you to dinner.")
print("Hello " +names[3]+". I would like to invite you to dinner.")
print("Hello " +names[4]+". I would like to invite you to dinner.")
print("Hello " +names[5]+". I would like to invite you to dinner.")

print("\nFML!! I'm sorry, I only have room for two people now")
print("\n")
print(names.pop(0)+" so sorry! We need to cancel tonight")
print(names.pop(0)+" so sorry! We need to cancel tonight")
print(names.pop(0)+" so sorry! We need to cancel tonight")
print(names.pop(0)+" so sorry! We need to cancel tonight")

print("\n")

print("Hello " +names[0]+". We're still down for dinner!")
print("Hello " +names[1]+". We're still down for dinner!")

names.remove("Dan")
print(names)
del names[:]
print(names)
