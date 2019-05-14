#### Scalar with TensorFlow in Python

import tensorflow as tf

tfs = tf.InteractiveSession()

## Constant

c1 = tf.constant(5,   name = "x")
c2 = tf.constant(6.0, name = "y")
c3 = tf.constant(7.0, tf.float64, name = "z")
c4 = tf.constant(8.0, tf.float64, name = "c")
print("c1 (x):",c1)
    # c1 (x): Tensor("x:0", shape=(), dtype=int32)
print("c2 (y):",c2)
    # c2 (y): Tensor("y:0", shape=(), dtype=float32)
print("c3 (z):",c3)
    # c3 (z): Tensor("z:0", shape=(), dtype=float64)

run = tfs.run([c1,c2,c3])
print("run([c1,c2,c3]):",run)
    # run([c1,c2,c3]): [5, 6.0, 7.0]

## Operator

op1 = tf.add(c3,c4)
op2 = tf.multiply(c3,c4)
print("op1: ",op1)
    # Tensor("Add:0", shape=(), dtype=float64)
print("op2: ",op2)
    # Tensor("Mul:0", shape=(), dtype=float64)
print("run(op1):", tfs.run(op1))
    # run(op1): 15.0
print("run(op2):", tfs.run(op2))
    # run(op2): 56.0

## Placeholder
"""
tf.placeholder(dtype, shape=None, name=None)
"""

p1 = tf.placeholder(tf.float64)
p2 = tf.placeholder(tf.float64)
print("p1:", p1)
    # p1: Tensor("Placeholder:0", dtype=float64)
print("p2:", p2)
    # Tensor("Placeholder_1:0", dtype=float64)

# Operator of Placeholders
op4 = p1 * p2
re = tfs.run(op4, {p1:3.0, p2:4.0})
print(r"tfs.run(op4, {p1:3.0, p2:4.0}):", re)
    # tfs.run(op4, {p1:3.0, p2:4.0}): 12.0

re = tfs.run(op4, feed_dict={p1:2.0, p2:5.0})
print(r"tfs.run(op4, feed_dict={p1:2.0, p2:5.0}):", re)
    # tfs.run(op4, feed_dict={p1:2.0, p2:5.0}): 10.0

re = tfs.run(op4, feed_dict={p1:[2.0,3.0,4.0], p2:[3.0,4.0,5.0]})
print(r"tfs.run(op4, feed_dict={p1:[2.0,3.0,4.0], p2:[3.0,4.0,5.0]}):", re)
    # tfs.run(op4, feed_dict={p1:[2.0,3.0,4.0], p2:[3.0,4.0,5.0]}): [ 6. 12. 20.]


## Tensors:
"""
Zero-dimensional collection:    Scalar
One-dimensional collection:     Vector
Two-dimensional collection:     Matrix
N-dimensional collection:       Tensor of rank N
"""

## TensorFlow Python API data type   Description
"""
tf.int8                           8 bit signed integer
tf.uint8                          8 bit unsigned integer
tf.qint8                          8 bit quantized signed integer
tf.quint8                         8 bit quantized unsigned integer
tf.int16                          16 bit signed integer
tf.uint16                         16 bit unsigned integer
tf.qint16                         16 bit quantized  signed integer
tf.quint16                        16 bit quantized  unsigned integer
tf.int32                          32 bit signed integer
tf.qint32                         32 bit quantized signed integer
tf.int64                          64 bit signed integer
tf.float16                        16 bit half-precision floating point
tf.float32                        32 bit single-precision floating point
tf.float64                        64 bit double-precision floating point
tf.bfloat16                       16 bit truncated floating point
tf.complex64                      64 bit single-precision complex
tf.complex128                     128 bit double-precision complex
tf.bool                           Boolean
tf.string                         String
tf.resource                       Handle to a mutable resource
"""

## Structure Tensor via 
"""
tf.convert_to_tensor()
"""

## Arithmetic Operation
"""
tf.add, tf.math.add
tf.subtract
tf.multiply
tf.scalar_mul
tf.div
tf.divide
tf.truediv
tf.floordiv
tf.realdiv
tf.truncatediv
tf.floor_div
tf.truncatemod
tf.floormod
tf.mod
tf.cross
"""

## Basic Mathematical Operations
"""
tf.add_n
tf.abs
tf.negative
tf.sign
tf.reciprocal
tf.square
tf.round
tf.sqrt
tf.rsqrt
tf.pow
tf.exp
tf.expm1
tf.log
tf.log1p
tf.ceil
tf.floor
tf.maximum
tf.minimum
tf.cos
tf.sin
tf.lbeta
tf.tan
tf.acos
tf.asin
tf.atan
tf.lgamma
tf.digamma
tf.erf
tf.erfc
tf.igamma
tf.squared_difference
tf.igammac
tf.zeta
tf.polygamma
tf.betainc
tf.rint
"""

## Matrix Mathematical Operations
"""
tf.diag
tf.diag_part
tf.trace
tf.transpose
tf.eye
tf.matrix_diag
tf.matrix_diag_part
tf.matrix_band_part
tf.matrix_set_diag
tf.matrix_transpose
tf.matmul
tf.norm
tf.matrix_determinant
tf.matrix_inverse
tf.cholesky
tf.cholesky_solve
tf.matrix_solve
tf.matrix_triangular_solve
tf.matrix_solve_ls
tf.qr
tf.self_adjoint_eig
tf.self_adjoint_eigvals
tf.svd
"""

## Tensor Mathematical Operations
"""
tf.tensordot
"""

## Complex Number Operations
"""
tf.complex 
tf.conj 
tf.imag 
tf.real
"""

## Complex Number Operations
"""
tf.string_to_hash_bucket_fast
tf.string_to_hash_bucket_strong
tf.as_string
tf.encode_base64
tf.decode_base64
tf.reduce_join
tf.string_join
tf.string_split
tf.substr
tf.string_to_hash_bucket
"""