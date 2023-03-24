length = int(input("Length Of Farm In Feet: "))
breath = int(input("Breadth Of Farm In Feet: "))
row = int(length/2 + 1)
column = int(breath/2 + 1)
tree = row * column
print("No Of Rows: ", row)
print("No Of Column Required: ", column)
print("No Of Plants Required: ", tree)