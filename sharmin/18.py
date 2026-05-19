# 18. Count total number of digits in a number
n = int(input("Enter a number: "))

count = 0

while n > 0:
    n = n // 10
    count += 1

print("Total digits =", count)