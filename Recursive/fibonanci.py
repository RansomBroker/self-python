def fibonancci(n):
    if n == 0 :
        return 0
    elif n == 1 : 
        return 1
    else : 
        return fibonancci(n-1) + fibonancci(n-2)

n = 10
j = 0
for i in range(int(n)):
    print("bilanggan fibonanci ke ("+str(i)+") : "+ str(fibonancci(j)))
    j += 1