arr = [1, 4, 1, 3, 0, 7, 5, 2,8,8,9,9,9]
sorted_arr = [0]*len(arr) 
dict = [0]*10 # if data in range 0 to 9  

for val in arr:
    dict[val]+=1

for i in range(1,len(dict)):
    dict[i]+=dict[i-1]

for val in arr:
    dict[val]-=1
    sorted_arr[dict[val]]=val

print(arr)
print(sorted_arr)