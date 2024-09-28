x = "ab3y+fm5"
y = []
z = ""

for i in x:
    if i in "0123456789":
        y.append(int(i))
    elif i in ["+","-","*","/"]:
        z = i
if z == '+':
    print( y[0] + y[1])
elif z == '-':
    print( y[0] - y[1])
elif z == '*':
    print( y[0] * y[1])
else:
    print( y[0] / y[1])


