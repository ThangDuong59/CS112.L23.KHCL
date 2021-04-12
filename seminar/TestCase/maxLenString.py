import numpy as np

pos = []
maxlen = [0]
maxsum = [-999999]
result = []

def scan(arr_tmp, x_tmp, i = 0):
    n_tmp = len(arr_tmp)
    if i == n_tmp:
        sum = 0
        for j in pos:
            sum += arr_tmp[j]
        if sum % x_tmp[0] == 0 and maxsum[0] < sum and len(pos) > maxlen[0]:
            maxsum[0] = sum
            maxlen[0] = len(pos)
            result.clear()
            for j in pos:
                result.append(j)
    else:
        for j in range(2):
            if j == 1:
                pos.append(i)
            scan(arr_tmp, x_tmp, i + 1)
            if j == 1:
                pos.pop()

def main(arr, x):
    print(arr)
    global result
    global maxlen
    global maxsum
    global pos
    scan(arr, x)
    maxlen, maxsum, pos = [0] , [-999999], [] 
    a = [arr[i] for i in result]
    return a



