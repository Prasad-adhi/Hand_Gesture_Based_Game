import numpy as np
grid=np.zeros([40,70],dtype=int)
grid[:,0]=100
grid[:,69]=-100
grid[0,:]=2
grid[39,:]=2
grid=np.transpose(grid)
grid[60,20:24]=1
grid[20,35]=5
print(len(grid[0]))
