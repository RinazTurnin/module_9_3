first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (True if len(first[i]) == len(second[i]) else False for i in range(0, len(first)))
print(list(second_result))