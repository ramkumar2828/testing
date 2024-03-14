import random

print("lets start the number game")

top_range = input("Enter the number ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <=0 :
        print("please enter number greater than 0 next time")
        quit()

else:
    print("enter the number please")
    quit()

print(top_range)

random_number = random.randint(1,top_range)

print("randomnumber is ",random_number)


guesses = 0
while True:
    guessed_number = input("guess the number ")
    guesses +=1

    if guessed_number.isdigit():
        guessed_number = int(guessed_number)

        if guessed_number <=0 :
            print("please enter number greater than 0 next time")
            continue
        elif random_number == guessed_number:
            print("guess is correct in ",guesses,"guesses")
            break
        elif guessed_number > random_number:
            print("your guess is above the number")
            continue
        else:
            print("your guess is below the number")
        
    else:
        print("enter the number please")
        continue






