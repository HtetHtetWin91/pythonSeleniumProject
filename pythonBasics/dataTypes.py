print("Helloa, World!")
a = 3
print(a)

b, c, d = 5,"Htet" , "Htet"


print(b, c, d)

print("Value is " + d)

print("{0} said {1}".format("Htet", "I love you"))

print(type(b), type(c))

print(b,"hello"+d)

values = [1, "Htet", "Birth", "love",14]
print (values[2])
print (values[1:4])
print (values[-1])
values.insert(2, "miss")
values.append("End...")
print(values)

values[2] = "HaHa"
print(values)

del values[2]
print(values)

valTuple = (1, "Htet", "Birth", "love",14)

print(valTuple)

valDict = {"name":"Htet", "age":14, "birth":"Birth", "love":"love"}
print(valDict["age"])

valDictDynamic = {}
valDictDynamic["name"] = "Htet"
valDictDynamic["age"] = 14
valDictDynamic["passport"] = "MH003535"

print(valDictDynamic)