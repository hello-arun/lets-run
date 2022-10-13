## List Comprehensions
https://www.hackerrank.com/challenges/list-comprehensions/problem?h_r=profile&isFullScreen=true
```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n ]
    print(arr)
```

## Find the Runner-Up Score!
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
```python
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner,runner=-101,-102
    
    for a in arr:
        if a>winner:
            winner,runner=a,winner
        if a>runner and a<winner:
            runner=a
    print(runner)
```

## Nested Lists
https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen&isFullScreen=true
```python
if __name__ == '__main__':
    lowest,secondlowest=9999,10000
    lowestN,secondlowestN=[""],[""]
    names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score==lowest:
            lowestN.append(name)
        if score==secondlowest:
            secondlowestN.append(name)
        if score<lowest:
            lowest,secondlowest=score,lowest
            secondlowestN=lowestN.copy()
            lowestN=[name]
        if score<secondlowest and score>lowest:
            secondlowest=score
            secondlowestN=[name]
    secondlowestN.sort()
    for name in secondlowestN:
        print(name)
```

## Validating phone numbers
https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
```python
import re
num=int(input())
while num:
    mobileno=input()
    valid="NO"
    if len(mobileno)==10:
        match=re.search(r'^[789]\d{9}',mobileno)
        if match:
            valid="YES"
    print(valid)
    num-=1
```

## Lists
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
```python
if __name__ == '__main__':
    N = int(input())
    arr=[]
    while N:
        args=input().split()
        arg0=args[0]
        if arg0 == "print":
            print(arr)
        elif arg0 == "sort":
            arr.sort()
        elif arg0 == "pop":
            arr.pop()
        elif arg0 == "reverse":
            arr.reverse()
        elif arg0 == "append":
            arr.append(int(args[1]))
        elif arg0 == "remove":
            arr.remove(int(args[1]))
        elif arg0 == "insert":
            arr.insert(int(args[1]),int(args[2]))
        N-=1
```
But an pythonic solution looks 
```python
lst = []
for comm, *vrs in (input().split() for i in range(int(input()))):
    if comm == "print": print(lst)
    else: getattr(lst,comm)(*map(int,vrs))
```

## Touples
https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true&page=4
```python

```

## numpy
```python
import numpy as np


if __name__ == "__main__":
    N,M = map(int,input().split())
    arr=np.array([list(map(int,input().split())) for i in range(N)])
    
    print(np.mean(arr,axis=1))
    print(np.var(arr,axis=0))
    print(round(np.std(arr,axis=None),11))

```