import random

def get_choices():
    player_choice = input('Could you please choose rock, paper, or scissors?').capitalize()
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    if player == computer:
        print("The computer choose: " + computer)
        return "It's a tie!"
    if player == 'Rock' and computer == 'Scissors':
        print("The computer choose: " + computer)
        return "Player wins!"
    if player == 'Rock' and computer == 'Paper':
        print("The computer choose: " + computer)
        return "Computer wins!"
    if player == 'Paper' and computer == 'Rock':
        print("The computer choose: " + computer)
        return "Player wins!"
    if player == 'Paper' and computer == 'Scissors':
        print("The computer choose: " + computer)
        return "Computer wins!"
    if player == 'Scissors' and computer == 'Rock':
        print("The computer choose: " + computer)
        return "Computer wins!"
    if player == 'Scissors' and computer == 'Paper':
        print("The computer choose: " + computer)
        return "Player wins!"

choices = get_choices()
player_choice = choices["player"]
computer_choice = choices["computer"]

result = check_win(player_choice, computer_choice)
print(result)

