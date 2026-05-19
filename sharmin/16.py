# 16. Reverse a given number (e.g., 12345 → 54321)
n = int(input("Enter a number: "))

rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

print(rev)
