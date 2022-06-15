def print_combination(arr,r):
    data = [0]*r # To temperory store a single combination
    combination_util(arr,r,data,0,0)

def combination_util(arr,r,data,i,index):
    # r => size of combination
    # i => current index in the original arr
    # index => current index in the temp data array
    if index == r:
        print(data)
        return
    
    if i >= len(arr):
        return 

    data[index] = arr[i]

    combination_util(arr,r,data,i+1,index+1)    
    combination_util(arr,r,data,i+1,index)

arr = [2,3,4,5,6]
size = 3
print_combination(arr,size)