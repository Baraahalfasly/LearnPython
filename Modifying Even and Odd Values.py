x = [2, 10, 3, 6, 7]

y = []

for i in x:
    if i % 2 == 0:
        y.append(i + 2)
    else:
        y.append(i - 1)
print(y)
