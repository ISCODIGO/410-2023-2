print("break")
i = 10
while i:
    i -= 1
    if i == 5:
        continue
    print(i)

print("continue")
i = 10
while i:
    i -= 1
    if i == 5:
        break
    print(i)