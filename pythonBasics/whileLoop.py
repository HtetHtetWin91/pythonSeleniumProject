it = 4
while it < 10:
    print(it)
    it = it + 1
print("End of While Loop")

it = 5
while it < 11:
    print(it)
    it = it + 1
    if it == 8:
        continue
    if it == 10:
        break

print("End of While Loop")
