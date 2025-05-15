from random import randrange
from time import sleep


def guess_number():
    def check_number():
        Run = 10
        number = randrange(0, 100)
        while Run > 0:
            try:
                print(f"\nYou have {Run} tries")
                guess = int(input("Enter number : "))
                if 0 < guess < 100:
                    if guess == number:
                        print("\nCorrect. You Win")
                        break
                    elif guess < number:
                        print("Your guess is small")
                    elif guess > number:
                        print("Your guess is bigger")
                    Run -= 1
                else:
                    print("The number must be 1 to 100")
            except:
                print("The input must be a number\nTry again")
        if Run == 0 and guess != number:
            print("\nYou lost")

    def run_game():
        print("Welcome to guess number")
        while True:
            run_game = input("Run the guess number game ? ")
            match run_game.title():
                case "Yes":
                    delay = 0
                    text = "===================="
                    while delay != 20:
                        print(text)
                        text = text.replace("=", "-", 1)
                        delay += 1
                        sleep(randrange(0, 5) / 10)
                    print(f"{text}\n")
                    print("The game is running")
                    check_number()
                case "No":
                    print("You exited the guess number game")
                    break
                case _:
                    print("Enter Yes or No")

    run_game()


if __name__ == "__main__":
    guess_number()
