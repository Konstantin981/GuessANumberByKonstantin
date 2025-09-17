import random
computer_number = random.randint(1,100)
print("Guess a whole number between 1 and 100")
while True:
    command = input()
    if not command.isdigit():
        print("Invalid input. Please enter a whole number between 1 and 100.")
        continue
    else:
        player_number = int(command)
    if player_number > 100 or player_number < 1 or player_number % 1 != 0:
        print("Invalid number. Please enter a whole number between 1 and 100")
        continue
    player_number = int(command)
    if player_number == computer_number:
        print("Correct! You guessed right!")
        break
    elif player_number > computer_number and player_number - computer_number <=10:
        print("You are very close! A bit lower!")
    elif player_number > computer_number:
        print("Lower!")
    elif player_number < computer_number and computer_number - player_number <= 10:
        print("You are very close! A bit higher!")
    elif player_number < computer_number:
        print("Higher!")