x = input ("Enter a string: ")
found = False
for i in x :
    if i in "123456789":
        found = True
        break
print(found)
