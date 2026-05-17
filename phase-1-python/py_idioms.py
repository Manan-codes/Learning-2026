words = ["hello", "world", "python", "git"]

List Comprehensions
uppercased = [word.upper() for word in words if len(word) > 4]


Enumerate
for i, word in enumerate(words, start=1):
    print(f"{i} {word}")


phases = ["Setup", "Python", "Data", "ML", "Ship"]
weeks = [0, 2, 5, 10, 14]

#zip
for week, phase in zip(weeks, phases):
    print(f"{phase} starts at week {week}")


#Unpacking 
first, *rest = [1, 2, 3, 4, 5]
print(f"First: {first}\nRest: {rest}")

first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}\nMiddle: {middle}\nLast: {last}")

#Swapping doesnt need temp
# a, b = b, a


#f-strings
price = 4.50
quantity = 3
print(f"Total: €{price*quantity:.2f}")
