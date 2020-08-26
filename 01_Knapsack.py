t = int(input())

while (t > 0):
    K = list(map(int, input().strip().split()))
    N = K[1]
    S = K[0]
    weights = []
    values = []
    for z in range(N):
        l = list(map(int, input().strip().split()))
        weights.append(l[0])
        values.append(l[1])
    
    a = [[0]*(S+1) for q in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, S+1):
            if (weights[i-1] > j):
                a[i][j] = a[i-1][j]
            else:
                a[i][j] = max(values[i-1]+a[i-1][j-weights[i-1]], a[i-1][j])
    
    print (a[N][S])
    
    t = t - 1

'''
1
4 5
1 8
2 4
3 0
2 5
2 3
'''
