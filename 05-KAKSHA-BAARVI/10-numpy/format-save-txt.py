# We aim to nicely format input.dat file
# and save it to output.dat in this script
import numpy as np
data = np.loadtxt("input.dat")
format = "%i "*15  # %i for integers
format = format+" %.4f %.4f %.4f"  # %f for floats
header = "4 Non Detached configurations\n[1-15]:id, [16-18]:Yield-Strain, Stress, Toughness"
np.savetxt(fname="output.dat", X=data, fmt=format, header=header)
