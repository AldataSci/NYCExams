arra = [1,2,3,4,5]

def twosums(arr,target):
    prevMap = {}
    for i, n in enumerate(arr):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
    return 'Not Found'

print(twosums(arra,5))