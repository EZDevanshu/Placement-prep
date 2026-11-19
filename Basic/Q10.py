a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    a, b = b, a

if b == 0:
    print("Division by zero is not possible")
else:
    quotient = 0
    remainder = a

    while remainder >= b:
        remainder = remainder - b
        quotient = quotient + 1

    print("Quotient =", quotient)
    print("Remainder =", remainder)