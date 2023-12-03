import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# # Make sure that the program is running on the CPU.
# mnist = tf.keras.datasets.mnist
# # pixel data, classification ## tuple of numpy arrays
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# ## Preprocessing

# # Normalize the training data, and set the values to be between 0 and 1.
# x_train = tf.keras.utils.normalize(x_train, axis=1)
# # Normalize the test data, and set the values to be between 0 and 1.
# x_test = tf.keras.utils.normalize(x_test, axis=1)

# # Build the model (basic sequential model) DEF (Sequential Model): A linear stack of layers.
# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28, 28))) # Flatten the input. Does not affect the batch size.
# model.add(tf.keras.layers.Dense(128, activation='relu')) # Add a dense layer with 128 neurons and relu activation.
# model.add(tf.keras.layers.Dense(128, activation='relu')) # Add a dense layer with 128 neurons and relu activation.
# model.add(tf.keras.layers.Dense(10, activation='softmax')) # Output layer with 10 neurons and softmax activation. Make sure they add up to 1.

# # optimizer is the function that will be used to optimize the model. 
# # loss is the function that will be used to calculate the error. 
# # metrics is the function that will be used to measure the accuracy of the model.
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# # Train the model.
# model.fit(x_train, y_train, epochs=3) # Train the model for 3 epochs.

# # save
# model.save('handwritten.model')

# load model
model = tf.keras.models.load_model('handwritten.model')

# # evaluate the model
# loss, accuracy = model.evaluate(x_test, y_test)

# print(loss)
# print(accuracy)

# Pull in the digit images.
image_number = 0
while os.path.isfile(f"digits/digit{image_number}.png"):
    try:
        img = cv2.imread(f"digits/digit{image_number}.png")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"The number is probably a {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("An exception occurred")
    finally:
        image_number += 1
    