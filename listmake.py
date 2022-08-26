a = [x*x for x in range(12)]
print(a)
b = [x*x for x in range(14) if x%2==1]
print(b)
c = [[m+n for m in ['z','j','h']] for n in ['l','y','h']]
print(c)