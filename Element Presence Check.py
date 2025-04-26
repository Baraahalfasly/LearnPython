x = [17,7,9,12,6,4,5]

y = [17,12,7]

all_found = True

for num in y:
    if num not in x:
        all_found = False
        break  

if all_found:
    print("True")
else:
      print("False")

