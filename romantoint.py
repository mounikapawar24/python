def romanToInt(s):
    translations = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    number = 0
    prev_value = 0
    for char in reversed(s):
        value = translations[char]
        if value < prev_value:
            number -= value
        else:
            number += value
        prev_value = value
    return number
s = input("Enter Roman numeral: ")
print(romanToInt(s))
