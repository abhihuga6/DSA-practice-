#method
##recurance relation T(n) = 2t(n/2)+c
##using master's theorem T(n) = o(n)
def findmaxandmin(arr, i, j):
    if i == j:
        max_val = arr[i]
        min_val = arr[i]
    #two element condition
    elif i == j -1:
        if arr[i] < arr[j]:
            max_val = arr[j]
            min_val = arr[i]
        else:
            max_val = arr[i]
            min_val = arr[j]

    else:
        mid = i + (j-i)//2
        max_1, min_1 = findmaxandmin(arr, i, mid)
        max_2, min_2 = findmaxandmin(arr, mid+1, j)

        if max_1 < max_2:
            max_val = max_2
        else:
            max_val = max_1
        if min_1 < min_2:
            min_val = min_1
        else:
            min_val = min_2
    return max_val, min_val

#driver code
arr = [20,39,45,65,21,44,89,92]
i = 0
j = len(arr) - 1
#functioncalling
max_val, min_val = findmaxandmin(arr, i, j)
print('maximum and minimum value in the array is',max_val, min_val)