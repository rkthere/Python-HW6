#Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
#Добавьте возможность использования скобок, меняющих приоритет операций.

s = input()
try:
    print(eval(s))
except:
    print('Вводите не так. Введите арифм.выражение')