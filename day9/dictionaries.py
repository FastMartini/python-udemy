# dictionary = {key: value}
# Example:
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",
#                          }

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


bid_over = False
dict = {}

while not bid_over:
    name = input ("What is your name\n")
    bid = input("How much do you want to bid?\n")

    dict[name] = bid

    question = input("Are there any other bidders? Yes/No\n").lower()
    print("\n" * 20)

    if question == "yes":
        bid_over = False
    if question == "no":
        bid_over = True


max_key = max(dict, key = dict.get)

print(f"Max bidder is {max_key} with {max(dict.values())}")

