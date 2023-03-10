M = int(input("Enter Marks obtained: "))
A = int(input("Enter Class average: "))
print("Grade:",end=" ")
if M>=A:
 if M-A>=20:
  print("S Grade")
 elif M-A>=10:
  print("A Grade")
 else:
  print("B Grade")
else:
 if A-M<=5:
  print("B Grade")
 elif A-M<=10:
  print("C Grade")
 elif A-M<=15:
  print("D Grade")
 else:
  print("F Grade")
