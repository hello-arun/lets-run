s = "ABACCCCCCCCBA"
k = 1
left = 0
dict = [0]*26   # Hash map for every alphabet
max_freq = 0
ans = 0
for i, c in enumerate(s):
    cc = ord(c)-65
    dict[cc] += 1
    max_freq = max(max_freq, dict[cc])
    if 1+i-left-max_freq > k:
        dict[ord(s[left])-65] -= 1
        left += 1
    ans = max(ans, i-left+1)
print(ans)