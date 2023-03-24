total = int(input("Total Nuts And Bolts in the Bag: "))
nuts = int(input("Total No Of Nuts: "))
bolts = total-nuts
defective_nuts = int(input("Defective Nuts Percentage: "))
defective_bolts = int(input("Defective Bolts Percentage: "))
a = 100-defective_nuts
b = 100-defective_bolts
non_defective_nuts = (nuts*a)/100
non_defective_bolts = (bolts*b)/100
total_non_defective = non_defective_nuts+non_defective_bolts
final = round((total_non_defective/total)*100,2)
print("Percentage of non-defective items in bag: ", final)