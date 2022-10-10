# https://www.geeksforgeeks.org/space-optimization-using-bit-manipulations/
# Let's say we want to have a dictionary/hasmap such that every key has either 0 or 1 binary values.
# For example we want to store in the memory whihc numver from 2 to 20 are divisible by either 2 or 3
# Let's try to accomplish this task 

a,b=2,34

# Direct Approach
print("# Direct Approach")
dict=[0]*(b-a+1)
for i in range(a,b+1):
    if i%2==0 or i%3==0:
        dict[i-a]=1

for i in range(a,b+1):
    if dict[i-a]==1:
        print(i,end=" ")

# Now if you closely look at this program then we can see that to store this dict hashmap we have utilized (b+a+1)*32 bits
# size saving 1/0 as integer use 32 bits(4 bytes), But can we do better... Yes definetely we can. We will see how

# We aim to utilise every bit for storing.
print("\n\n# Clever Approach")


# index >> 5 corresponds to dividing index by 32
# index & 31 corresponds to modulo operation of
# index by 32
 
# Function to check value of bit position whether
# it is zero or one
def checkbit(array, index):
    return array[index >> 5] & (1 << (index & 31))
 
# Sets value of bit for corresponding index
def setbit(array, index):
    array[index >> 5] |= (1 << (index & 31))

from math import ceil
size = b-a+1
# Size that will be used is actual_size/32 ceil is used to initialize the array with
# positive number

size = ceil(size / 32)
dict=[0]*size

for i in range(a,b+1):
    if i%2==0 or i%3==0:
        setbit(dict,i-a)
print("Encoded:",dict)
print("Decoded: ",end="")

for i in range(a, b + 1):
    if (checkbit(dict, i - a)):
        print(i, end = " ")
