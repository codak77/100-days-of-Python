#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

total_bill= input("What was the total bill? $")

percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")

# int_total_bill = int(total_bill) 
# print(type(int_total_bill))

percentage_tip_calc = float(total_bill) * int(percentage_tip) / 100
sum_of_total_bill = float(total_bill) + percentage_tip_calc

no_of_pple = input("How many people will split the bill? ")

individual_bill = sum_of_total_bill / int(no_of_pple)

print(f"Each person should pay ${round(individual_bill, 2)}")
