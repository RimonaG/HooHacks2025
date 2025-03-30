import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("Available devices:", tf.config.list_physical_devices())
print("GPU available:", tf.config.list_physical_devices('GPU'))