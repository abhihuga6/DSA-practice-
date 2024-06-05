#method implimentation
def findpowerofelement(a,n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        mid = n//2
        b = findpowerofelement(a, mid)

    result = b * b
    if n % 2 == 0:
        return result
    return result * a

#drever code
a = 2
n = 43
#function calling
result = findpowerofelement(a,n)
print("The power of the element is", result)