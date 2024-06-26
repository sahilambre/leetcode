def bubbleSort(arr):
    until_unsorted_index = len(arr) - 1
    sorted = False
    steps = 0
    comparision  = 0
    while not sorted:
        sorted = True

        for i in range(until_unsorted_index):
            steps += 1 
            if arr[i] > arr[i + 1]:
                comparision += 1
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

        until_unsorted_index = until_unsorted_index - 1
    
    print(arr)
    print(steps)
    print(comparision)

list = [65, 55, 45, 35, 25, 10]
bubbleSort(list)
print(list)