# BMI Calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / height ** 2)

# < 18 = underweight
# > 18 - 25 = normal
# > 25 - 30 = slightly overweight
# > 30 - 35 = obese
# > 35 = clinically obese

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI <= 25:
  print(f"Your BMI is {BMI}, you are normal weight.")
elif BMI <= 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <= 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")





