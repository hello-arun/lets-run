## Count Palindromic Subsequences
https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/

We aim to solve it via recursion, dynamic programming  
Understanding Recursive algorithm is the best part here  
```
count[i,j] = #palindromic subseqs from index i to jth both included
```
if i==j; count = 1 , otherwise  
We can think that  
```
count[i,j] = count[i+1,j] + count[i,j-1] + some correction term
```
We need to know this correction term  
### if s[i]!=s[j]  
In this case we know for sure we are couting [i+1,j-1] two times so we just remove that  
So expression become  
```
count[i,j]=count[i+1,j] + count[i,j-1] -count[i+1,j-1]
```
### When s[i]==s[j]=x:some char  
In this Let P is a palim that strictly belongs to [i+1,j-1]. Then xPx will also be a valid palindrom  
So this time doubl counting is necessary here becuase P and xPx are two different sets of palindroms.  
In addition, an extra palim 'xx' should be added to the list   
So expression become  
```
count[i,j]=count[i+1,j] + count[i,j-1] + 1  
```
