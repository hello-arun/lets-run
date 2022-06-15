# https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
# Python3 program to print all elements
# of given matrix:
#   1   2   3   4 
#   5   6   7   8 
#   9  10  11  12
#  13  14  15  16
#  17  18  19  20
# in diagonal order as: 
# 1
# 5 2
# 9 6 3
# 13 10 7 4
# 17 14 11 8
# 18 15 12
# 19 16
# 20

def valid_index(i,j):

    return i>=0 and j>=0 and i<r and j < c

def print_diag():
    i,j=0,0
    while(True):
        ii,jj=i,j
        while(valid_index(ii,jj)):
            print(f"{val(ii,jj):3}",end=" ")
            ii-=1
            jj+=1
        if valid_index(i+1,j):
            i+=1
        elif valid_index(i,j+1):
            j+=1
        else:
            break
        print()

def val(i,j):
    # return value of 2Darray at index i,j
    return 1+i*c+j

def print_direct():
    for i in range(r):
        for j in range(c):
            print(f"{val(i,j):3}",end=" ")
        print("")

r = 5
c = 4
print("Direct Print:")
print_direct()
print("\nDiagnl Print:")
print_diag()