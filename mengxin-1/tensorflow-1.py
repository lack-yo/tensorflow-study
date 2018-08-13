# tensorflow
# coding=UTF-8
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0], name="b")
with tf.Session() as sess:
    print(sess.run(hello))
    print(sess.run(a + b))
# 通过a.graph查看当前张量所属的计算图
print(a.graph is tf.get_default_graph())
