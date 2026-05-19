# 15. Find factorial of a number (using loop)

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)
