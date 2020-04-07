p, i = 4, 0
n = int(input())
a = [0] * n
a[0], a[1], a[2], a[3] = 4, 5, 44, 55
if n < 4:
    for e in range(n):
        print (a[e])
else:
    for e in range(4):
        print (a[e])
    while (p < n):
        a[p] = int('4'+str(a[i])+'4')
        print (a[p])
        p = p + 1
        if p == n:
            break
        a[p] = int('4'+str(a[i+1])+'4')
        print (a[p])
        p = p + 1
        if p == n:
            break
        a[p] = int('5'+str(a[i])+'5')
        print (a[p])
        p = p + 1
        if p == n:
            break
        a[p] = int('5'+str(a[i+1])+'5')
        print (a[p])
        p = p + 1
        i = i + 2
