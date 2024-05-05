arr = []


for i in range(5):
    arr.append(int(input("Enter the Number : ")))

def SelectionSort(arr):
    n = len(arr)
    for j in range (0,n -1):
        smallest = j
        for i in range(j+1, n):
            if arr[i] < arr[smallest]:
                smallest = i
        arr[j],arr[smallest] = arr[smallest],arr[j]        
    return arr

sortedArr = SelectionSort(arr.copy())

print("Original array:" , arr)
print("Sorted array :", sortedArr)


