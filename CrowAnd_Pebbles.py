import math

m1 = float(input("Initial water in jug (m1) : "))
m2 = float(input("Level of water in jug required for drinking (m2) : "))

x = float(input("Height which small pebble will increase (x) : "))
y = float(input("Height which big pebble will increase (y) : "))
n = int(input("Number of small pebbles (n): "))

small_pebble = n * x
large_pebble = (m2 - m1 - small_pebble) / y
total_pebl = math.ceil (large_pebble) + n
print("Number of big pebbles required is: ",large_pebble)
print("Number of pebbles required is: ", total_pebl)
