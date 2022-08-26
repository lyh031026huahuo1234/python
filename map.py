from re import X


def f(x):
    return x**x

a = map(f,{1,2,3,4})
print(list(a))
print(tuple(a))
a = list(map(lambda x:x**3,[1,2,3,4]))
print(a)
x,y,z = map(int,input().split())
print(x,y,z) 