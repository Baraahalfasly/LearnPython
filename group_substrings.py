def collect(word, size):
    return [word[i:i+size] for i in range(0, len(word), size)]

# Test cases
print(collect("intercontinentalisationalism", 6))  
# ➞ ["ationa", "interc", "ntalis", "ontine"]

print(collect("strengths", 3))  
# ➞ ["eng", "str", "ths"]

print(collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15))  
# ➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]
