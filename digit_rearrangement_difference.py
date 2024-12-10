def rearranged_difference(number):
    # Convert the number to a list of digits, then sort for largest and smallest numbers
    digits = list(str(number))
    largest = int("".join(sorted(digits, reverse=True)))  # Largest number by sorting in descending order
    smallest = int("".join(sorted(digits)))  # Smallest number by sorting in ascending order
    return largest - smallest  # Compute the difference

# Examples
print(rearranged_difference(972882))  # ➞ 760833
print(rearranged_difference(3320707))  # ➞ 7709823
print(rearranged_difference(90010))  # ➞ 90981
