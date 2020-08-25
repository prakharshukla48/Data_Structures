import time

# ''.join(reversed(a)
# a[: :-1]

# Creating a list of first 1000 natural numbers 
a = []
for i in range(1000):
    a.append(i)

# USING "IN"

start1 = time.time()

total = 0
for i in a:
    total+=i
print (total)

end1 = time.time()


print ('Time taken by IN: ' + str(end1 - start1))

# USING "ENUMERATE"

start2 = time.time()

total = 0
for i, x in enumerate(a):
    total+=x
print (total)

end2 = time.time()

print ('Time taken by enumerate: ' + str(end2 - start2))
