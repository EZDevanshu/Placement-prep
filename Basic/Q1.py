# interative

n = 5

def factorial(n) :
    ans = 1
    while(n != 0) :
        ans *= n 
        n = n - 1

    print(ans)

factorial(n)


# recursive 

def fac(n) :
    if n == 1 :
        return 1 

    else :
        return n * fac(n - 1)

n = 5 

print(fac(n))