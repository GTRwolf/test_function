import tensorflow as tf
import time
import os
from tensorflow.examples.tutorials.mnist import input_data

INPUT_NODE = 784
OUTPUT_NODE = 10
LAYER1_NODE = 500

BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99

REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 20000
MOVING_AVERAGE_DECAY = 0.99
model_path = './save_model/model'
load_path = "./save_model/model-15000"

def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    if avg_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)
        return tf.matmul(layer1, weights2) + biases2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) + avg_class.average(biases1))
        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)


def train(mnist):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')

    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))

    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))

    y = inference(x, None, weights1, biases1, weights2, biases2)

    global_step = tf.Variable(0, trainable=False)

    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)

    variable_averages_op = variable_averages.apply(tf.trainable_variables())

    average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)

    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))

    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)

    regularization = regularizer(weights1) + regularizer(weights2)

    loss = cross_entropy_mean + regularization

    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step, mnist.train.num_examples / BATCH_SIZE,
                                               LEARNING_RATE_DECAY)

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    with tf.control_dependencies([train_step, variable_averages_op]):
        train_op = tf.no_op(name='train')
        correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32), name='accu')


    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        load = tf.train.import_meta_graph(load_path + '.meta')
        load.restore(sess, tf.train.latest_checkpoint('./save_model'))
        graph = tf.get_default_graph()
        X = graph.get_tensor_by_name("x-input:0")
        Y = graph.get_tensor_by_name("y-input:0")
        acc = graph.get_tensor_by_name("accu:0")
        validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}
        test_feed = {X: mnist.test.images, Y: mnist.test.labels}
        # for i in range(TRAINING_STEPS):
        #     if i % 1000 == 0:
        #         validate_acc = sess.run(accuracy, feed_dict=validate_feed)
        #         print("%d %.3f" % (i, validate_acc))
        #         if os.path.isdir(model_path) is False:
        #             os.makedirs(model_path)
        #         tf.train.Saver().save(sess, save_path=model_path, global_step=i)
        #     xs, ys = mnist.train.next_batch(BATCH_SIZE)
        #     sess.run(train_op, feed_dict={x: xs, y_: ys})

        print(sess.run(acc, feed_dict=test_feed))
        # test_acc = sess.run(accuracy, feed_dict=test_feed)
        # test_acc2 = sess.run(accuracy, feed_dict=validate_feed)
        # print("stop", test_acc, test_acc2)

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
train(mnist)

