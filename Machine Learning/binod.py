import os
import numpy as np
import cv2 as cv
import pickle

data_dir = './garduino/plant'

categories = ['Great', 'Good']

data =[]

def make_data():
    for category in categories:
        path = os.path.join(data_dir, category)
        label = categories.index(category)

        for img_name in os.listdir(path):
            image_path = os.path.join(path, img_name)
            image = cv.imread(image_path)

            try:
                image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                image = cv.resize(image, (224,224))

                image = np.array(image, dtype = np.float32)

                data.append([image, label])

            except Exception as e:
                pass

    pik = open('./garduino/garduino/data.pickle', 'wb')
    pickle.dump(data, pik)
    pik.close()

make_data()

def load_data():
    pick = open('./garduino/garduino/data.pickle', 'rb')
    data = pickle.load(pick)
    pick.close()

    np.random.shuffle(data)

    feature = []
    labels = []

    for img, label in data:
        feature.append(img)
        labels.append(label)

    feature = np.array(feature, dtype=np.float32)
    labels = np.array(labels)

    feature = feature/255.0

    return [feature, labels]


