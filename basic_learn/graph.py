#! /usr/bin/env python

import tensorflow as tf

g = tf.Graph()
with g.as_default():
    x = tf.constant(8, name = "x_constant")
    y = tf.constant(5, name = "y_constant")
    sum = tf.add(x, y, name = "x_y_sum")

    with tf.Session() as sess:
        print(sum.eval())
