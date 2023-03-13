# 4. Структуры данных: списки, срезы, кортежи.
# list - списok
# tuple - кортеж
# print(type(objects))
# [start:stop:step]
# print(objects[2])
# print(objects[3:6])
# print(7 if 4 > 5 else 10)
# new = [i*2 for i in objects if i > 2]

# students_count = int(input('how many students? '))
#
# data = [int(input(f'rate for student: {i}')) \
#         for i in range(1, students_count + 1)]
#
# answer = input(f'{data} \n all right? ')
# if answer == 'yes':
#     print(sum(data) / len(data))
# else:
#     while True:
#         print(data)
#         index_rate = int(input('choose index of rate: '))
#         if index_rate > len(data):
#             break
#         data[index_rate] = int(input('enter new rate: '))
#
# print(data)


week_days = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

data = []

for day in week_days:
    expense = int(input(f'enter expense for "{day}": '))
    data.append(expense)

min_value = min(data)
data[data.index(min_value)] = 500

print(f'average: {sum(data) / len(week_days)}')


# objects = tuple('1')
# objects += (1, 2, 3)
#
# print(objects)
# print(type(objects))

# a = 5
# objects = [11, 2, 1.5, 2.9, 3.4, 1.6]
# print(new)

# new = list('python')
# new = list(range(1, 6))
# print(new)

# new_copy = objects.copy()

# print(id(objects))
# print(id(new_copy))

# new_copy[0] = 33

# print(objects)
# print(new_copy)
# print(objects == new_copy)
# print(objects is new_copy)


# objects.sort()
# objects.reverse()
# print(objects.count('hello'))
# print(len(objects))
# print(objects[::-1])

'''delete'''
# deleted = objects.pop(-2)
# print(objects.pop(1))
# print(objects)
# objects.remove('python')
# del objects[-1]
# del objects[4:]
# print(deleted)

'''edit'''
# objects[0], objects[2] = objects[2], objects[0]
# objects[3] = 'goodbay'
# objects[objects.index(2.9)] += 1
# objects[4:] = [55, 63]
# objects.insert(3, ['python']*4)


'''add'''
# objects.append('anna')
# objects.insert(2, 250)
# objects.extend(new)
# objects += new
