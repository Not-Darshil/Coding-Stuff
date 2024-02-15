# 6. Create a 5x5 identity matrix using numpy.
import numpy as np
array=np.zeros((5,5),dtype=int)
for i in range(0,array.shape[0]):
    for j in range(0,array.shape[1]):
        if i==j:
            array[i,j]=1
print(array)

# 7.Given two numpy arrays arr1 = np.array([1, 2, 3]) and arr2 = np.array([4, 5, 6]), concatenate them horizontally.
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr3)

# 8. Given a numpy array `arr = np.array([1, 2, 3, 4, 5])`, reverse the array.
import numpy as np
arr = np.array([1, 2, 3, 4, 5,6])
arr2=arr[::-1]
print(arr2)

# arr3=np.array([],dtype=int)
# for i in range(len(arr)-1,-1,-1):
#     arr3=np.append(arr3,arr[i])
# print(arr3)

# n = len(arr)
# for i in range(n // 2):
#     arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
# print(arr)


# 9.Create a numpy array with 10 equally spaced values between 0 and 1.
import numpy as np
k=np.linspace(0,1,10)
print(k)

# 10.Given a numpy array arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), extract all odd numbers from the array.
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2=arr[arr%2!=0]
print(arr2)