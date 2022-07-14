# Sample game
# if you want to play it, run it on an IDE 
import random

name = input("Hi there! What's your name? ")
print("Hello, ", name, "\b!")
question = input("Are you down for playing a game? [Y/N] ")
if question.lower() == 'n':
    print("Ok, your choice!")
elif question.lower() == 'y':
    # Level 1
    game_over = 0
    score = 0
    print("Ok, let's do this. It's just a math quiz!")
    while game_over != 1:
        rand_num1 = random.randrange(1, 13)
        rand_num2 = random.randrange(1, 13)
        print(rand_num1, "x", rand_num2)
        answer = input(" = ")
        if int(answer) == rand_num1 * rand_num2:
            score += 10
        else:
            game_over = 1
    print("Game over! You had a score of ", score, "points")
    decision = input("Do you want to go on? [Y/N] ")
    if decision.lower() == 'n':
        print("Ok, bye!")
        exit()
    elif decision.lower() == 'y':
        # Level 2
        print("The second part of the game is all about luck")
        rand_num = random.randrange(1, 11)
        ans = input("I'm thinking of a number between 1-10, which one is it? ")
        number = int(ans)
        tries = 0
        num_found = 0
        while num_found != 1:
            if number < rand_num:
                number = int(input("Guess higher "))
            elif number > rand_num:
                number = int(input("Guess lower "))
            else:
                print("That's the number! Congratulations!")
                num_found = 1
            tries += 1
        print("It took you ", tries, "tries!")
        print("It was nice playing with you, my friend!")
print("Have a nice day!")