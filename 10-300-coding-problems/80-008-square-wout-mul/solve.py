def sq(num):
    ans=0
    n2=num
    i=0
    while num:
        if num&1:
            ans+=n2<<(i)
        i+=1
        num>>=1
    return ans
# ans|=1<<(start+j+1)
for i in range(20):
    print(sq(abs(i)))
    
