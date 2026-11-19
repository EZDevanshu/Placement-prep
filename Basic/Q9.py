a = int(input("Enter base: "))
b = int(input("Enter exponent: "))

result = 1

for i in range(b):
    temp = 0

    for j in range(a):
        temp = temp + result

    result = temp

print("Power =", result)
