#5.Find the code to demonstrate matrix add,substract, and division

import numpy as np
arr=np.array([[1,2],[4,6]])
arr1=np.array([[4,6],[2,4]])
print('First array:\n',arr)
print('Second array:\n',arr1)

add=np.add(arr,arr1)
print('Addition of two matrix:\n',add)

subtract=np.subtract(arr,arr1)
print('Subtraction of two matrix:\n',subtract)

div=np.divide(arr,arr1)
print('Division of two matrix:\n',div)
