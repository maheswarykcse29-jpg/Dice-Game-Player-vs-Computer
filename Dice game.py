import random
def roll_dice():
    return random.randint(1, 6)
def play_game():
    player_score = 0
    computer_score = 0
    rounds = 5
    for i in range(rounds):
        input("Press Enter to roll dice...")
        player = roll_dice()
        computer = roll_dice()
        print("You rolled:", player)
        print("Computer rolled:", computer)
        if player > computer:
            print("You win this round!")
            player_score += 1
        elif computer > player:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print("---------------------")

    print("Final Score")
    print("You:", player_score)
    print("Computer:", computer_score)
play_game()
