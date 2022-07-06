# https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

def count_triplets(arr, sum):
    arr.sort()  # First sort the array
    count = 0
    for i in range(len(arr)-2):
        j=i+1
        k=len(arr)-1
        while(k>j):
            sum_ = arr[i]+arr[j]+arr[k]
            if sum_ < sum :
                count += k-j
                j+=1
            else:
                k-=1
    return count

if __name__ == '__main__':
    arr = [5, 1, 3, 4, 7]
    sum = 12
    print(count_triplets(arr, sum))
