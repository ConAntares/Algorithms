#### Array in Python

#%% Data

## Data Types
"""
dtype   Variants    Description
int     int8        Integers, ∈[-128,127].
        int16       Integers, ∈[32768,32767].
        int32       Integers, ∈[-2^32,2^32-1].
        int64       Integers, ∈[-2^63,2^63-1].
uint    uint8       Unsigned(non-negative) integers.
        uint16      Unsigned(non-negative) integers.
        uint32      Unsigned(non-negative) integers.
        uint64      Unsigned(non-negative) integers.
bool    bool        Boolean(True or False).
float   float16     Floating point numbers with half precision.
        float32     Floating point numbers with single precision.
        float64     Floating point numbers with double precision.
        float       Floating point numbers with double precision.
complex complex64   Complex valued floating-point numbers with half precision on each parts.
        complex128  Complex valued floating-point numbers with single precision on each parts.
        complex256  Complex valued floating-point numbers with double precision on each parts.
Note: It is not recommended that the different types ares mixed, it may reduce the performance.
"""

## Data Attribute
"""
Attribute   Description
shape       A tuple that contains the number of elements(ie., the length) for each dimension(axis) of the array.
size        The total number if elements in this array.
ndim        Number of dimensions
ntype       The data type of the elements in this array.
nbytes      Number of bytes used to store the data.
"""

import numpy as np

data = np.array([[1,1+4j],[4+9j,9+16j],[16+25j,25]],dtype=np.complex64)
data
    # array([[ 1. +0.j,  1. +4.j],
    #        [ 4. +9.j,  9.+16.j],
    #        [16.+25.j, 25. +0.j]], dtype=complex64)
np.sqrt(data)
    # array([[1.       +0.j       , 1.6004852+1.249621j ],
    #        [2.6314309+1.7100962j, 3.6984835+2.1630487j],
    #        [4.779207 +2.6154966j, 5.       +0.j       ]], dtype=complex64)
data.dtype      # dtype('complex64')
data.ndim       # 2
data.shape      # (3, 2)
data.size       # 6
data.nbytes     # 48
data.real
    # array([[ 1.,  1.],
    #        [ 4.,  9.],
    #        [16., 25.]], dtype=float32)
data.imag
    # array([[ 0.,  4.],
    #        [ 9., 16.],
    #        [25.,  0.]], dtype=float32)


#%% Summary of NumPy functions for generating arrays

"""
np.array:
    Creates an array for which the elements are given by an array-like object, which,
    for example, can be a (nested) Python list, a tuple, an iterable sequence,
    or another ndarray instance.
np.zero:
    Creates an array – with the specified dimensions and data type – that is filled with zeros.
np.ones:
    Creates an array – with the specified dimensions and data type – that is filled with ones.
np.diag:
    Creates an array with evenly spaced values between specified start, end, and, increment values.
np.linspace:
    Creates an array with evenly spaced values between specified start and end values,
    using a specified number of elements.
np.logspace:
    Creates an array with values that are logarithmically spaced between the given start and end values.
np.meshgrid:
    Generate coordinate matrices (and higher-dimensional coordinate arrays) from onedimensional coordinate vectors.
np.fromfunction:
    Create an array and fill it with values specified by a given function,
    which is evaluated for each combination of indices for the given array size.
np.fromfile:
    Create an array with the data from a binary (or text) file.
    NumPy also provides a corresponding function np.tofile with which NumPy arrays can be stored to disk,
    and later read back using np.fromfile.
np.loadtxt, np.genfromtxt:
    Creates an array from data read from a text file. For example, a comma-separated value. (CSV) file.
    The function np.genfromtxt also supports data files with missing values.
np.random.rand:
    Generates an array with random numbers that are uniformly distributed between 0 and 1.
    Other types of distributions are also available in the np.random module.
"""

import numpy as np

A = np.array([[1,2,3,4],[5,6,7,8]])
A
    # array([[1, 2, 3, 4],
    #        [5, 6, 7, 8]])
A.ndim      # 2
A.shape     # (2,4)
A.shape[0]  # 2
A.shape[1]  # 4

# Control the Print Precision, we can use: np.set_printoptions(precision=8)
# Control the Scientific Counting, we can use: np.set_printoptions(suppress=False)

#%% Arrays Filled with Constant Value

"""
    The functions np.zeros and np.ones create and return arrays filled with zeros and ones, respectively.
They take, as first argument, an integer or a tuple that describes the number of elements along each dimension of the array.
For example, to create a 2×3 array filled with zeros, and an array of length 4 filled with ones.
"""
import numpy as np

np.zeros((2,2))
    # array([[0., 0.],
    #        [0., 0.]])
np.ones((2,2))
    # array([[1., 1.],
    #        [1., 1.]])

"""
    An array filled with an arbitrary constant value can be generated by first creating an array filled with ones,
and then multiply the array with the desired fill value.
However, NumPy also provides the function np.full that does exactly this in one step.
np.full is slightly more efficient since it avoids the multiplication.
"""
x = np.empty(4)
x.fill(3.0)