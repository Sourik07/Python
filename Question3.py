# Read input values
n = int(input("Enter the number of labourers: "))
t = int(input("Enter the total number of toys to be made: "))
d = int(input("Enter the total number of days allotted for completion: "))
d1 = int(input("Enter the number of days work had been done: "))
t1 = int(input("Enter the number of toys made in d1 days: "))

# Calculate the number of toys n labourer can make in d-d1 days
total_toy = (t1/d1)*(d-d1)

# Calculate the number of toys 1 labourer can make in d-d1 days
total_toys = total_toy/n

# Calculate the number of toys that are required in remaining (d - d1) days
remaining_toys = t - t1

# Calculate the number of extra toys left after n labour complete their work for d days
extra_toys = remaining_toys - total_toy

# Calculate the number of additional men required
additional_men = int(extra_toys / total_toys)

# Print the result
print("Number of more men required for completing the job in allotted period:", additional_men)