import re

# function to find the weightage
def weightage(user):
    if (user == 'G'):
        return 2
    elif (user == 'M'):
        return 1
    else:
        return None


def _main(N):
    dic = {}   # dict to store weightage of each number occured
    messages = []
    for i in range(N):
        s = ''
        s = str(input())
        messages.append(s)

    for message in messages:
        digits = re.findall(r'\d+', message)
        
        if (len(digits) > 0):
            for digit in digits:
                dic[int(digit)] = 0    # initialize each element to 0 weightage
                
    for message in messages:
        user = message[0]
        digits = re.findall(r'\d+', message)    # find the digits
        if (len(digits) > 0):
            for digit in digits:
                d = int(digit)
                dic[d] = dic[d] + weightage(user)  # find the weightages

    m = 0
    for i in dic:
        if (dic[i] > m):
            m = dic[i]
            date = i           # find the max weightage and its date
    n = 0
    
    for j in dic:
        
        if (dic[j] == m):
            n = n + 1

    if (n > 1):  # check if two dates have max weightages
        print ('No date')
    else:
        if (date == 19 or date == 20):
            print ('Date')

_main(4)
        
