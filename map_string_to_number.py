mapping = {
    "write": 0,
    "your": 1,
    "strings": 2,
    "here": 50
}

def custom_eval(word):
    return mapping.get(word, "Invalid Input")  # Default to "Invalid Input" if the word is not found

zero = "write"
one = "your"
two = "strings"
fifty = "here"

print(custom_eval(zero))  # 0
print(custom_eval(one))   # 1
print(custom_eval(two))   # 2
print(custom_eval(fifty)) # 50
