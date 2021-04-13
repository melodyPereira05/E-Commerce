import keras
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
from keras.layers import Dense,GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.applications.mobilenet import preprocess_input
import numpy as np
import PIL
from PIL import Image
from keras.optimizers import Adam
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os






mobile = keras.applications.mobilenet.MobileNet()

def prepare_image(file):
    img =Image.open(file)
    new_width  = 224
    new_height = 224
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)
   
    





def predict(result):
    global mobile
    preprocessed_image = result    
    predictions = mobile.predict(preprocessed_image)
    results = imagenet_utils.decode_predictions(predictions)
    #print(results[0][0])
    threshold=0.50
    resultlist=[]
    for i in range(5):
        if results[0][i][2]>=threshold:
            resultlist.append(results[0][i][1])

    i=0
    difference=0
    if len(resultlist)==0:
        while(difference<10) and i<5:
            
            difference=abs(results[0][i][2]-difference)
            resultlist.append(results[0][i][1])
            i+=1



    return resultlist   



def get_image(image_path):
    import numpy
    img11 =Image.open(image_path)
    img = cv2.cvtColor(numpy.array(img11), cv2.COLOR_RGB2BGR)      
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   
    
    return img1

def get_colors(image, number_of_colors, show_chart):
    
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
   
    counts = Counter(labels)
    # sort to ensure correct color percentage
    counts = dict(sorted(counts.items()))
    
    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    
    
    return  rgb_colors