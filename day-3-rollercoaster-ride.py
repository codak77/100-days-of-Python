print("Welcome to our rollercoaster ride")
height = int(input("Please enter your height (in cm)\n"))

if height >= 128:
  print("Congratulations, you are able to ride")
  age = int(input("How old are you?\n"))
  if age < 12: 
    print("Your fine is $5")
  elif age <= 18:
    print("Your fine is $7")
  else:
    print("Your fine is $12")
else:
  print("We are sorry but you can not tall enough to participate on this ride")
