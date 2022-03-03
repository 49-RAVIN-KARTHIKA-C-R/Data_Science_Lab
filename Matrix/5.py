import numpy as np

Matrix1 = np.array([[1, 3, 4], [3, 6, 2], [5, 2, 4]])
Matrix2 = np.array([[2, 2, 3], [3, 2, 1], [1, 2, 6]])
print("Matrix after addition: ", Matrix1 + Matrix2)
print("Matrix after subtraction: ", Matrix1 + Matrix2)
print("Matrix after multiplication: ", np.matmul(Matrix1, Matrix2))
print("Matrix after division: ", np.divide(Matrix1, Matrix2))
