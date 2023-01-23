# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = 90
months = 12
weeks = 52
days = 365

rem_years = years - int(age)
rem_months = months * rem_years
rem_weeks = weeks * rem_years
rem_days = days * rem_years

print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left.")
