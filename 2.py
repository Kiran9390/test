def count(a, c) :
    res = 0
    for i in range(len(a)) :
        if (a[i] == c):
            res = res + 1
    return res
a,b = input().split()
x=len(b)
c=b[x-1]
z=count(a,c)
print(z)
