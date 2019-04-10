#### Array in Python

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

#%%
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

## Summary of NumPy functions for generating arrays
"""
np.array:
    Creates an array for which the elements are given by an array-like object, which,
    for example, can be a (nested) Python list, a tuple, an iterable sequence,
    or another ndarray instance.
np.zeros:
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

#%%
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

## Arrays Filled with Constant Value
"""
    The functions np.zeros and np.ones create and return arrays filled with zeros and ones, respectively.
They take, as first argument, an integer or a tuple that describes the number of elements along each dimension of the array.
For example, to create a 2×3 array filled with zeros, and an array of length 4 filled with ones.
"""
#%%
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
x1 = np.empty(4)
x1.fill(4.0)
x1
    # array([3., 3., 3., 3.])

"""
    In this last example we also used the np.empty function, which generates an array with uninitialized values, of the given size.
This function should only be used when the initialization of all elements can be guaranteed by other means,
such as an explicit loop over the array elements or another explicit assignment.
"""

x2 = np.ones(4)
x2.fill(4.0)
x2      # array([4., 4., 4., 4.])

x3 = np.zeros(4)
x3.fill(5.0)
x3      # array([5., 5., 5., 5.])

## Arrays Filled with Incremental Sequences
"""
    In numerical computing it is very common to require arrays with evenly spaced values between a start value and end value.
NumPy provides two similar functions to create such arrays: np.arange and np.linspace.
Both functions takes three arguments, where the first two arguments are the start and end values.
The third argument of np.arange is the increment, while for np.linspace it is the total number of points in the array.
"""

import numpy as np

x1 = np.arange(0.0,10,2)
x2 = np.linspace(0,10,6)
x1      # array([0., 2., 4., 6., 8.])
x2      # array([0., 2., 4., 6., 8., 10.])

# np.arange(start number, end number, the step value)
# np.linspace(start number, end number, the step number)

## Mesh-grid Arrays
"""
#     Multidimensional coordinate grids can be generated using the function np.meshgrid.
# Given two onedimensional coordinate arrays (that is, arrays containing a set of coordinates along a given dimension),
# we can generate two-dimensional coordinate arrays using the np.meshgrid function. An illustration of this is given in the following example:
"""
#%%
import numpy as np

x = np.array([ 1, 2, 3])
y = np.array([-4,-5,-6])
X,Y = np.meshgrid(x,y)

x   # array([1, 2, 3])
y   # array([-4, -5, -6])
X
    # array([[1, 2, 3],
    #        [1, 2, 3],
    #        [1, 2, 3]])
Y
    # array([[-4, -4, -4],
    #        [-5, -5, -5],
    #        [-6, -6, -6]])
X*Y
    # array([[ -4,  -8, -12],
    #        [ -5, -10, -15],
    #        [ -6, -12, -18]])

"""
    It is also possible to generate higher-dimensional coordinate arrays by passing more arrays as argument to the np.meshgrid function.
Alternatively, the functions np.mgrid and np.ogrid can also be used to generate coordinate arrays,
using a slightly different syntax based on indexing and slice objects.
See their docstrings or the NumPy documentation for details.
"""

## Creating Uninitialized Arrays
"""
    To create an array of specific size and data type, 
but without initializing the elements in the array to any particular values, 
we can use the function np.empty.
"""
import numpy as np

a = np.empty(8,dtype=np.float64)
a
    # array([2.68383415e-316, 0.00000000e+000, 0.00000000e+000, 0.00000000e+000,
    #        0.00000000e+000, 0.00000000e+000, 7.51109446e+242, 2.13508962e+137])
#     Here we generated a new array with three elements of type float.

"""
There is no guarantee that the elements have any particular values, and the actual values will vary from time to time.
For this reason is it important that all values are explicitly assigned before the array is used,
otherwise unpredictable errors are likely to arise. Often the np.zeros function is a safer alternative to np.empty,
and if the performance gain is not essential it is better to use np.zeros,
to minimize the likelihood of subtle and hard to reproduce bugs due to uninitialized values in the array returned by np.empty.
"""

## Creating Matrix Arrays
"""
    Matrices, or two-dimensional arrays, are an important case for numerical computing.
