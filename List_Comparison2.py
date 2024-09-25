x = [3,10,5,7,8,3,11]
y = [1,8,9,11,4,8,4]
m = []

for xi, yi in zip(x, y):
    if xi % 2 == 0 and yi % 2 == 0:
        m.append(xi * yi)

    elif xi % 2 != 0 and yi % 2 != 0:
        m.append(xi + yi)
    else:

      if xi > yi:
         m.append(xi-yi)
      elif yi > xi:
         m.append(yi-xi)

print(m)
