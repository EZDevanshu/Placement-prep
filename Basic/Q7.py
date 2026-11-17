n = int(input("Enter how many numbers: "))

num = int(input("Enter number: "))

maximum = num
minimum = num
total = num

for i in range(1, n):
    num = int(input("Enter number: "))

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

    total = total + num

average = total / n