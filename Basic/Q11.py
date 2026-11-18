# ugly or not 

n = 6 

li = [] 
if n <= 1 :
    print("False")

for i in range(2 , n + 1) :
    if n % i == 0 :
        for j in range(2 , i + 1) :
            if i % j == 0 :
                break
            else :
                li.append(i)

prime = [2 , 3 , 5]

for i in li : 
    if i not in prime :
        print("False")
        break
else :
    print("True")