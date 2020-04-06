b = 'abcaby'
n, i, j = len(b), 1, 0
temp = [0]
z = 0
while (i < n and j < n):
    if not(b[j] == b[i]):
        if (j > 0):
            j = temp[j-1]
            z = j
        else:
            temp.append(z)
            
            i = i + 1

    else:
        temp.append(z+1)
        i = i + 1
        j = j + 1
        z = z + 1
print (temp)
text = 'abyabc'
n, m, i, j = len(text), len(b), 0, 0
while (i%n < n and j < m):
    if (text[i%n] == b[j]):
        i = i + 1
        j = j + 1
    else:
        if (j == 0):
            i = i + 1
        else:
            j = temp[j-1]
if (j == m):
    print ('Yes')
else:
    print ('No')
