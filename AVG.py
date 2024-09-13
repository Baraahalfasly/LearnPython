x = [30, 20, 10, 40, 50]

def getAVG(x):
    z = 0
    for i in x:
           z = z + i
    N = len(x)
    M = z/N 
    return M

y = getAVG(x)

for i in x :
   if i > y:
     
     print(i)

