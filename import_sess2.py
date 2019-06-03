import tensorflow as tf
import  import_sess1 as t
a = tf.constant(0.5)
b = tf.constant(8.0)
sess = tf.Session()
c = t.multi(sess, a, b)
print(c)