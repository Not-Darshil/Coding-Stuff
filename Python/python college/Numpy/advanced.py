# 11. Given a numpy array `arr = np.array([1, 2, 3, 4, 5])`, compute the square of each element without using loops. (Hint: Look into numpy's vectorized operations.)
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr**2)
# print(np.square(arr))

# 12. Create a 2D numpy array of shape (5, 7) with 1's on the diagonal and 0's elsewhere. (Hint: Consider using numpy's `diag` function.)
# import numpy as np
# arr=np.zeros((5,7),dtype=int)
# for i in range(arr.shape[0]):
#     for j in range(arr.shape[1]):
#         if i==j:
#             arr[i,j] =1
# print(arr)

# 13. Given a numpy array `arr = np.array([1, 2, 3, 4, 5])`, calculate the cumulative sum of elements. (Hint: Look into numpy's `cumsum` function.)
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
sum=np.cumsum(arr)
print(sum)

# 14. Given a 2D numpy array `arr`, swap its rows such that the first row becomes the last row and vice versa. (Hint: Think about slicing.)
# import numpy as np
# arr=np.random.randint(0,10,(5,4))
# print(arr)
# print("after swap")
# n=arr.shape[0]
# for i in range(n//2):
#     x=arr[i:i+1,:].copy()
#     y=arr[-i-1:-i-2:-1,:]
#     arr[i:i+1,:],arr[-i-1:-i-2:-1,:]=y,x
# print(arr)

# import numpy as np

# arr = np.random.randint(0, 10, (5, 4))
# print("Original array:")
# print(arr)

# print("After swapping rows:")
# n = arr.shape[0]
# for i in range(n // 2):
#     arr[i, :], arr[n-i-1, :] = arr[n-i-1, :], arr[i, :].copy()

# print(arr)


# 15. Implement the dot product of two numpy arrays without using numpy's built-in dot function. (Hint: Recall the definition of the dot product and how it can be computed using element-wise multiplication and summing.)
import numpy as np

arr1 = np.random.randint(0, 5, (3,3))
arr2 = np.random.randint(0, 5, (3,3))
print(arr1)
print(arr2)
result=0
    for i in range(np.shape(arr1)[1]):
    result+=arr1[0,i]*arr2[i,0]
print(result)