NumPy provides functions for generating commonly used matrices.
In particular, the function np.identity generates a square matrix with ones on the diagonal and zeros elsewhere:
"""
import numpy as np

n = 4
a = np.identity(n)
a
    # array([[1., 0., 0., 0.],
    #        [0., 1., 0., 0.],
    #        [0., 0., 1., 0.],
    #        [0., 0., 0., 1.]])
a = np.eye(3,k=-1)
a
    # array([[0., 0., 0.],
    #        [1., 0., 0.],
    #        [0., 1., 0.]])
b = np.eye(3,k=0)
b
    # array([[1., 0., 0.],
    #        [0., 1., 0.],
    #        [0., 0., 1.]])
c = np.eye(3,k=1)
c
    # array([[0., 1., 0.],
    #        [0., 0., 1.],
    #        [0., 0., 0.]])
d = np.eye(3,k=2)
d
    # array([[0., 0., 1.],
    #        [0., 0., 0.],
    #        [0., 0., 0.]])
a = np.diag(np.arange(0,20,5))
a
    # array([[ 0,  0,  0,  0],
    #        [ 0,  5,  0,  0],
    #        [ 0,  0, 10,  0],
    #        [ 0,  0,  0, 15]])
b = np.diag(np.linspace(0,20,5))
b
    # array([[ 0.,  0.,  0.,  0.,  0.],
    #        [ 0.,  5.,  0.,  0.,  0.],
    #        [ 0.,  0., 10.,  0.,  0.],
    #        [ 0.,  0.,  0., 15.,  0.],
    #        [ 0.,  0.,  0.,  0., 20.]])

# Transfor number type:
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

## Summary
# Scale:
#%%
import numpy as np

ћ = 1.0545726663
ћ           # 1.0545726663

# Vector:
#%%
import numpy as np

υ = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
υ           # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
υ.dtype     # dtype('int64')
υ.ndim      # 1
υ.shape     # (10,)
υ.size      # 10
υ.nbytes    # 80
κ = np.arange(0.0,10,2)
κ           # array([0., 2., 4., 6., 8.])
η = np.linspace(0,10,6)
η           # array([ 0.,  2.,  4.,  6.,  8., 10.])

# Matrix:
#%%
import numpy as np

μ = np.array([[0.0,0.1,0.2,0.3,0.4],
              [1.0,1.1,1.2,1.3,1.4],
              [2.0,2.1,2.2,2.3,2.4]])
μ
    # array([[0. , 0.1, 0.2, 0.3, 0.4],
    #        [1. , 1.1, 1.2, 1.3, 1.4],
    #        [2. , 2.1, 2.2, 2.3, 2.4]])
μ.dtype     # dtype('float64')
μ.ndim      # 2
μ.shape     # (3, 5)
μ.size      # 15
μ.nbytes    # 120

# Tensor:
#%%
import numpy as np

T = np.array([[[0.00,0.01,0.02,0.03],[0.10,0.11,0.12,0.13],[0.20,0.21,0.22,0.23]],
              [[1.00,1.01,1.02,1.03],[1.10,1.11,1.12,1.13],[1.20,0.21,0.22,0.23]]])
T
    # array([[[0.  , 0.01, 0.02, 0.03],
    #         [0.1 , 0.11, 0.12, 0.13],
    #         [0.2 , 0.21, 0.22, 0.23]],
    #        [[1.  , 1.01, 1.02, 1.03],
    #         [1.1 , 1.11, 1.12, 1.13],
    #         [1.2 , 0.21, 0.22, 0.23]]])
T.dtype     # dtype('float64')
T.ndim      # 3
T.shape     # (2, 3, 4)
T.size      # 24
T.nbytes    # 192

## Array Indexing and Slicing
# Indexing and Slicing
"""
  Elements and subarrays of NumPy arrays are accessed using the standard square bracket notation that is also used with for example Python lists.
Within the square bracket, a variety of different index formats are used for different types of element selection.
In general, the expression within the bracket is a tuple,
where each item in the tuple is a specification of which elements to select from each axis (dimension) of the array.
"""

# One-dimensional Arrays
"""
  Along a single axis, integers are used to select single elements, 
and so-called slices are used to select ranges and sequences of elements. 
Positive integers are used to index elements from the beginning of the array(index starts at 0), 
and negative integers are used to index elements from the end of the array, 
where the last element is indexed with -1, the second-to-last element with -2, and so on.
  Slices are specified using the: notation that is also used for Python lists. 
