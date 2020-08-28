print("Welcome to my first game!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name, "you are", age, "years old")

health = 10
print("You start the game with 10", health)

if age >= 21:
    print("You are old enough to play")
    want_to_play = input("Do you wanna play?: ").lower()
    if want_to_play == "yes":
        print("let's play")
        first_choice = input("First choice left or right?: ")
        if first_choice == "right":
            ans = input("Cool, You followed the path and reached a lake. Do you walk or swim?: ")
            if ans == "walk":
                print("You've reached other side of the lake")
            elif ans == "swim":
                print("You swam and got bitten by fish and lost 5 health")
                health -= 5
            ans = input("You noticed a house and a river. Where do you go to?: ").lower()
            if ans == "house":
                print("You went in the house and dog attacked you. You lost 5 health. You lost the game")
                health -= 5
            else:
                print("You went to the river and survived! Win!")
        else:
            print("You fell down. Try again")
    else:
        print("Googbye!")
else:
    print("You are not old enough to play")