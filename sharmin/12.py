# 12. Multiplication table of any number (take input from user)
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
