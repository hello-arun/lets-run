
chocklates = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
students = 7

chocklates.sort() # Most unefficient part of the array but can't find another approach
# print(chocklates)
min_diff=chocklates[students-1]-chocklates[0]
for i in range(1+len(chocklates)-students):
    c_diff=chocklates[i+students-1]-chocklates[i]
    # print(f"min {chocklates[i]}, max {chocklates[i+students-1]}, diff {c_diff}")
    if c_diff<min_diff:
        min_diff=c_diff 
print(min_diff)

