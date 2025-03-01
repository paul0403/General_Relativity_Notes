import numpy as np
import matplotlib.pyplot as plt

# NOTE: this script uses c = 1 as speed of light
E = 10  # energy
G = 1   # Newton's gravitational constant
m = 1   # black hole mass
rmax = 10  # infalling particle starts at r = 10
print("Black hole mass is ", m, ", infalling particle energy is ", E)
print("Horizon is at r = ", 2*m*G)
print("Infalling particle starts at r = ", rmax)


def rdot(r):
    return np.sqrt((1-2*m*G/r)**2 - (m**2) * ((1-2*m*G/r)**3) / (E**2))

def integrate(r):
    # returns the time it takes for particle to fall to r from rmax
    if r >= rmax:
        print("Need to fall to a place with r < rmax!")
        return 0
    
    numofgridpoints = 300
    grid = np.linspace(r, rmax, numofgridpoints)
    gridlength = (rmax - r) / numofgridpoints
    accum = 0
    for i in range(0, len(grid), 1):
        accum += gridlength / rdot(grid[i])
    return accum 
    
window_rightlim = 9
window_uplim = 50
r_array = np.linspace(2, window_rightlim, 1000)
# rdot_array = np.zeros(len(r_array))
# for i in range(0, len(rdot_array), 1):
#     rdot_array[i] = rdot(r_array[i])
# plt.plot(r_array, rdot_array)

# rdot_inv_array = np.zeros(len(r_array))
# for i in range(0, len(rdot_inv_array), 1):
#     rdot_inv_array[i] = 1/rdot(r_array[i])
# plt.plot(r_array, rdot_inv_array)

t_array = np.zeros(len(r_array))
for i in range(0, len(t_array), 1):
    t_array[i] = integrate(r_array[i])
plt.plot(r_array, t_array, 'r')
plt.axvline(x=2*m*G)
plt.xlabel('r')
plt.ylabel('t')
plt.xlim([1.5, window_rightlim])
plt.ylim([0, window_uplim])

