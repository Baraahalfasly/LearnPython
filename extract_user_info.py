import re

def parse_code(text):
    # Regular expression to match the pattern
    pattern = r"([a-zA-Z]+)0+([a-zA-Z]+)0+(\d+)"
    match = re.match(pattern, text)
    if match:
        return {
            "first_name": match.group(1),
            "last_name": match.group(2),
            "id": match.group(3)
        }
    return "Invalid format"

# Test cases
print(parse_code("John000Doe000123"))      # ➞ {"first_name": "John", "last_name": "Doe", "id": "123"}
print(parse_code("michael0smith004331"))   # ➞ {"first_name": "michael", "last_name": "smith", "id": "4331"}
print(parse_code("Thomas00LEE0000043"))    # ➞ {"first_name": "Thomas", "last_name": "LEE", "id": "43"}
