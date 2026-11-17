# WAP to find a total odd and total even digit of a given number.
num = 12345
even = 0
odd = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    num = num // 10

print(odd)
print(even)
