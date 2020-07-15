
import tensorflow.compat.v1 as tf
import keras
from keras.backend.tensorflow_backend import set_session

a = tf.constant(1)
b = tf.constant(2)


with tf.Session() as sess:
    print(sess.run(b))
    print(sess.run(a + b))
    print(sess.run(a*b))
set_session(sess)
keras.backend.clear_session()

