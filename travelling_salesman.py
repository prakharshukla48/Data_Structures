n = int(input())
total = n**2 - n

nodes = list(map(str, input().strip().split()))

a = [[0]*len(nodes) for z in range(len(nodes))]

for t in range(total):
    l = list(map(int, input().strip().split()))
    x, y, w = l[0], l[1], l[2]
    a[x][y] = w

start = 0
i = 0
print ([i for i in range(len(nodes))])
s = set([i for i in range(len(nodes))])
def g(i, s):
    if (len(s) == 1):
        item = [k for k in s][0]
        return a[i][item] + a[item][start]
    q = []
    for j in s:
        q.append(a[i][j] + g(j, s-{j}))
    return min(q)

answer = g(i, s)
print (answer)

'''
Input
4
A B C D
0 1 16
0 2 11
0 3 6
1 0 8
1 2 13
1 3 16
2 0 4
2 1 7
2 3 9
3 0 5
3 1 12
3 2 2
'''
