# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).
float_num = input('Введите число: ')
sum = 0
for i in float_num:
    if i != ',':
        sum += int(i)
print(sum)

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
n = int(input('ВВедите число N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial, end=' ')

# Реализуйте алгоритм перемешивания списка.
import random
list = ['Некий', 3.14, 'False', 'True']
random.shuffle(list)
print(list)