# 8. Print all numbers divisible by 5 and 7 from 1 to 100
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)