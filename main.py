import random
print("Welcome to guess number")
def guess_number():
    Run = 10
    number = random.randrange(0, 100)
    while Run > 0:
        try:            
            print(f'\nYou have {Run} tries')
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
guess_number()