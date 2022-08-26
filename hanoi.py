def Hanoi(n,src,mid,dist):
    if(n == 1):
        print("%c -> %c" %(src,dist))
    else:
        Hanoi(n-1,src,dist,mid)
        print("%c -> %c" %(src,dist))
        Hanoi(n-1,mid,src,dist)
    return

n = int(input())
Hanoi(n,'A','B','C')