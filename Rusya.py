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


#moe, staroe
# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')


# letters, numbers = [], []

# for i in data_tuple:
#     letters.append(i) if type(i) == str else numbers.append(i)
# letters = [str(i) for i in letters[::-1]]
# letters[0], letters[1], letters[3], letters[4], letters[5], letters[6], letters[7] = 'C', 'h', 'T', 'e', 'k', 'e', 'g'
# del numbers[0]
# letters.append(numbers.pop(0))
# numbers.insert(1, 2)
# numbers = [int(i) for i in numbers[::-1]]
# numbers = [int(i) ** 2 for i in numbers]
# letters = tuple(letters)
# numbers = tuple(numbers)
# print(letters)
# print(numbers)
