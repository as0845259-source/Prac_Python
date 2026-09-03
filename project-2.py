# Rock Paper Game

import random
l = ['Rock', 'scissor', 'paper']

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
Game Start.....                   
1 Yes | Play
2 No  | Exit             
                   '''))
    
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
1 Rock
2 Scissor
3 Paper                                                            
                                  '''))
            if userInput == 1:
                uchoice = 'Rock'
            elif userInput == 2:
                uchoice = 'Scissor'
            elif userInput == 3:
                uchoice = 'paper'

            Cchoice = random.choice(l)

            if Cchoice == uchoice:
                ccount = ccount + 1
                ucount = ucount + 1
                winner = "Draw"
            elif (uchoice == "paper" and Cchoice == "Rock") or (uchoice == "Scissor" and Cchoice == "paper") or (uchoice == "Rock" and Cchoice == "scissor"):
                ucount = ucount + 1
                winner = "User"
            else:
                ccount = ccount + 1
                winner = "Computer"

            print(f"Round {a}: User = {uchoice}, Computer = {Cchoice}, Winner = {winner}")

        if ucount == ccount:
            print("Final Game Draw...")
            print("User Count:", ucount)
            print("Computer Count:", ccount)
        elif ucount > ccount:
            print("Final You Win the Game...")
            print("User Count:", ucount)
            print("Computer Count:", ccount)
        else:
            print("Final Computer win the Game...")
            print("User Count:", ucount)
            print("Computer Count:", ccount)

    else:
        break