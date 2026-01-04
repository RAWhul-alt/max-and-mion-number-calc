a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print("Minimum number is:", minimum)
print("Maximum number is:", maximum)
