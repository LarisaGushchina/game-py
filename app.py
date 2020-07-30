print("Welcome to my game!")
name = input("Enter you name gamer: ")
age = int(input("Enter you age gamer: "))
print("I am greeting you", name, age, "years old!")

health = 10



if age >= 18:
    print("You're old enough to play!")

    want_to_play = input("Do you want to play? ").lower()
    if want_to_play == "yes":
        print("Lets play!")
        print("You are starting with", health, "health")
        left_or_right = input("Your first choice. Left or Right? ").lower()
        if left_or_right == "right":
            ans = input("Cool! You've reached a lake. Do you swim across or walk around?(around/swim) ").lower()
            if ans == "around":
                print("You've reached other side if the lake")
            elif ans == "swim":
                print("You swam acroos and got bitten by a fish and lost 5 health")
                health -= 5

            ans = input("You noticed a house and a river. Were do you go to? ").lower()
            if ans == "house":
                print("You go to the house and greeted by the owner of the house. He doesn't like you. You lost 5 health")
                health -= 5

                if health <= 0:
                    print("You have 0 health and you lost the game...")
                else:
                    print("You've survived.. You win! Congrats!")



            else:
                print("You fell in a river and lost...")

        else:
            print("You're lost")

    else:
        print("See you later!")
else:
    print("You're young to play my game")








