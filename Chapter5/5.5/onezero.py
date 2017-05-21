#coding=utf-8

import tensorflow as tf
import os
import cv2


def read_img(filepath):
  for file in os.listdir(data_dir):
    file_path = os.path.join(data_dir, file)
    print(file_path)

def gen_tfrecord(zero_dir, one_dir, output_tfrecord_file):
  '''
  '''
  tf_writer = tf.python_io.TFRecordWriter(output_tfrecord_file)

  #为数字0的数据
  for file in os.listdir(zero_dir):
    file_path = os.path.join(zero_dir, file)
    img_data = cv2.imread(file_path)
    image_raw = img_data.tostring()
    rows = img_data.shape[0]
    cols = img_data.shape[1]
    channels = img_data.shape[2]
    label_data = 0

    example = tf.train.Example()

    feature = example.features.feature
    feature['height'].int64_list.value.append(rows)
    feature['width'].int64_list.value.append(cols)
    feature['channels'].int64_list.value.append(channels)
    feature['image_raw'].bytes_list.value.append(image_raw)
    feature['label'].int64_list.value.append(label_data)

    tf_writer.write(example.SerializeToString())
  
  #为数字1的数据
  for file in os.listdir(one_dir):
    file_path = os.path.join(zero_dir, file)
    img_data = cv2.imread(file_path)
    image_raw = img_data.tostring()
    rows = img_data.shape[0]
    cols = img_data.shape[1]
    channels = img_data.shape[2]
    label_data = 1

    example = tf.train.Example()

    feature = example.features.feature
    feature['height'].int64_list.value.append(rows)
    feature['width'].int64_list.value.append(cols)
    feature['channels'].int64_list.value.append(channels)
    feature['image_raw'].bytes_list.value.append(image_raw)
    feature['label'].int64_list.value.append(label_data)

    tf_writer.write(example.SerializeToString())

  tf_writer.close()

    
def gen_tfrecord_data(train_data_dir, test_data_dir)
  '''
  生成训练和测试的tfrecord格式的数据
  '''
  train_data_zero_dir = os.path.join(train_data_dir, "0")  
  train_data_one_dir = os.path.join(train_data_dir, "1")  

  
  test_data_zero_dir = os.path.join(test_data_dir, "0")  
  test_data_one_dir = os.path.join(test_data_dir, "1")  

  
if __name__ == "__main__":
  read_img("./data/train/1/")
