def candy(A):
    n = len(A)
    # data = (rating,index)
    data = sorted((x, i) for i, x in enumerate(A))  # sort based on rating
    candies = [1]*n
    for _,i in data:
        # Check left neighbour
        if i > 0 and A[i]>A[i-1]:
            candies[i] = candies[i-1]+1
        # Check right neighbour
        if i < n-1 and A[i]>A[i+1]:
            candies[i]= max(candies[i],candies[i+1]+1)
    return sum(candies)


if __name__ == "__main__":
    ratings=[1,2,7,4,3,3,1]
    print(candy(ratings))
    