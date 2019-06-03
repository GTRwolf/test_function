import threading
import tensorflow as tf

def dead_loop():
    while True:
        print("test coord")


worker_threads = []
COORD = tf.train.Coordinator()
for i in range(20000000):
    job = lambda: dead_loop()
    t = threading.Thread(target=job)
    t.start()
    worker_threads.append(t)
#COORD.join(worker_threads)
