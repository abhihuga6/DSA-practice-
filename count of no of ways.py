#method implimentation
def possibilities(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return possibilities(n-1) + possibilities(n-2)

##driver code
n = 4
result = possibilities(n)
print(result)