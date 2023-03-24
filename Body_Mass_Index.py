weight = float(input("Weight In Pounds: "))
height = float(input("Height In Inches: "))
weight_in_kg = weight*0.4536
height_in_cm = height*2.54
height_in_m = height_in_cm/100
bmi =round(( weight_in_kg) / (height_in_m**2),2)
print("Body Mass Index(BMI) = ",bmi)