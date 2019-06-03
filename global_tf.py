import tensorflow as tf

def some_func():
    z = tf.Variable(1, name='var_z')

a = tf.Variable(1, name='var_a')
b = tf.get_variable('var_b', 2)
with tf.name_scope('aaa'):
    c = tf.Variable(3, name='var_c')

with tf.variable_scope('bbb'):
    d = tf.Variable(3, name='var_d')

some_func()

print([str(i.name) for i in tf.global_variables()])
print([str(i.name) for i in tf.local_variables()])
