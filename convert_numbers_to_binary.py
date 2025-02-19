import re

def replace_nums(s):
    return re.sub(r'\d+', lambda x: bin(int(x.group()))[2:], s)

# Test cases
print(replace_nums("I have 2 sheep."))  # "I have 10 sheep."
print(replace_nums("My father was born in 1974.10.25."))  # "My father was born in 11110110110.1010.11001."
print(replace_nums("10hell76o4 boi"))  # "1010hell1001100o100 boi"
