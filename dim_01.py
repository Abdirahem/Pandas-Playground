import numpy as np

d1 = np.array([12,34,55])
print(d1[2])
print(d1.ndim,"D")

d2 = np.array([[12,23,43],
               [34,45,56]])
print(d2[1,0])
print(d2.ndim,"D")

d3 = np.array([[[12,34,56],
                [23,45,67]],
                [[11,22,33],
                [0,0,0]]])
print(d3[0,1,1])
print(d3.ndim,"D")