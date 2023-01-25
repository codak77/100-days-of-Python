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
  elif age >= 45 and age <= 56:
    print("Your bill has already been taken care of by our sponsor")
  else:
    bill = 12
    print(f"Your bill is ${bill}")
    
  picture = input("Do you want your pictures taken? Y or N \n")
  if ((picture == "Y") and (age <= 44 or age >= 57)):
    bill += 3
    print(f"Your final bill is ${bill}")
  elif ((picture == "N") and (age <= 44 or age >= 57)):
    print(f"No pictures will be taken, hence no charges.\nYour bill remains ${bill}")
  elif picture == "Y":
    print("Don't forget to smile for the camera!")
  else:
    print("Too bad, You know it's also free for you right?")
else:
  print("We are sorry but you can not tall enough to participate on this ride")
