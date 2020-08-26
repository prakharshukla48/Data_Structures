l = list(map(int, input().strip().split()))

m1 = l[0]
m2 = l[1]

days = int(input())

stocks = list(map(float, input().strip().split()))
trends = 0

for i in range(m1, days):
    if (i < m2):
        continue
    m1_y1 = 0
    m1_y2 = 0
    m2_y1 = 0
    m2_y2 = 0
    for j in range(0, m2):
        if(j<m1):
            m1_y2 = m1_y2 + stocks[i-j]
            if (j != 0):
                m1_y1 = m1_y1 + stocks[i-j]
                
        m2_y2 = m2_y2 + stocks[i-j]
        if (j != 0):
            m2_y1 = m2_y1 + stocks[i - j]
            
    m1_y1 = m1_y1 + stocks[i-m1]
    m1_y1 = m1_y1 / m1
    m1_y2 = m1_y2 / m1
    m2_y1 = m2_y1 + stocks[i-m2]
    m2_y1 = m2_y1 / m2
    m2_y2 = m2_y2 / m2
    
    if (m1_y2 >= m2_y2 and m1_y1 < m2_y1):
        trends+=1
    elif (m1_y2 <= m2_y2 and m1_y1 > m2_y1):
        trends+=1
print (trends, end='')
