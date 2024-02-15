# 1. Create a numpy array of zeros of shape (3, 4).
import numpy as np
np_array = np.zeros((3,4),dtype=int)
print(np_array)

# 2. Create a numpy array of ones of shape (2, 3).
import numpy as np
np_array=np.ones((2,3),dtype=int)
print(np_array,type(np_array))

# 3. Create a numpy array of shape (3, 3) with random integers ranging from 1 to 10.
import numpy as np
k=np.random.randint(1,10,(3,3))
print(k)

# 4.Create a numpy array containing the numbers 1 to 10.
import numpy as np
k=np.arange(10)
print(k,type(k))

# 5.Reshape the array from question 4 into a shape of (2, 5).
import numpy as np
k=np.arange(10)
print(k,type(k))
k=k.reshape(2,5)
print(k,type(k))
