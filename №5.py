#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
txt = input("Введите текст через пробел: ")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {"".join(lst)}')
#Создайте программу для игры в ""Крестики-нолики"".
maps = [1,2,3
        4,5,6
        7,8,9]
victories = [[0,1,2]
             [3,4,5]
             [6,7,8]
             [0,3,6]
             [1,4,7]
             [2,5,8]
             [0,4,8]
             [2,4,6]]
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])

    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])

    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])

def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

def get_result():
    win = " "
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X"
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O"
            win = "O"
    return win

def check_line(sum_O, sum_X):
    step = ""
    for line in victories:
        o = 0
        x = 0

        for j in range(0,3):
            if maps[line[j]] == "O":
                o = o +1
            if maps[line[j]] == "X":
                x = x +1
        if o == sum_O and x == sum_X
            for j in range(0,3):
                if maps [line[j]] != "O" and maps[line[j]] != "X"
                    step = maps[line[j]]
    return step

def AI():
    step= ""
    step = check_line(2,0)
    if step == "":
        step = check_line(0,2)
    if step == "":
        step=check_line(1,0)
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1
    return step

game_over = False
human = True
while game_over == False:
    print_maps()
    if human == True:
        symbol = "X"
        step = int(input("Ваш ход: "))
    else:
        print("AI делает ход: ")
        step = AI()
    if step != "":
        step_maps(step,symbol)
        win = get_result()
        if win != ""
            game_over = True
        else:
            game_over = False
    else:
        print("Ничья")
        game_over = True
        win = "0_0"
    human = not(human)

print_maps()
print("Победил", win)


#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def  encode(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding

if __name__ == '__main__':
    s = 'ABBSCCCD'
    print(encode(s))