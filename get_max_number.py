numbers = (5, 7, 9, 65, 4, 8, 3, 2, 1)

def largest_num(numbers):
    largest = 0
    for i in numbers:
        if i > largest:
            largest = i
    return largest

largest = largest_num(numbers)
print("The largest number is:", largest)
