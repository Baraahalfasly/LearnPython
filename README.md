# LearnPython

1- My first python code (hello world)

2- (Create for_loop.py)

for i in range(10):: Starts a loop where i takes values from 0 to 9 (which are 10 numbers).
print(i): Prints the current value of i in each iteration

It will print the numbers from 0 to 9, each on a separate line.



3- This is my Third python code. 

a= [10]
E = 0
O = 0
for i in a:
    if i % 2 == 0:
       E += 1 
    else:
       O += 1
print("Number of even numbers: ",E)
print("Number of odd numbers: ", O)

"This code counts the even and odd numbers in list a. If an element is even, the variable E is incremented by 1, and if it is odd, the variable O is incremented by 1. At the end, it prints the count of even and odd numbers"

4-This is my fourth python code.

name = input("Enter your name: ")
print("Hello", name)
name[0]
if name[0] == "B":
  print("the first letter is B")
        
elif name[0] == "A":
  print("the first letter is A")     
else:
  print("the first letter is not B"

This code does the following:

Asking for the name: The program starts by asking the user to input their name with the line name = input("Enter your name: ").

Greeting: After entering the name, the program prints a greeting message using print("Hello", name).

Checking the first letter: The program checks the first letter of the name using name[0].

First condition: If the first letter is "B", the program prints "the first letter is B".

Second condition: If the first letter is "A", the program prints "the first letter is A".

Default condition: If the first letter is neither "B" nor "A", the program prints "the first letter is not B".

In summary, the code greets the user and checks the first letter of their name to determine whether it is "A", "B", or something else.

5- This is my fifth python code.

x = 10
def checkAge(x):
    if x < 15:
        print("child")
    elif x < 25 and x > 10:
        print("yowng")
    else:
        print("woman")
 
checkAge(x)

1.Variable x: It is assigned the value 10.

2.Function checkAge: It takes a value (age) and determines the age category:

   If the age is less than 15, it prints "child."
   If the age is between 10 and 25 (excluding 10), it prints "young."
   If the age is 25 or older, it prints "woman."
3.When calling the function with checkAge(x):

The value of x is 10, so it prints "child."
In summary, the code determines the age category based on the input value.

