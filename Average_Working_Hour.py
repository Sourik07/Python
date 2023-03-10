n = 0
for i in range(5):
 h = float(input(f"No. of hours worked on Day {i+1}: "))
 n = n+h
print("Average hours worked in a week:",round(n/5),"hours")
