file = open("pythonBasics/htet.txt")
print("All Content", file.read())
file.close()
print("###########################3")
file1 = open("pythonBasics/htet.txt")

line = file1.readline()
while line!="":
    print(line)
    line = file1.readline()
file1.close()

print("###########################3")
file2 = open("pythonBasics/htet.txt")
for lines in file2.readlines():
    print(lines)
file2.close()