import numpy as np

arr = 
n = len(arr)
pos = []
maxlen = [0]
maxsum = [-999999]
result = []
def scan(i = 0):
    if i == n:
        sum = 0
        for j in pos:
            sum += arr[j]
        if sum % x == 0 and maxsum[0] < sum and len(pos) > maxlen[0]:
            maxsum[0] = sum
            maxlen[0] = len(pos)
            result.clear()
            for j in pos:
                result.append(j)
    else:
        for j in range(2):
            if j == 1:
                pos.append(i)
            scan(i + 1,)
            if j == 1:
                pos.pop()

scan()
result = [arr[i] for i in result]
print(result)