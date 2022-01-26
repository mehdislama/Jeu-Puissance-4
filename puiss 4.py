from random import randint
def display_board(board):
    print(' ' + ' | ' + '1 ' + ' | ' + '2 ' + ' | ' + '3 ' + ' | ' + '4 ' + ' | ' + '5 ' + ' | ' + '6 ' + ' | ' + '7 ' + ' | ')
    print('  ------------------------------------')
    print(' ' + ' | '+board[36] + ' | ' + board[37] + ' | ' + board[38] + ' | ' + board[39] + ' | ' + board[40] + ' | '+ board[41]+ ' | ' +board[42] + ' | ')
    print('  ------------------------------------')
    print(' '+  ' | ' +  board[29] + ' | ' + board[30]+ ' | '+ board[31]+ ' | ' + board[32] + ' | ' + board[33] + ' | ' + board[34] + ' | '+ board[35]+ ' | ')
    print('  ------------------------------------')
    print(' ' +  ' | ' + board[22] + ' | ' + board[23] + ' | ' + board[24]+ ' | '+ board[25]+' | ' + board[26] + ' | ' + board[27] + ' | ' + board[28]+ ' | ')
    print('  ------------------------------------')
    print(' ' + ' | ' + board[15]+ ' | ' + board[16]+ ' | ' + board[17]+ ' | ' + board[18]+ ' | ' + board[19]+ ' | ' + board[20]+  ' | ' + board[21]+ ' | ')
    print('  ------------------------------------')
    print(' '+ ' | '  + board[8] + ' | ' + board[9] + ' | ' + board[10]+ ' | ' + board[11]+ ' | ' + board[12]+ ' | ' + board[13]+ ' | '+ board[14]+ ' | ' )
    print('  ------------------------------------')
    print(' '+ ' | '  + board[1] + ' | ' + board[2] + ' | ' + board[3]+ ' | ' + board[4]+ ' | ' + board[5]+ ' | ' + board[6]+ ' | '+ board[7]+ ' | ' )
    print('  ------------------------------------')
def gagner (l,s):
    for i in [1,2,3,4,8,9,10,11,15,16,17,18,22,23,24,25,29,30,31,32,36,37,38,39]:
        if (l[i]==s and l[i+1]==s and l[i+2]==s and l[i+3]==s):
            return  True
    for i in [4,5,6,7,11,12,13,14,18,19,20,21]:
        if (l[i] == s and l[i + 7] == s and l[i + 14] == s and l[i + 21] == s):

            return True
    for i in range(1,22):
        if (l[i]==s and l[i+8]==s and l[i+16]==s and l[i+24]==s):
            return True
    for i in [1,2,3,4,8,9,10,11,15,16,17,18]:
        if (l[i] == s and l[i + 6] == s and l[i + 12] == s and l[i + 18] == s):
            return True

    return False
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
def choix_player(player1,player2): #choisir qui va commencer le premier
    if randint(0,1)==1:
        return player1
    else:
        return player2
def complet(l):
    for i in range(1,len(l)):
        if l[i] =='  ':
            return False
    return True
def Inserer(l,col,s):
    i=0
    h=0
    while i<6:
        i+=1
        if l[col]!='  ': # si la plus base case du colonne est vide on insere
         col+=7
         h+=1
    if h==6:
                col = int(input("Colonne complet choisie une autre ! :                                 QUITER : x \n"))
                while l[col] != '  ':  # si la plus base case du colonne est vide on insere
                    col+=7
    l[col]=s
def player_input():

            colonne = str(input('Choisir une colonne                                 QUITER : x \n'))# permet de tester toutes les conditions
            if colonne.lower() == 'x':
                return colonne.lower()
            while colonne  not in '1 2 3 4 5 6 7 x X'.split(): #liste des chaines des caracteres de 1 a 7
                colonne = input('Choisir une colonne de 1 a 7 :                                 QUITER : x \n')
                if colonne.lower() == 'x':
                    return colonne.lower()
            return int(colonne)
def computer_input():
    return randint(1,7) #choisir une colonne au hasard
while True:
    print('------------WELCOME TO THE GAME------------')
    print('----------------PUISSANCE 4----------------')
    board = ['  '] * 43
    mode=input("Mode SOLO : Touch 1     Mode DUO : Touch 2   \n").startswith('1') # retourne true si on tappe 1


    if not mode : # mode DUO
        player1 = str(input("Player1 : donner votre nom\t"))
        player2 = str(input("Player2 : donner votre nom\t"))
        player = choix_player(player1,player2)
        display_board(board)
        print(f"{player} will go first")
        fix_player=player2

    else: #mode MONO
        player1=str(input("Player1 : donner votre nom"))
        player = choix_player('Computer',player1)
        display_board(board)
        print(f"{player} will go first")
        fix_player='Computer'
    gameON = True
    while gameON :
        if player==player1:

                    print(f'{player1} :  ☺ ')

                    col = player_input()
                    if col=="x":
                        print("GAME SUSPENDED !!")
                        gameON=False
                    else:
                        Inserer(board,col,'☺')
                        display_board(board)
                        if gagner(board,'☺'):
                                    print(f'CONGRATULATION {player1} , YOU WIN!!')
                                    gameON=False

                        elif complet(board):
                                    print('DRAW !')
                                    gameON=False
                        else:
                                    player=fix_player

        else :
            print(f'{fix_player} : ☻ ')
            if fix_player== 'Computer':
                    col = computer_input()
            else:
                    col = player_input()
            if col == "x":
                print("GAME SUSPENDED !!")
                gameON = False
            else:
                Inserer(board, col, '☻')
                display_board(board)
            if gagner(board,'☻'):
                print(f'CONGRATULATION {fix_player} , YOU WIN!!')
                gameON = False
            elif complet(board):
                print('DRAW !')
                gameON = False

            else:
                player = player1
    if not replay() :
        print('GAME OFF !')
        break
    else:
        print('REPLAY')


