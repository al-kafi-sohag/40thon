# 13. Count how many even numbers are there between 1 and 200
count = 0

for i in range(1, 201):
    if i % 2 == 0:
        count += 1

print(count)
