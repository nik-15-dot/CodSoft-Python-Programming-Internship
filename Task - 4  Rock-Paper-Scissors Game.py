#Task - 4 : Rock-Paper-Scissors Game
import random

def who_won(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    player = 0
    computer = 0

    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Choose your weapon: rock, paper, or scissors")
        player = input("Your choice: ").lower()

        if player not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! ")
            continue

        computer = random.choice(['rock', 'paper', 'scissors'])

        print("You chose:", player)
        print("Computer chose:", computer)

        result = who_won(player, computer)
        print(result)

        if 'win' in result:
            player += 1
        elif 'lose' in result:
            computer += 1

        print("Scoreboard - You:", player, "Computer:", computer)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()