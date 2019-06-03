import tensorflow as tf
import numpy as np

a = 0.1
b = 0.2
c = 1.0,
action = tf.distributions.Normal(a, c).sample(1)

with tf.Session() as sess:
    test = sess.run(action)
    print(test)