print("Welcome to our rollercoaster ride")
height = int(input("Please enter your height (in cm)\n"))
bill = 0

if height >= 128:
  print("Congratulations, you are able to ride")
  age = int(input("How old are you?\n"))
  if age < 12:
    bill = 5
    print(f"Your bill is ${bill}")
  elif age <= 18:
    bill = 7
    print(f"Your bill is ${bill}")
  else:
    bill = 12
    print(f"Your bill is ${bill}")
    
  picture = input("Do you want your pictures taken? Y or N \n")
  if picture == "Y":
    bill += 3
    print(f"Your final bill is ${bill}")
  else:
    print(f"No pictures will be taken, hence no charges.\nYour bill remains ${bill}")
else:
  print("We are sorry but you can not tall enough to participate on this ride")
