# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
a = int(input("Введите число: "))
if 0 < a <= 5:
    print('Нет')
if 5 < a <= 7:
    print('Да')
else:
    print('Число вне 7 дней')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
x = int(input('input x: '))
y = int(input('input y: '))
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
n = int(input('input some: '))
if n < 1 or n > 4:
    print('Please, repeat the input')
elif n == 1:
    print('x > 0 and y > 0')
elif n == 2:
    print('x < 0 and y > 0')
elif n == 3:
    print('x < 0 and y < 0')
elif n == 4:
    print('x > 0 and y < 0')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
x = int(input('Введите координату по оси X- '))
y = int(input('Введите координату по оси Y- '))
if x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
else:
    print('Введите корректные координаты')