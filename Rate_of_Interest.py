initial = int (input("Initial Amount : "))
n = int(input("No of Years: "))
expected = int (input("Expected Amount : "))
result = ((expected - initial) / (initial * n)) * 100
print("Rate of Interest", result , "%")