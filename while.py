s = input()
list = s.split()
maxV = int(list[0])
try:
    while True:
        lst = s.split()
        for x in range(lst):
            maxV = max(maxV,int(x))
        s = input()
except:
    pass
print("the maximum num is %d"% maxV)