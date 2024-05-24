#binary search algoarithm
#function defination
def binarysearch(arr, x, i, j):
    while i <= j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            #right side of the mid
            return binarysearch(arr, x, mid+1, j)
        else:
            return binarysearch(arr, x, i, mid-1)

#searching element is not present in arr

arr=[20, 30, 40, 50, 60, 70, 80, 90]
x = 70
i = 0
j = len(arr) - 1
result = binarysearch(arr, x, i, j)
print("searching element is present at the location:",result)