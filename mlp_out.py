import tensorflow as tf
import tensorflow.contrib.layers as layers

x1 = tf.constant(1.0)
l1 = tf.nn.l2_loss(x1)

x2 = tf.constant([2.5, -0.3])
l2 = tf.nn.l2_loss(x2)

tf.add_to_collection("losses", l1)
tf.add_to_collection("losses", l2)
tf.add_to_collection("X", x1)
tf.add_to_collection("X", x2)
losses = tf.get_collection('losses')
X = tf.get_collection("X")

loss_total = tf.add_n(losses)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
a = sess.run(l1)
b = sess.run(l2)
losses_val = sess.run(losses)
XX = sess.run(X)
loss_total_val = sess.run(loss_total)

print(a, b, XX)
print(losses, losses_val, loss_total_val)