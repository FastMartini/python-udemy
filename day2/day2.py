#Tip Calculator

print("Welcome to the Tip Calculator!")


bill = float(input("How much was your total bill?\n"))
tip_pct = int(input("what percentage of tip would you like to give? (10%, 15%, 20%, etc.)\n"))
people = int(input("How many people will split the bill?\n"))

tip = (tip_pct * .01) + 1
total_per_person = (bill / people) * tip

print("Each person should pay: $" + str(round(total_per_person, 2)))



