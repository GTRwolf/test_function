import tensorflow as tf

a = tf.constant([[[0,5,6,4,9,7]], [[0,3,2,4,5,2]]])
b = tf.nn.top_k(a, 6, sorted=True)
c = tf.reverse(a, axis=[0])
test = a * a
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(test))