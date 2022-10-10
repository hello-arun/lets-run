from turtle import color
import matplotlib.pyplot as plt
import random
from quick_union_weighted import quick_union_wighted
random.seed(3)

N = 20  # No of rows
M = 20  # No of cols
random_samples = random.sample(range(0, N*M), N*M)
fig, [ax1,ax2] = plt.subplots(1,2)
ax2.set_xlim([-0.1,1.1])
ax2.set_ylim([-0.1,1.1])

probs = [i/20.0 for i in range(0,20)]  # probablity of a grid grid element to be one
for prob in probs:
    # Create NxM grid with all element 0
    grid = [[0]*M for _ in range(N)]
    # print("Grid Initialisation:", grid)

    # Change some ones to zeros based on prob
    total_ones = int(N*M*prob)
    samples = random_samples[0:total_ones]
    #sample(range(0, N*M), total_ones)
    samples.sort()
    for pos in samples:
        row = pos//M
        col = pos % M
        grid[row][col] = 1

    # print("Grid substituted:", grid)

    root_node= -1
    root_node_bot = -2
    canPercolates=True
    if (len(samples)>0 and samples[0]//M == 0):
        root_node = samples[0]
    else:
        canPercolates=False

    if(canPercolates):
        quf = quick_union_wighted(N*M)
        for pos in samples:
            row = pos//M
            col = pos % M
            grid[row][col] = 1

        # Assign the same node to the first row
        for i in range(M):
            if(grid[0][i]==1):
                quf.union(i,root_node)

        canPercolates=False
        for pos in samples:
            row,col = pos//M, pos % M
            if(row==0):
                quf.union(i,root_node)
            else:
                if(grid[row-1][col]):
                    quf.union(pos,(row-1)*N+col)
                if(grid[row][col-1] and col-1 >=0):
                    quf.union(pos,row*N+col-1)
            if(row==N-1):
                if(quf.connected(pos,root_node)):
                    canPercolates=True
                    break
        print(canPercolates)
    # Display grid
    ax1.imshow(grid)
    ax1.set_title(f"{N}x{M}, Prob: {prob:0.2f}, {canPercolates}")
    ax2.plot([prob],[canPercolates],".k")
    fig.tight_layout()
    fig.savefig(f"./out/{N}x{M}-Prob-{prob:0.2f}.png")