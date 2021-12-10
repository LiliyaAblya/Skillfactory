table=[1,2,3,4,5,6,7,8,9]
def filed(table):
    for i in range(3):
        print ('|', table[0+i*3], '|', table[1+i*3],'|', table[2+i*3],'|')
def turn(token):
        stroke=int(input('Сделайте свой ход: '))
        if 1<=stroke<=9 and type(stroke)==int:
            table[stroke -1]=token
        else:
            print('Некорректный ввод!')
def check(table):
    win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win:
        if table[each[0]] == table[each[1]] == table[each[2]]:
            return table[each[0]]
    return False
def play(table):
    counter = 0
    win = False
    while not win:
        filed(table)
        if counter % 2 == 0:
            turn("X")
        else:
            turn("O")
        counter += 1
        if counter > 4:
            player = check(table)
            if player:
                print (player, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    filed(table)
play(table)
