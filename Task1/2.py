#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

number_1 = [int(x) for x in input().split(' ')]
number_2 = number_1[::-1]
middle = len(number_1) / 2 if int(len(number_1) / 2) == len(number_1) / 2 else int(len(number_1) / 2) + 1
result = list(map(lambda x: x[0] * x[1], zip(number_1[:middle], number_2[:middle])))
print(result)