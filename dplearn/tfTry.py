import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with tf.Session() as session:
    x = tf.placeholder(tf.float32,[1],name="x")
    y = tf.placeholder(tf.float32,[1],name="y")
    z = tf.constant(1.0)
    y = x * z
    x_in = [100]
    y_output = session.run(y,{x:x_in})
    print(y_output)