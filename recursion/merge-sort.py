# def merge_sort(data, start, end):
#     if start < end:
#         mid = int((start+end)/2)
#         print(mid)

#         # continously dividing 
#         merge_sort(data, start, mid)
#         merge_sort(data, mid+1, end)
#         merge(data, start, mid, end)

# def merge(data, start, mid, end):
#     # build temp to avoid modifying original array
#     temp = []

#     i= start
#     j= mid
#     k= 0

#     while i<=mid and j <=end:
#         print(temp)
        
#         if data[i]<data[j]:
#             print(data[i], "<", data[j])
#             temp.append(data[i])
#             i+=1
#         else:
#             print(data[i], ">", data[j])
#             temp.append(data[j])
#             j+=1
#         # k+=1

#     while i < mid:
#         temp.append(data[i])
#         i+=1
    
#     while j < end:
#         temp.append(data[j])
#         j+=1
#     print("  ")


# print(merge_sort([-5,2,10,15,8,-3,5,9,2], 0, 8))

# # data=[1,2,3]
# # print(data.insert(3,4))
# # print(data)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
 
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

print(mergeSort([7,4,89,2,8,3,-1]))