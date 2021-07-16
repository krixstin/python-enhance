import numpy as np

test_array = np.array([1,4,5,6], float)

#to save memory storage
np.array([1,2,3,4], np.float32) 

# tuple type 
print(test_array.shape)

print(test_array.dtype) 

matrix = [[1,1,2,2],
        [3,4,5,6]
        ,[8,8,9,9],]

print(np.array(matrix, int).shape)
m = np.array(matrix, int)
print(m.reshape(-1,6))

np.arange(30)