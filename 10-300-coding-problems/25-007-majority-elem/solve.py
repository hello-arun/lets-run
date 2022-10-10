# https://www.geeksforgeeks.org/majority-element/


def majorityElement(arr, n):
    dict = {}
    critera = n/2
    for num in arr:
        if not num in dict:
            dict[num] = 0
        dict[num] += 1
        if dict[num] > critera:
            return num
    return None


# Test 1
arr = [1, 1, 2, 1, 3, 5, 1]
n = len(arr)

# Test 2
arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
n = len(arr)

# Function calling
print(majorityElement(arr, n))
