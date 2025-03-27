str = "Welcome From Python"
str1 = "Welcome From Python,My Email is htethtetwin.minkin@gmail.com"
str3 = "Welcome From Java "

print(str[0:7])  # Welcome

print(str+str1)

splitString = str1.split(",")
print(splitString[0])

print(str in splitString[0])

print(str3.strip())

print(str3.replace("Java", "Python"))

print(str3.find("Java"))


