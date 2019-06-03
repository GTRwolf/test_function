import tensorflow as tf
def multi(sess, a, b):
    c = sess.run(tf.multiply(a, b))
    return c
