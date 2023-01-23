# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_weight = float(weight)
int_height = float(height)
int_height_sqrd = int_height**2
BMI = int_weight / int_height_sqrd
print(int(BMI))
