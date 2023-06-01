import webcam
import tensorflow as tf
import numpy as np

if __name__ == '__main__':

    categories = ['Great', 'Good']

    model = tf.keras.models.load_model('./garduino/plant.h5')
    
    for w in webcam.webcam():
        
        img = np.array([w])
        prediction = model.predict(img)

        print("Status: " + categories[np.argmax(prediction[0])])