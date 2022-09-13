import numpy as np

np.random.seed(2)
a=np.random.random((5,5))*1000
a[0,0]=0.00006
# Print without format
print("Without format\n",a,"\n")

# Temporarily format with supression 
with np.printoptions(precision=3, suppress=True):
    print("Temporary format with supression \n",a,"\n")

# Temporarily format without supression 
with np.printoptions(precision=3, suppress=False):
    print("Temporary format without supression \n",a,"\n")

# Manual format

print("Manual Formatting 10.3f with end=\"\"")
for x in a:
    for i in x:
        print(f"{i:10.3f}",end="")
    print("")

print("\nManual Formatting 08.3f with end=\" \"")
for x in a:
    for i in x:
        print(f"{i:08.3f}",end=" ")
    print("")