In this notation, a range of elements can be selected using an expressions like m:n, 
which selects elements starting with m and ending with n−1 (note that the nth element is not included). 
The slice m:n can also be written more explicitly as m:n:1, 
where the number 1 specifies that every element between m and n should be selected. 
To select every second element between m and n, use m:n:2, and to select every p element, use m:n:p, and so on. 
If p is negative, elements are returned in reversed order starting from m to n+1,
which implies that m has be larger than n in this case. 
"""

# Examples of Array Indexing and Slicing Expression
"""
  Expression      Description
  a[ m]           Select element at index m, where m is an integer, with counting from 0. 
  a[-m]           Select the m th element from the end of list, where m is an integer.
                  The last element in the list is addressed as -1.
  a[m:n]          Select element with index starting at m and ending at n-1, where both m and n are integer.
  a[:], a[0:-1]   Select all elements in the given axis.
  a[m:],a[m:01]   Select elements starting with index m and going up to the last.
  a[:n]           Select elements starting with index 0 and going to index n-1.
  a[m:n:p]        Select elements with index m through n(exclusive), with increment p.
  a[::-1]         Select all the elements, in reverse order.
"""

#%%
import numpy as np
a = np.arange(0,11,1)       # Contains a sequence of integers between 0 and 10.
print ("a =",a)
print ("The first element a[0] is",a[0])
print ("The last element a[-1] is",a[-1])
print ("The 5th number, at index 4 is",a[4])
print ("The second to the last: ",a[1:-1])
print ("The second to the last with increment 2:",a[1:-1:2])
print ("The first five element",a[:5])
print ("The last five elements",a[-5:])
print ("The reversed array with slice -1", a[::-1])
print ("The reversed array with slice -2", a[::-2])

## Reshaping and Resizing
"""
When working with data in array form, it is often useful to rearrange arrays and alter the way they are interpreted. 
For example, an N*N matrix array could be rearranged into a vector of length N^2, 
or a set of one-dimensional arrays could be concatenated together, or stacked next to each other to form a matrix. 
NumPy provides a rich set of functions of this type of manipulation. 
See this Table for a summary of a selection of these functions.
"""

"""
# Array[a:b,c:d]
    The matrix from (a,c) to (b-1,d-1)
    Array[[a,b],[c,d]]
    The elements: (a,c) and (b,d)
"""

"""
# Array
    [0,0]   [0,1]   [0,2]   [0,3]
    [1,0]   [1,1]   [1,2]   [1,3]
    [2,0]   [2,1]   [2,2]   [2,3]
    [3,0]   [3,1]   [3,2]   [3,3]


# data[0]
    [0,0]   [0,1]   [0,2]   [0,3]




# data[1,:]

    [1,0]   [1,1]   [1,2]   [1,3]



# data[:,1]
            [0,1]
            [1,1]
            [2,1]
            [3,1]

# data[0:2,0:2]
    [0,0]   [0,1]
    [1,0]   [1,1]



# data[0:2,2:4]
                    [0,2]   [0,3]
                    [1,2]   [1,3]



# data[::2,::2]
    [0,0]           [0,2]

    [2,0]           [2,2]


# data[1::2,1::2]

            [1,1]           [1,3]

            [3,1]           [3,3]

# data[:,[0,3]]
    [0,0]                   [0,3]
    [1,0]                   [1,3]
    [2,0]                   [2,3]
    [3,0]                   [3,3]

# data[[1,3],[0,3]]

    [1,0]

                            [3,3]

# data
    [0,0]   [0,1]   [0,2]   [0,3]
    [1,0]   [1,1]   [1,2]   [1,3]
    [2,0]   [2,1]   [2,2]   [2,3]
    [3,0]   [3,1]   [3,2]   [3,3]

# data[:,np.array[[False,True,True,False]]]
            [0,1]   [0,2]
            [1,1]   [1,2]
            [2,1]   [2,2]
            [3,1]   [3,2]

# data[1:3,np.array[[False,True,True,False]]]
    [0,0]   [0,1]   [0,2]   [0,3]
    [1,0]   [1,1]   [1,2]   [1,3]
    [2,0]   [2,1]   [2,2]   [2,3]
    [3,0]   [3,1]   [3,2]   [3,3]
"""

# Summary of NumPy functions for manipulating the dimensions and the shape of arrays
"""
np.reshape, np.ndarray.reshape: 
    Reshape an N-Dimensional array. The total number of elements must remain the same.
