import numpy as np
n = 1000000
print(n)
array1 = np.random.uniform(1, 10000, n)
array2 = np.random.uniform(1, 10000, n)
for i in range(n):
    print(array1[i],end = " ")
print()
for i in range(n):
    print(array2[i],sep = " ")