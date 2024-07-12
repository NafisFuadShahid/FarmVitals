
from easygui import *
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import sys

detection=load_model('LeafModel.h5')

# message to be displayed  
text = 'hello poor farmers'

# show logo
img="logo.jpg"

# window title 
title = "File Open-Path"
  
# button list 
button_list = [] 
  
# button 1 
button1 = "select foto nigga"
button2 = "close"

# appending button to the button list 
button_list.append(button1) 
button_list.append(button2)

img_size=48
batch_size=64
datagen_train=ImageDataGenerator(horizontal_flip=True)
train_generator=datagen_train.flow_from_directory("My Drive/train_set",
target_size=(img_size,img_size),
batch_size=batch_size,
class_mode='categorical',
shuffle=True)
  
# creating a button box 
output = buttonbox(msg=text, title=title,image=img, choices=button_list) 
if output=='select foto nigga':
    txt=''
    path=fileopenbox()
    pred = buttonbox(msg="click on the photo nigga", title='Detection',image=path,choices=('Cancel',)) 
    if pred!=path:
        sys.exit()
        
    test_img=image.load_img(path,target_size=(48,48))
    test_img=image.img_to_array(test_img)
    test_img=np.expand_dims(test_img,axis=0) 
    result=detection.predict(test_img)
    a=result.argmax()
    classes=train_generator.class_indices
category=[]
for i in classes:
          category.append(i)
for i in range(len(classes)):
           if(i==a):
                output=category[i]
print(output) 
    