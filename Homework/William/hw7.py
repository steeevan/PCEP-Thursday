#Lesson 7

import random as ra

option=["rock","paper","scissors","spock","lizard"]
rounds=[3,5,7]
user_score= 0
computer_score= 0
def picking():
    while True:
        action= input("Pick a option between rock, paper, scissors: ")
        if action.lower() in option:
            return action.lower()
        else:
            print("try again")

def get_computer_choice():
    return ra.choice(option)

def result(l1,l2):
    """
    value=0
    value2=1
    print("result:")
    for i in range (len(l1)):
        print(f"\nIn round {value2} player chosed {list(l1[value])} and computer chosed {list(l2[value])}")
        value+=1
        value2+=1

    pause
    """

def save(player_score):
    with open("score.txt","w")as file:
        file.write(player_score)

def display_saves():
    """
    with open('your_file.txt', 'r') as file:
    for line in file:
        if 'your_keyword' in line:
            value = line.split(':')[1].strip() 
            print(value)

    I don't know how to extract it yet
    """


def choosing_round():
    start= True
    while start:
        chose_round= (input("\n How many round do you want : 3,5,7 or infinite : "))
        if chose_round== "3" or chose_round== "5" or chose_round== "7" or chose_round.lower()=="infinite":
            start= False
            return chose_round 
        else:
            print("try again")

def help_menu():
    select= input("\n Need to open help menu? : yes or no :  ")
    select.lower()
    if select == "yes":
        print("\n You can chose rounds between 3,5,7 ,or infinite")
        print("It a rock, paper, scissors game with additional choice of lizard and spock and you are competing against a computer")
        print("You have 3 choice between rock, paper, scissors, spock, and lizard")
        print("Rock crushes Lizard")
        print("Scissors cuts Paper.")
        print("Paper covers Rock.")
        print("Rock crushes Lizard.")
        print("Lizard poisons Spock.")
        print("Spock smashes Scissors.")
        print("Scissors decapitates Lizard.")
        print("Lizard eats Paper.")
        print("Paper disproves Spock.")
        print("Spock vaporizes Rock.")
        print("Your goal is to win : Good Luck")
    else:
        pass

def random_message(who_win):
    tie_m=["Atleast you didn't loose","Atleast the computer didn't win"]
    player_m=["Great one!!!","Nice!!!","Wow!!!"]
    computer_m=["It fine","You will do it","You can win next time"]
    if who_win=="player win":
        print("\n")
        print(ra.choice(player_m))
    elif who_win==" Ii a tie":
        print("\n")
        print(ra.choice(tie_m))
    else:
        print("\n")
        print(ra.choice(computer_m))
    


def determine_winner(user,computer):
    if user==computer:
        return "It tie"
    elif user=="rock" and computer=="scissors":
        return "player win"
    elif user=="paper" and computer=="rock":
        return "player win"
    elif user=="scissors" and computer=="paper":
        return "player win" 
    elif user=="rock" and computer=="lizard":
        return "player win"
    elif user=="lizard" and computer=="spock":
        return "player win"
    elif user=="spock" and computer=="scissors":
        return "player win"
    elif user=="scissors" and computer=="lizard":
        return "player win"
    elif user=="lizard" and computer=="paper":
        return "player win"
    elif user=="paper" and computer=="spock":
        return "player win"
    elif user=="spock" and computer=="rock":
        return "player win"
    else:
        return "computer win"

 

def game(user_choice,computer_choice,result):
    print("\n")
    print(f"you chose {user_choice}")
    print(f"computer chose {computer_choice}")
    print(result)
    return result

def play_game():
    global user_score, computer_score
    user_score=0
    computer_score=0
    help_menu()
    chose= choosing_round()
    computer_list=[]
    player_list=[]
    while True:
        if chose.lower() == "infinite" :   
            computer= get_computer_choice()
            user=picking()
            result= determine_winner(user,computer)
            game(user,computer,result)
            random_message(result)
            if result=="tie":
                pass
            elif result== "player win":
                user_score+=1
            else:
                computer_score+=1
            computer_list.append(computer)
            player_list.append(user)
            print(f"you scored {user_score} and computer scored {computer_score}")
            continu= input("\n do you want to continue: yes or no ").lower()
            if continu =="yes":
                pass
            elif continu=="no":
                result(player_list,computer_list)
                save(user_score)
                print("\n thanks for playing")
                
                break
        elif chose== "3":
            for i in range (3):
                computer= get_computer_choice()
                user=picking()
                result= determine_winner(user,computer)
                game(user,computer,result)
                random_message(result)
                if result=="tie":
                    pass
                elif result== "player win":
                    user_score+=1
                else:
                    computer_score+=1
                print(f"you scored {user_score} and computer scored {computer_score}")
                computer_list.append(computer)
                player_list.append(user)
            result(player_list,computer_list)
            save(user_score)
            print("\n thanks for playing")
            
            break
        elif chose =="5":
            for i in range(5):
                computer= get_computer_choice()
                user=picking()
                result= determine_winner(user,computer)
                game(user,computer,result)
                random_message(result)
                if result=="tie":
                    pass
                elif result== "player win":
                    user_score+=1
                else:
                    computer_score+=1
                computer_list.append(computer)
                player_list.append(user)
                print(f"you scored {user_score} and computer scored {computer_score}")
            result(player_list,computer_list)
            save(user_score)
            print("\n thanks for playing")
            
            break
            
        elif chose=="7":
            for i in range(7):
                computer= get_computer_choice()
                user=picking()
                result= determine_winner(user,computer)
                game(user,computer,result)
                random_message(result)
                if result=="tie":
                    pass
                elif result== "player win":
                    user_score+=1
                else:
                    computer_score+=1
                computer_list.append(computer)
                player_list.append(user)
                print(f"you scored {user_score} and computer scored {computer_score}")
            result(player_list,computer_list)
            save(user_score)
            print("\n thanks for playing")
            break

play_game()

