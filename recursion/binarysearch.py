
def binary_search(array=list(), left=0, right= 0, x=0):
    if left > right :
        return -1

    mid = int((left + right )/2)
    if x == array[mid]:
        return mid

    if x < array[mid]:
        return binary_search(array, left, mid-1, x)
    # discard left half 
    return binary_search(array, mid+1, right, x)

print(binary_search([-1,0,2,3,4,5,6,7,8,20,40],0,10,x=20))