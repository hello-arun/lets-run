arr = [2, 7, 6, 1, 4, 5]
mod_arr = {}
k = 3
mod = 0
max_len = 0
for i, num in enumerate(arr):
    mod = ((mod+num) % k + k) % k
    if (mod==0):
        max_len=i+1
    else:
        if mod not in mod_arr:
            mod_arr[mod] = mod
        else:
            max_len = max(max_len,i-mod_arr[mod])
print(max_len)