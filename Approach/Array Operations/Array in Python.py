#### Array in Python

### Normal Array Sentences

import numpy as np

data = np.array([[1,2+1j],[3+2j,4+3j],[5+4j,6]],dtype=np.complex64)
sqrt_data = np.sqrt(data)

print(type(data))

### Data

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

data = np.array([[1,2+1j],[3+2j,4+3j],[5+4j,6]],dtype=np.complex64)
sqrt_data = np.sqrt(data)

print("data.dtype:",data.dtype)
print("data.ndim:", data.ndim)
print("data.shape:",data.shape)
print("data.size:", data.size)
print("data.nbytes:",data.nbytes)
print(data)
print(sqrt_data)
print(sqrt_data.real)
print(sqrt_data.imag)

### Arrays Created from Lists and Other Array-like Objects

## Summary of NumPy functions for generating arrays
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

array_a = np.array([1,2,3,4])
print("This array =",array_a,"\n",
      "data.ndim =",array_a.ndim,"\n",
      "data.shape =",array_a.shape)

# To create a two-dimensional array with the same data as in the previous example, we can use a nested Python list:
array_b = np.array([[1,2],[3,4]])
print("This array = \n",array_b,"\n",
      "data.ndim =",array_b.ndim,"\n",
      "data.shape =",array_b.shape)

# Control the Print Precision, we can use: np.set_printoptions(precision=8)
# Control the Scientific Counting, we can use: np.set_printoptions(suppress=False)


### Arrays Filled with Constant Value Method 1

"""
The functions np.zeros and np.ones create and return arrays filled with zeros and ones, respectively.
They take, as first argument, an integer or a tuple that describes the number of elements along each dimension of the array.
For example, to create a 2×3 array filled with zeros, and an array of length 4 filled with ones,
we can use:
"""

import numpy as np

array_zeros = np.zeros((2,3))
array_ones = np.ones((2,3))

print("np.zeros((2,3))= \n",array_zeros)
print("np.ones((2,3)) = \n",array_ones)

array_zeros_int = np.zeros((2,3),dtype=np.int16)

print("np.ones((2,3)) = \n",array_zeros_int,"\n","dtype =",array_zeros_int.dtype)

"""
An array filled with an arbitrary constant value can be generated by first creating an array filled with ones,
and then multiply the array with the desired fill value.
However, NumPy also provides the function np.full that does exactly this in one step.
np.full is slightly more efficient since it avoids the multiplication.
"""

### Empty Array

"""
In this last example we also used the np.empty function, which generates an array with uninitialized values, of the given size.
This function should only be used when the initialization of all elements can be guaranteed by other means,
such as an explicit loop over the array elements or another explicit assignment.
"""

import numpy as np

x1 = np.empty(4)
x1.fill(3.0)
print(x1)

x2 = np.ones(4)
x2.fill(4.0)
print(x2)

x3 = np.zeros(4)
x3.fill(5.0)
print(x3)                     # np.full will make 0 × N = N.

### Arrays Filled with Incremental Sequences

"""
In numerical computing it is very common to require arrays with evenly spaced values between a start value and end value.
NumPy provides two similar functions to create such arrays: np.arange and np.linspace.
Both functions takes three arguments, where the first two arguments are the start and end values.
The third argument of np.arange is the increment, while for np.linspace it is the total number of points in the array.
"""

import numpy as np
x1 = np.arange(0.0,10,2)
x2 = np.linspace(0,11,10)
print(x1,"\n",x2)

# np.arange(start number, end number, the step value)
# np.linspace(start number, end number, the step number)

### Mesh-grid Arrays

"""
Multidimensional coordinate grids can be generated using the function np.meshgrid.
Given two onedimensional coordinate arrays (that is, arrays containing a set of coordinates along a given dimension),
we can generate two-dimensional coordinate arrays using the np.meshgrid function. An illustration of this is given in the following example:
"""

import numpy as np

x = np.array([ 1, 2, 3])
y = np.array([-4,-5,-6])
X,Y = np.meshgrid(x,y)
print("X =\n",X,"\nY =\n",Y)
print("X * Y =\n",X*Y)

# Do some computation:
Z = (X+Y)**2
print("Z = (X + Y)**2 =\n",Z)

# However, this computation of array is not the matrix computation.
# If we assume A=X*Y, then Amn = Xmn*Ymn.
A = X*Y
print("X * Y =\n",A)
B = Y*X
print("Y * X =\n",B)

"""
It is also possible to generate higher-dimensional coordinate arrays by passing more arrays as argument to the np.meshgrid function.
Alternatively, the functions np.mgrid and np.ogrid can also be used to generate coordinate arrays,
using a slightly different syntax based on indexing and slice objects.
See their docstrings or the NumPy documentation for details.
"""

### Creating Uninitialized Arrays

"""
To create an array of specific size and data type, 
but without initializing the elements in the array to any particular values, 
we can use the function np.empty.
"""

