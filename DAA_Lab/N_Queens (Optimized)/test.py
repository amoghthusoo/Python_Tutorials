import numpy as np

# arr = np.array([[0 for _ in range(4)] for _ in range(4)], dtype=np.int8)
arr = np.array([1, 2, 2])

print(np.where(arr == 2)[0][0])


