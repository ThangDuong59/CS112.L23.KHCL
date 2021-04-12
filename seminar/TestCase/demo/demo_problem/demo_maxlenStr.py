array  = list(map(int, input().split()))
x = int(input())
queue = []
maxLen = 0
maxSum = -9999999
match_sub_array = []

def max_len_str(ith = 0):
    if ith == len(array):
        global x, maxLen, maxSum, match_sub_array
        sub_array = []
        sum_sub_array = 0

        for j in queue:
            tmp = array[j]
            sub_array.append(tmp)
            sum_sub_array += tmp
        
        if sum_sub_array % x == 0:
            if sum_sub_array > maxSum:
                match_sub_array = sub_array
                maxSum = sum_sub_array
                maxLen = len(sub_array)
            elif sum_sub_array == maxSum:
                if len(sub_array) > len(match_sub_array):
                    match_sub_array = sub_array
                    maxSum = sum_sub_array
                    maxLen = len(sub_array)
        
    else:
        for i in range(0, 2):
            if i == 1:
                queue.append(ith)
            max_len_str(ith + 1)
            if i == 1:
                queue.pop()

max_len_str()
print(match_sub_array)