import numpy as np

a = np.empty(8,dtype=np.float64)
print(a)

"""
Here we generated a new array with three elements of type float.
There is no guarantee that the elements have any particular values, and the actual values will vary from time to time.
For this reason is it important that all values are explicitly assigned before the array is used,
otherwise unpredictable errors are likely to arise. Often the np.zeros function is a safer alternative to np.empty,
and if the performance gain is not essential it is better to use np.zeros,
to minimize the likelihood of subtle and hard to reproduce bugs due to uninitialized values in the array returned by np.empty.
"""

### Creating Matrix Arrays

"""
Matrices, or two-dimensional arrays, are an important case for numerical computing.
NumPy provides functions for generating commonly used matrices.
In particular, the function np.identity generates a square matrix with ones on the diagonal and zeros elsewhere:
"""

import numpy as np

n = 4
a = np.identity(n)
print(a)

"""
The similar function numpy.eye generates matrices with ones on a diagonal (optionally offset),
as illustrated in the following example,
which produces matrices with nonzero diagonals above and below the diagonal, respectively:
"""

a = np.eye(3,k=-1)
print("Array = ","\n",a,"\n","When k=-1")
b = np.eye(3,k=0)
print("Array = ","\n",b,"\n","When k=0")
c = np.eye(3,k=1)
print("Array = ","\n",c,"\n","When k=1")
d = np.eye(3,k=2)
print("Array = ","\n",d,"\n","When k=2")

"""
To construct a matrix with an arbitrary one-dimensional array on the diagonal,
we can use the np.diag function (which also takes the optional keyword argument k to specify an offset from the diagonal).
"""

a = np.diag(np.arange(0,20,5))
print (a)
b = np.diag(np.linspace(0,20,5))
print (b)

## Transfor number type:
"""
     int(x [,base])         into int 
     long(x [,base])        into long int  
     float(x)               into float  
     complex(real [,imag])  into complex  
     str(x)                 into str  
     repr(x)                into represent str  
     eval(str)              Calculate valid Python expression in the string, and returns an object  
     tuple(s)               into a tuple  
     list(s)                into a list  
     chr(x)                 into a char  
     unichr(x)              into a Unicode char  
     ord(x)                 into decimal system (int)
     hex(x)                 into hex system (int) 
     oct(x)                 into oct system (int)
"""

### Summary

### Scale:

import numpy as np

print('\n Scale in NumPy:')
ћ = 1.0545726663
print('ћ:',ћ)

### Vector

import numpy as np

print('\n Vector in NumPy:')
υ = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(υ)
print("υ.dtype:", υ.dtype)
print("υ.ndim:",  υ.ndim)
print("υ.shape:", υ.shape)
print("υ.size:",  υ.size)
print("υ.nbytes:",υ.nbytes)
κ = np.arange(0.0,10,2)
print('np.arange(0.0,10,2):',κ)
η = np.linspace(0,10,6)
print('np.linspace(0,10,6):',η)

### Matrix

import numpy as np

print('\n Matrix in NumPy:')
μ = np.array([[0.0,0.1,0.2,0.3,0.4],
              [1.0,1.1,1.2,1.3,1.4],
              [2.0,2.1,2.2,2.3,2.4]])
print(μ)
print("μ.dtype:", μ.dtype)
print("μ.ndim:",  μ.ndim)
print("μ.shape:", μ.shape)
print("μ.size:",  μ.size)
print("μ.nbytes:",μ.nbytes)
u = np.array([0.0, 0.1, 0.2])
b = np.array([1.0, 1.1, 1.2])
U,B = np.meshgrid(u,b)
print(U)
print(B)
n = 4
a = np.identity(n)
print('np.identity(n)=\n',a)
a = np.eye(3,k=-1)
print("When k=-1, Array = ","\n",a)
b = np.eye(3,k=0)
print("When k=0, Array = ","\n",b)
c = np.eye(3,k=1)
print("When k=1, Array = ","\n",c)
d = np.eye(3,k=2)
print("When k=2, Array = ","\n",d)
a = np.diag(np.arange(0,20,2))
print('np.diag(np.arange(0,20,2))=\n',a)
b = np.diag(np.linspace(0,20,5))
print('np.diag(np.linspace(0,20,5))=\n',b)


### Tensor:

import numpy as np

print('\n Tensor in NumPy:')
T = np.array([[[0.00,0.01,0.02,0.03],[0.10,0.11,0.12,0.13],[0.20,0.21,0.22,0.23]],
              [[1.00,1.01,1.02,1.03],[1.10,1.11,1.12,1.13],[1.20,0.21,0.22,0.23]]])
print(T)
print("T.dtype:", T.dtype)
print("T.ndim:",  T.ndim)
print("T.shape:", T.shape)
print("T.size:",  T.size)
print("T.nbytes:",T.nbytes)