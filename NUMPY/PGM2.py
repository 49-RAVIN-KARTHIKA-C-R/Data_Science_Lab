#Find the number rows and columns of a given matrix using numpy

import numpy as np

arr = np.array([[2,3,8],[4,5,9]])
print('Array :\n',arr)
shape=np.shape(arr)
rows,columns=arr.shape
print("no.of rows:",rows)
print("no. of columns:",columns)
