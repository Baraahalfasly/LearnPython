def stutter(word):
    first_two = word[:2]
    return f"{first_two}...{first_two}...{word}?"


print(stutter("incredible"))

print(stutter("enthusiastic"))

print(stutter("outstanding"))
