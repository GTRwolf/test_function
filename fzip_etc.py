#获取cpu信息
from multiprocessing import cpu_count

import tensorflow as tf

a = [1, 2, 3]
b = [4, 5, 6]
c = [0, 1, 0, 2, 0, 3]

#测试zip的作用
zipped = zip(a, b)

#测试interactivesession
sess = tf.InteractiveSession()
x = tf.Variable([1.0, 2.0])
y = tf.constant([2.0, 3.0])
sub = tf.subtract(x, y)
with tf.Session() as sess:
    x.initializer.run()
    sub.eval()

print (sub.eval())
#打印cpu核心数
print(cpu_count())
#打印zip后的结果
print (list(zipped))