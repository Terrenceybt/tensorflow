#! /usr/bin/env python

print("hello world")
import tensorflow as tf
c = tf.constant('hello tensorflow')
with tf.Session() as sess:
    print(sess.run(c))
