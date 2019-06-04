import tensorflow as tf
import numpy as np

def matrix_one_hot_test():
    a = tf.constant([[1,2,3,4],[0,3,4,1],[1,0,3,2],[2,2,2,0]])
    class_num = 5
    out = tf.one_hot(a, class_num)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        output = sess.run(out)
        print(output.shape)

def tf_matrix_reshape_test():
    a = tf.constant([ [[1,2,3,4],[0,3,4,1],[1,0,3,2]],
                      [[0,5,2,1],[9,8,4,2],[3,3,5,7]] ])
    b = tf.constant([1,2,3,5,6,4,6,8,93,10,3,1])
    out = tf.reshape(a, (6,4))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        out_ = sess.run(out)
        print(out_)



tf_matrix_reshape_test()