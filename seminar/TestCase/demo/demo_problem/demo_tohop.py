array  = input().split()
queue = []

def sinh_to_hop(ith = 0):
    if ith == len(array):
        sub_array = []
        for j in queue:
            sub_array.append(array[j])
        print(sub_array)
    else:
        for i in range(0, 2):
            if i == 1:
                queue.append(ith)
            sinh_to_hop(ith + 1)
            if i == 1:
                queue.pop()

# run sinh_to_hop function
sinh_to_hop()
    