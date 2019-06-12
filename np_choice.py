import numpy as np

a = [0.4,0.3,0.2,0.1]
b = [1,6,3,4]
for i in range (20):
    c= np.random.choice(b, p=a)
    print(c)