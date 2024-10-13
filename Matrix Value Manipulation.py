import numpy as np
x = np.array([[1,2,3,5,7,8],[3,5,6,8,4,9],[7,8,9,3,5,7]])

x[:3, ::2]

print(x[:3, ::-2])

x[0,0] = 3

print(x[0,3]) 
print(x[1,2])
print(x[2,1])

