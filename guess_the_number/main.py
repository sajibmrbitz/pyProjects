import random

def guess_the_number():

    print("---Welcome to GUESS THE NUMBER---\n")
    print("I have picked a number between 1 and 100. Can you guess it?\n")

    secret_number=random.randint(1, 100)
    attempts=0

    while True:
        try:
            guess=int(input("Enter your prediction: "))
            attempts+=1

            if guess < secret_number:
                if abs(guess - secret_number) <= 10:
                    print("You're close! Try a bit higher!\n")
                else:
                    print("Too low! Try higher!\n")
            elif guess > secret_number:
                if abs(guess - secret_number) <= 10:
                    print("You're close! Try a bit lower!\n")
                else:
                    print("Too high! Try lower!\n")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                if attempts<=5:
                    print("Verdict: GENIUS!!\n")
                elif attempts<=10:
                    print("Verdict: GREAT!!\n")
                else:
                    print("Verdict: TOO MANY ATTEMPTS!! TRY TO IMPROVE\n")
                break

        except ValueError:
            print("Please enter a valid number!!")
            continue 


if __name__ == "__main__":
    guess_the_number()