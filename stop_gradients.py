import tensorflow as tf
import numpy as np

status_n = tf.placeholder(tf.float32, [None, 5], 'status-input')


def build_net():
    print("building net")
    w_init = tf.random_normal_initializer(0., 0.1)
    with tf.variable_scope('actor'):
        l_a = tf.layers.dense(status_n, 64, tf.nn.relu, kernel_initializer=w_init, name='l_a')
        mu = tf.layers.dense(l_a, 5, tf.nn.relu, kernel_initializer=w_init, name='mu')
        mu2 = tf.layers.dense(l_a, 5, tf.nn.relu, kernel_initializer=w_init, name='mu2')
        mu3 = tf.layers.dense(l_a, 5, tf.nn.relu, kernel_initializer=w_init, name='mu3')
        sigma = tf.layers.dense(l_a, 5, tf.nn.softplus, kernel_initializer=w_init, name='sigma')
        a = tf.Print(sigma, ['s:', sigma])
    with tf.variable_scope('critic'):
        l_c = tf.layers.dense(status_n, 32, tf.nn.relu, kernel_initializer=w_init, name='lc')
        v = tf.layers.dense(l_c, 1, kernel_initializer=w_init, name='v')
        return mu, mu2, mu3, sigma, v, w_init, a
mu, mu2, mu3, sigma, v, w, a = build_net()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # s = np.array([[1.0, 2.0, 3.0, 4.0, 5.0],
    #               [0.1, 0.2, 0.3, 0.4, 0.5],
    #               [9.0, 8.0, 7.0, 6.0, 5.0]])
    s = np.random.uniform(0.0, 1.0, (3,5))
    t = np.random.uniform(0.0, 1.0, (3,5))

    print(sess.run(a, feed_dict={status_n:s}))