np.ndarray.flatten:
    Create a copy of an N-Dimensional array and reinterpret it as a One-Dimensional array, that is all dimensions are collapsed into one.
np.ravel, np.ndarray,ravel:
    Create a view (if possible, otherwise a copy) of an N-dimensional array in which it is interpreted as a One-Dimensional array.
np.squeeze:
    Remove axes with length 1.
np.expand_dims, np.newaxis:
    Adds a new axis (dimension) of length 1 to an array, where np.newaxis is used with array indexing.
np.transpose, np.ndarray.transpose, np.ndarray.T:
    Transpose the array. The transpose operation corresponds to reversing (or more generally, permuting) the axes of the array.
np.vstack:
    Stack a list of arrays vertically (along axis 0): For example, given a list of row vectors, append the rows to form a matrix.
np.hstack:
    Stack a list of arrays horizontally (along axis 1): For example, given a list of column vectors, append the columns to form a matrix.
np.dstack:
    Stack arrays depth-wise (along axis 2).
np.concatenate:
    Create a new array by appending arrays after each other, along a given axis.
np.resize:
    Resize an array. Creates a new copy of the original array, with the requested size. 
    If necessary, the original array will repeated to fill up the new array.
np.append:
    Append an element to an array. Creates a new copy of the array.
np.insert:
    Insert a new element at a given position. Creates a new copy of the array.
np.delete:
    Delete an element at a given position. Creates a new copy of the array.

Reshaping an array does not require modifying the underlying array data; it only changes in how the data is interpreted, 
by redefining the array’s strides attribute. An example of this type of operation is a 2*2 array (matrix) that is reinterpreted as a 1*4 array (vector). 
In NumPy, the function np.reshape, or the ndarray class method reshape, can be used to reconfigure how the underlying data is interpreted. 
"""

# Example
import numpy as np

α = np.array([[1,2],
              [3,4]])
β = np.arange(0,5)
γ = np.arange(1,6)

Reshape = np.reshape(α,(1,4))
α
    # array([[1, 2],
    #        [3, 4]])
Reshape
    # array([[1, 2, 3, 4]])
α.reshape(4)
    # array([1, 2, 3, 4])
α.reshape(1,4)
    # array([[1, 2, 3, 4]])
α.reshape(2,2)
    # array([[1, 2],
    #        [3, 4]])
α.reshape(4,1)
    # array([[1],
    #        [2],
    #        [3],
    #        [4]])
α.reshape(4,1,1)    # Generate 4*1*1 array
    # array([[[1]],
    #        [[2]],
    #        [[3]],
    #        [[4]]])
α.reshape(2,2,1)     # Generate 2*2*1 array
    # array([[[1],
    #         [2]],
    #        [[3],
    #         [4]]])
α.reshape(2,1,2)     # Generate 2*1*2 array
    # array([[[1, 2]],
    #        [[3, 4]]])
α.reshape(1,2,2)     # Generate 1*2*2 array
    # array([[[1, 2],
    #         [3, 4]]])
α.reshape(1,1,4)     # Generate 1*1*4 array
    # array([[[1, 2, 3, 4]]])
np.ndarray.flatten(α)
    # array([1, 2, 3, 4])
β   
    # array([0, 1, 2, 3, 4])
column = β[:,np.newaxis]
column
    # array([[0],
    #        [1],
    #        [2],
    #        [3],
    #        [4]])
row = β[np.newaxis,:]
row
    # array([[0, 1, 2, 3, 4]])
γ
    # array([1, 2, 3, 4, 5])
np.vstack((β,β,β))
    # array([[0, 1, 2, 3, 4],
    #        [0, 1, 2, 3, 4],
    #        [0, 1, 2, 3, 4]])
np.vstack((γ,γ,γ))
    # array([[1, 2, 3, 4, 5],
    #        [1, 2, 3, 4, 5],
    #        [1, 2, 3, 4, 5]])
np.hstack((β,β,β))
    # array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4])
np.hstack((γ,γ,γ))
    # array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
np.vstack((row,row,row))
    # array([[0, 1, 2, 3, 4],
    #        [0, 1, 2, 3, 4],
    #        [0, 1, 2, 3, 4]])
np.hstack((column,column,column))
    # array([[0, 0, 0],
    #        [1, 1, 1],
    #        [2, 2, 2],
    #        [3, 3, 3],
    #        [4, 4, 4]])