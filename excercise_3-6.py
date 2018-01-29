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

print("Hello " +names[0]+". I would like to invite you to dinner.")
print("Hello " +names[1]+". I would like to invite you to dinner.")
print("Hello " +names[2]+". I would like to invite you to dinner.")
print("Hello " +names[3]+". I would like to invite you to dinner.")
print("Hello " +names[4]+". I would like to invite you to dinner.")
print("Hello " +names[5]+". I would like to invite you to dinner.")

print("\nI am inviting " + str(len(names))+ " people to dinner.")
