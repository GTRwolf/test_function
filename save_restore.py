import tensorflow as tf

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

w = tf.Variable(tf.zeros([1, 1], dtype=tf.float32))
b = tf.Variable(tf.ones([1, 1], dtype=tf.float32))
y_hat = tf.add(b, tf.matmul(x, w))

saver = tf.train.Saver()  # defaults to saving all variables - in this case w and b
save_dir = './save_model/model'
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    if True:
        for i in range(500):
            if (i + 1) % 10 == 0:
                saver.save(sess, save_dir + 'model.ckpt', global_step=i+1)
    # else:
    #     # Here's where you're restoring the variables w and b.
    #     # Note that the graph is exactly as it was when the variables were
    #     # saved in a prior training run.
    #     ckpt = tf.train.get_checkpoint_state(FLAGS.checkpoint_dir)
    #     if ckpt and ckpt.model_checkpoint_path:
    #         saver.restore(sess, ckpt.model_checkpoint_path)
    #
    #     # Now you can run the model to get predictions
    #     batch_x = ...load some data...
    #     predictions = sess.run(y_hat, feed_dict={x: batch_x})