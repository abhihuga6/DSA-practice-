#method implimentation
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#driver code
arr = [70, 20, 50, 60, 35, 47]
result = bubblesort(arr)
print("array after using bubble sort is:", result)
