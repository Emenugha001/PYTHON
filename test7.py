    # coding for a bmi machine, this is a machine used to run fat bscreens in the hospital.
    # Something i did on my own, i donno if its okay

Name     = input ( 'Enter Name: '  )
Height_m = float(input ( 'Enter Height_in _m: ' ))
Weight_kg = float(input ( 'Enter weight_in_Kg: ' ))


bmi = Weight_kg/(Height_m**2)
print ('bmi:   ')
print (bmi)

if bmi < 18:
  print (Name + " Is Sadly-Underweight")
elif 18 <=bmi < 24.9:
  print (Name + " Is Very Healthy")
elif 25 <= bmi < 29.9:
  print (Name + " Is Over-weight")
elif 30 <=bmi < 39.9:
  print (Name + " Is Obese")
elif bmi > 40:
  print(Name + " Is Severely Obese")
else:
  print( "See a Doctor urgently, This could be a death case")
print ("Thanks For Using Our BMI App")