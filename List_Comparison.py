x = [2, 7, 5, 10, 3]
y = [4, 3, 9, 8, 1]

m = []

for xi , yi in zip (x,y):
    if xi % 2 == 0 and yi % 2 == 0:
        m.append(xi*yi)
    
    else:
        m.append(xi+yi)
print(m)
