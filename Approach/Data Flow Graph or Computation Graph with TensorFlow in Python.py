#### Data Flow Graph or Computation Graph

import tensorflow as tf

tfs = tf.InteractiveSession()

## We can get explicit access to the default graph using the following command:
"""
graph = tf.get_default_graph()
"""

## For example y = x1 + x2 + x3
"""
tf.add(x1 + x2 + x3)
"""

## Calculate Linear Model y = w×x + b

w = tf.Variable([0.3], tf.float32)          # Define model parameter: w
b = tf.Variable([-.3], tf.float32)          # Define model parameter: b
x = tf.placeholder(tf.float32)              # Define model input and output
y = w * x + b
output = 0
with tf.Session() as tfs:
    tf.global_variables_initializer().run() # Initialize
    output = tfs.run(y, {x:[1,2,3,4]})      # Print the variable y
print('output : ',output)
    # output :  [0.         0.3        0.6        0.90000004]


## Executing Graphs Across Compute Devices - CPU and GPU
"""
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
"""