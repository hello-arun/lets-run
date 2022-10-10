arr=[1,2,3,4,5,6,7]
print(f"original: {arr}")

size=len(arr)
# Divide by 2 could be inefficient here but can be very efficiently handeled by bit shifting
for i in range(size//2):
    temp = arr[i]
    arr[i] = arr[size-i-1]
    arr[size-i-1] = temp

print(f"reversed: {arr}")