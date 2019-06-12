import numpy as np

a = np.array([[1],[2],[3],[4],[5],[6]])
b = np.array([[[0,1,0,1,0,0]],[[0,1,0,1,5,0]]])
c = np.array([[[1,0,1,0,1,1]], [[1],[2],[3],[4],[5]]])


out = list(zip(b, c))
for i in out[::-1]:
    print(i)