
def bin_search(arr, key):
    l, r = 0, len(arr)-1
    while (l <= r):
        mid = (l+r)//2
        # check if mid element is the key
        if (arr[mid] == key):
            return mid
        # if we reached so far then mid element is useless to us; we will discard it
        # Now we know that at least one of left/right subarr will be sorted
        # lets check if left subarr is sorted
        if arr[l] <= arr[mid]:
            # if we reached so far we know that we are in the sorted subarr
            # We check if key can be found in left subarr
            if key < arr[mid] and key >= arr[l]:
                r = mid-1
            # if given key is out of range of this left subarr switch to right subarr
            else:
                l = mid+1
        # if left arr is not sorted then right subarr will defineltely be
        else:
            # We check if key can be found in right subarr
            if key <= arr[r] and key > arr[mid]:
                l = mid+1
            # if given key is out of range of this right subarr switch to left subarr
            else:
                r = mid-1
    # if we cant find anything so far, user is useless
    return -1


if __name__ == "__main__":
    arr = [3,1]
    key = 1
    index = bin_search(arr, key)
    print(f"index of {key} in given arr is {index}")
