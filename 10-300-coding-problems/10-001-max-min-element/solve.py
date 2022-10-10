
def findMinMax(array):
    # min num at index 0 and max num at index 1
    min_max=[array[0],array[0]]

    for num in array:
        if(num>min_max[1]):
            min_max[1]=num
        if(num<min_max[0]):
            min_max[0]=num
    return min_max


values=[-1,5,25,370,25,2,369,2,1,5,35,52]
print(findMinMax(values))