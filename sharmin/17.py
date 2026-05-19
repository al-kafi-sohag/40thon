# 17. Find sum of digits of a number (e.g., 1234 = 1+2+3+4 = 10)
# Find sum of digits of a number

n = int(input("Enter a number: "))

total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits =", total)