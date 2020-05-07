import random

def game():
    playing = True
    user_hand = None
    current_score = 0
    user_name = input("enter your name: ")
    print("Hello, ", user_name)
    # ratings = open('rating.txt')
    # for line in ratings:
        # name, score = line.split()
        # if name == user_name:
            # current_score = int(score)
    # ratings.close()

    game_list = input().split(",")
    if game_list == ['']:
        game_list = ["rock", "paper", "scissors"]
    print("Okay, let's start")

    while playing:
        user_hand = input()
        if user_hand not in game_list:
            if user_hand == "!exit":
                print("Bye!")
                playing = False
            elif user_hand == "!rating":
                print("Your rating:" + str(current_score))
            else:
                print("Invalid input")
        else:
            computer_number = random.randint(0, len(game_list) - 1)
            computer_hand = game_list[computer_number]
            checklist = listcheck(game_list.index(user_hand), game_list)
            if computer_hand == user_hand:
                print("There is a draw ({})".format(computer_hand))
                current_score += 50
            else:
                if checklist.index(computer_hand) < len(game_list) // 2:
                    print("Sorry, but computer chose " + computer_hand)
                else:
                    print("Well done. Computer chose {} and failed".format(computer_hand))
                    current_score += 100


def listcheck(number, game_list):
    """Takes the number of the item that the user is playing
    and returns the list that can be used to check whether
    the computers choice is a winning one or losing one
    returns the new list"""
    first_part = game_list[:number]
    second_part = game_list[number + 1:]
    return second_part + first_part

game()
