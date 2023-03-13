data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters, numbers = [], []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
letters.append(numbers[1])
letters.reverse()
letters.remove("g")
letters.remove("C")
letters.insert(1, "G")
letters.insert(7, "c")
letters = tuple(letters)
print(letters)

del numbers[:2]
numbers.insert(1, 2)
numbers.sort()
numbers = [i ** 2 for i in numbers]
numbers = tuple(numbers)
print(numbers)
