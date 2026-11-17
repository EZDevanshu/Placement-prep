# WAP to find a summation of a digit of a given number. (Iterative and recursive) 

# interative

n = 5
ans = 0
for i in range(0 , n + 1) :
    ans += i

print(ans)

# recursive 
ans1 = 0
def summation(n) :
    if n <= 1 :
        return n
    else :
       return n + summation(n - 1) 
        
n = 5 
print(summation(n))