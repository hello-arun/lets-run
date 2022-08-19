def find_majority(A:list)-> int:
    n = len(A)
    ans=0
     
    for b in range(32):
        ones = 0
        for num in A:
            if (1 << b) & num:
                ones +=1
            if ones > n//2:
                ans += 1<<b
    return ans

if __name__ == "__main__":
    A=[3,2,2,4,2,2]
    print(find_majority(A))