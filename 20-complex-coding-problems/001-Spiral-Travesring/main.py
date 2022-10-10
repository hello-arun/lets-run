# Define Matrix Dimensions Here
_R = 5
_C = 5

# Do not edit just run and see the output
R = _R
C = _C

cr = 0
cc = -1

dr = -1
dc = 1

# Wether pointer is moving along column or along rows
# 0 => false
# 1 => true
movingAlongColumn = 0
steps = C

while(C > 0 and R > 0):
    # print(steps)
    for i in range(steps):
        cr += dr*movingAlongColumn
        cc += dc*(1-movingAlongColumn)
        print(1+cr*_C+cc, end=" ")
    if movingAlongColumn:
        movingAlongColumn = 0
        if C > 0:
            C -= 1
            steps=C
        dc *= -1
    else:
        movingAlongColumn = 1
        if R > 0:
            R -= 1
            steps=R
        dr *= -1
