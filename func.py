def Isprim(n):
    if(n%2==0 and n!=2 or n<=1 ):
        return False
    elif (n==2):
        return True
    else:
        for i in range(3,n,2):
            if(n%i==0):
                return False
            if(i**2>n):
                break
    return True

for i in range(300):
    if(Isprim(i)):
        print("num %d is prime" %i)
