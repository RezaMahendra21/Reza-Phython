import numpy as np
import os

os.system("clear")

lista = [1,2,3,4]
vectorA = np.array([1,2,3,4])
print(vectorA**2)
verctorB = np.array([(1,2), (3,4)])
print(verctorB*3)

zeros_c = np.zeros((3,2))
# zeros_c = np.zeros((3,3))
print(zeros_c)

ones = np.ones((2,2))

print(f"hasil : {verctorB + ones}")