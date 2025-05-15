print("Welcome to Guess the number")
import random
def Number(orginal_Number, guess_Number):
    def check_Number(org_Number, guess):
        if guess == org_Number:
            print("You Win")
            return True
        elif guess < org_Number:
            print("Your guess is smaller")
        elif guess > org_Number:
            print("Your guess is bigger")
    if 0 <= guess_Number <= 100:
        result = check_Number(orginal_Number, guess_Number)
    else:
        print("The guess must be between 1 and 100")
        return False
    return result
Run = 10
number = random.randrange(0, 100)
while Run > 0:
    print(f'You have {Run} chances to guess')
    input_Number = int(input("Guess what number it is (0 - 100) : "))
    result = Number(number, input_Number)
    if result == True:
        break
    elif result == False:
        continue
    Run -= 1