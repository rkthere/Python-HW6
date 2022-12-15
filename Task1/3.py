#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

number = [round(float(x), 2) for x in input().split(' ')]
parts = [round((x - int(x)), 2) for x in number if x - int(x) != 0.0]
result = max(parts) - min(parts)
print(f"{result:.2f}")