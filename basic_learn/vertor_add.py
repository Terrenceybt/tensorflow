#! /usr/bin/env python

import tensorflow as tf

with tf.Graph().as_default():
    primes = tf.constant([2, 3, 5, 7, 11, 13], dtype = tf.int32)
    #create a six-element vector(1-D tensor)
    ones = tf.ones([1], dtype = tf.int32)
    #create another six-element vector, and each element in the vector will be initialized to 1
    beyond_primes = tf.add(primes, ones)
    
    x = tf.constant([[5,2,4,3], [5,1,6,-2], [-1,3,-1,-2]], dtype = tf.int32)
    y = tf.constant([[2,2],[3,5],[4,5],[1,6]], dtype = tf.int32)
    with tf.Session() as sess:
        print(beyond_primes.eval()) 
        matrix_multiply = tf.matmul(x,y)
        print(matrix_multiply.eval())
