print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15? (Please only add a number without % sign) \n"))
people = int(input("How many people to split the bill? \n"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

each_person_bill = total_bill/ people
final_amount = round(each_person_bill, 2)
print(f"Each person should pay: ${final_amount}")
