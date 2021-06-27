weights_values = []
queue, max_sum_values = [], 0
#n, m = 0, 0

n, m = list(map(int, input().split()))
for i in range(n):
    tmp = list(map(int, input().split()))
    weights_values.append(tmp)

# each item can just select one time

def packageOne(k = 0):
    global n
    if k == n:
        global  max_sum_values
        sum_weight, sum_value = 0, 0
        for i in queue:
            sum_weight += weights_values[i][0]
            sum_value += weights_values[i][1]
        if sum_weight <= m:
            if sum_value > max_sum_values:
                max_sum_values = sum_value
        
    else:
        for i in range(0, 2):
            if i == 1:
                queue.append(k)
            packageOne(k + 1)
            if i == 1:
                queue.pop()


def packageTwo(k = 0):
    global n
    if k == n:
        global  max_sum_values
        sum_weight, sum_value = 0, 0
        for i in range(n):
            sum_weight += queue[i] * weights_values[i][0]
            sum_value +=  queue[i] * weights_values[i][1]
        if sum_weight <= m:
            if sum_value > max_sum_values:
                max_sum_values = sum_value

    else:
        tmp = int(m / weights_values[k][0])
        for i in range(0, tmp + 1):
            queue.append(i)
            packageTwo(k + 1)
            queue.pop()


def main():
    global max_sum_values
    
    # Task 1
    packageOne()

    # Task 2
    #packageTwo()
    
    print(max_sum_values)

if __name__=='__main__':
    main()