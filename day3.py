# > (Greater than)
# < (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)
# == (Equal to)
# != (Not equal to)

print("Welcome to Treasure Island. Your mission is to find the treasure.")
print("(every input is in lower case)\n")

lr = input("left or right?\n")

if lr == "right":
    print("Game Over.")
elif lr == "left":
    sw = input("swim or wait.\n")
    if sw == "swim":
        print("Game Over.")
    elif sw == "wait":
        wd = input("Which door: red, blue, or yellow?\n")
        if wd == "red":
            print("Game Over.")
        elif wd == "blue":
            print("Game Over.")
        elif wd == "yellow":
            print("You Win!")
        else:
            print("incorrect input")
    else:
        print("incorrect input")
else:
    print("incorrect input")