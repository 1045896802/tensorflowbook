import tensorflow as tf

weight1 = tf.Variable(0.001)
# weight2�ĳ�ʼֵ��weight��2��
weight2 = tf.Variable(weight1.initialized_value() * 2)
init = tf.global_variables_initializer()
with tf.Session() as sess:
  sess.run(init)
  print("weight1 is:")
  print(sess.run(weight1))
  print("weight2 is:")
  print(sess.run(weight2))
