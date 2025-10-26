import random
import day4_mod

# Rock, Paper Scissors
#-------------------------------------
# prints a pseudo random integer from 1 to 10

# rand_int = random.randint(1, 10)
# print(rand_int)

# you can multiply to increase range:

# rand_num_0_to_1 = random.random() * 10
# print(rand_num_0_to_1)

# example with heads or tails:

# rand_int = random.randint(1, 2)

# if rand_int == 1:
    # print("Tails")
# else:
    # print("Heads")
#-------------------------------------
# transcribes data from an imported file

# print(day4_mod.my_fav_num)
#-------------------------------------
# Examples of Lists:

# states_of_usa = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
# print(states_of_usa[0])
# print(states_of_usa[-50])

# add more items in list:

# states_of_usa.append("Diegoland")
# states_of_usa.extend("Diegoland", "Diegonia")
#-------------------------------------

rand_int = random.randint(0, 2)

user = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if user == 0:

    if rand_int == 0:
        print("Computer chose: Rock")
        print("You tied!")
    elif rand_int == 1:
        print("Computer chose: Paper")
        print("You lose!")
    else:
        print("Computer chose: Scissors")
        print("You win!")

elif user == 1:

    if rand_int == 0:
        print("Computer chose: Rock")
        print("You win!")
    elif rand_int == 1:
        print("Computer chose: Paper")
        print("You tied!")
    else:
        print("Computer chose: Scissors")
        print("You lose!")

elif user == 2:

    if rand_int == 0:
        print("Computer chose: Rock")
        print("You lose!")
    elif rand_int == 1:
        print("Computer chose: Paper")
        print("You win!")
    else:
        print("Computer chose: Scissors")
        print("You tied!")

else:
    print("incorrect input")


