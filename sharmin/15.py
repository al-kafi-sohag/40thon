# 15. Find factorial of a number (using loop)
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)



