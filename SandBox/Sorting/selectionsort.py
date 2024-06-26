def selectionSort(arr):
    for i in range(len(arr)):
        lowestNumberIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowestNumberIndex]:
                lowestNumberIndex = j
        
        if lowestNumberIndex != i:
            arr[i], arr[lowestNumberIndex] = arr[lowestNumberIndex], arr[i]

        
    return arr
    

list = [4,2,7,1,3]

selectionSort(list)

print(list)