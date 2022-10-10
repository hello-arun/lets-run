# Using binary search in the sorted array is very efficient
# but can we utilise power of binary search in the pivot array?
# I think that i need to find the pivot point in first place
# then i can utilise power of binary search in two diffetent
# parts

arr = [5, 6, 7, 8, 9, 10, 1, 1, 3]
key = 3
print(arr)
# finding the pivot index
def find_pivot(arr):
    l,r=0,len(arr)-1
    while(l<r):
        mid=(r+l)//2
        if (r==l+1):
            return r
        if arr[mid]>arr[r]:
            l=mid+1
        else:
            r=mid

# binary search based on left and right index
def bin_search(arr,element,l,r):
    while l <= r:
        mid = (r+l) // 2
 
        # if element at mid
        if arr[mid] == element:
            return mid 
        # If element is greater, ignore left half
        elif arr[mid] < element:
            l = mid + 1 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
    return None

pivot=find_pivot(arr)
print("pivot index",pivot)
index = bin_search(arr,key,0,pivot-1) 
if index is not None:
    print("found at",index)
else:
    index = bin_search(arr,key,pivot,len(arr)-1)
    if index is not None:
        print("found at",index)
    else:
        print("Not exists")