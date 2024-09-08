a = [10]

E = 0
O = 0

for i in a:
    if i % 2 == 0:
       E += 1 
    else:
       O += 1

print("Number of even numbers: ",E)
print("Number of odd numbers: ", O)
