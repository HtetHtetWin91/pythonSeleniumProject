with open("pythonBasics/htet.txt", "r") as reader:
    content = reader.readlines()
    contentReversed = reversed(content)
    with open("pythonBasics/htet.txt", "w") as writer:
        for line in contentReversed:
            writer.write(line)

with open("pythonBasics/htet.txt", "r") as reader:
    content = reader.readlines()
    for line in content:
        print(line)