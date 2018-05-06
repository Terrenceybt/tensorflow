#! /usr/bin/env pyton

import tensorflow as tf

with tf.Graph().as_default():
    scalar = tf.zeros([])
    
    vector = tf.zeros([3])

    matrix = tf.zeros([2, 3])
    
    
    a = tf.constant([5, 3, 2, 7, 1, 4])
    b = tf.constant([4, 6, 3])

    with tf.Session() as sess:
        print("scalar has shape", scalar.get_shape(), "and value:\n", scalar.eval())
        print("vector has shape", vector.get_shape(), "and value:\n", vector.eval())
        print("matrix has shape", matrix.get_shape(), "and value:\n", matrix.eval())

        reshape_a_2x3 = tf.reshape(a,[2,3])
        reshape_b_3x1 = tf.reshape(b,[3,1])
        a_mutiply_b = tf.matmul(reshape_a_2x3,reshape_b_3x1)
        print(a_mutiply_b.eval())
