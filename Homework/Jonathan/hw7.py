# Rock paper scissors

import random

def RockPaperScissors():
    # Best of Yes
    BestOfX=int(input('Best of: '))

    # Scoring system
    Player=0
    Computer=0
    Ties=0
    
    def leaderboard():
        print('<==< Leaderboard >==>')
        print(f"Player's points: {Player}")
        print(f"Computer's points: {Computer}")
        print(f'Ties: {Ties}')
    
    # randomized messages
    random_winmessage=[
        'imagine winning',
        'You win!',
        '*happy accomplishment sound*',
        'Gouda Jouba'
    ]

    random_losemessage=[
        'imagine losing',
        'You Lost!',
        '*sad trumpet sound*',
        'Wompity womp womp! You LOST!!!!!!!'
    ]

    random_tiemessage=[
        'Tie!',
        '*sword clashing noise*',
        'You have chosen the same as the computer! Congratulations!',
        'nothing happens'
    ]

    # Just in case
    if BestOfX<=0:
        print("You can't play negative or zero rounds, genius")
    
    elif BestOfX>=7:
        print('What are you trying to do, play best of 100270139865?')
    
    # Crucial part of the game (actually announces the start and end of game)
    else:
        print(f'New game: Best of {BestOfX}')

        # Count of games to play
        count=1
        for i in range(BestOfX):
            print(f'round {count}')
            
            # The end of the game
            if count>BestOfX:
                print(f'Game has ended.')
                print()

            # Yes:
            win={
            "r":"s",
            "s":"p",
            "p":"r"
            }

            icon={
            "r":"🪨",
            "s":"✂️",
            "p":"🧻",
            'yes':'yes',
            'secret':'secret power... uh oh, why is he getting so many points?'
            }

            # Whom and Whom
            comp_choice=random.choice(["r","s","p"])
            hand=str(input("Rock, paper, scissors, shoot! Which do you choose? rock[r], paper[p], or scissors[s]? Note: You can access the help menu by typing in 'help me'. ")).lower()

            # SECRET EASTER EGGS!!!
            if hand=='yes':
                print('You have found an easter egg! You will now gain 735 points (7=y, 3=e, 5=s). Nice! ')
                Player+=735

            elif hand=='secret':
                print('You have found an easter egg... oh no! Adding points to your opponent: s=5, e=3, c=2, r=6, e=3, t=1')
                Computer+=532631

            # Da Help Menu
            def HelpMenu():
                print()
                print("<==< Help Menu >==>")
                print('Rules:')
                print(' -Rock crushes Scissors')
                print(' -Scissors cut Paper')
                print(' -Paper covers Rock')
                print()
                print('Scoring system')
                print(' -You will enter the amount of games to play')
                print(' -The winner of each round will get one point')
                print(' -These points will be saved to the leaderboard and displayed at the end of the game')
                print()
                print('New features:')
                print(' -Help Menu')
                print(' -Scoring system')
                print(' -Leaderboard')
                print(' -If you access the help menu, that will be your choice of hand and you will "lose" to the computer.')
                print()
            
            if hand=='help me':
                HelpMenu()
                break

            # Yes 2.0:
            print()
            print (f"computer's hand: {icon[comp_choice]}")
            print ("vs")
            print (f"your hand: {icon[hand]}")

            # Gamecore XXVII Ver. 6921420 Pro Yes:
            if hand=='yes' or hand=='secret':
                print('You found an easter egg! That could be good or bad.')

            elif win[hand]==comp_choice:
                print()
                print(random.choice(random_winmessage))
                print()
                Player+=1

            elif comp_choice==hand:
                print()
                print(random.choice(random_tiemessage))
                print()
                Ties+=1
            
            elif win[comp_choice]==hand:
                print()
                print(random.choice(random_losemessage))
                print()
                Computer+=1
            
            else:
                print()
                print('You have found an easter egg!')

            # Gamecore XXVII Ver. 6921420 Pro Yes (Part 2):
            count+=1

    leaderboard()

    # Final scoring   
    if Player>Computer:
        print()
        print(f'The Player has won best out of {BestOfX}!')
    
    elif Player==Computer:
        print()
        print('This game has resulted in a tie!')
    
    else:
        print()
        print(f'The Computer has won best out of {BestOfX}!')

'''
<==< Update Log >==>
-New Features!
-No extra choices (that will make the game not rock paper scissors)
-Yes
'''

RockPaperScissors()
