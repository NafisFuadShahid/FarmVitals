from easygui import *
from tensorflow import keras
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing import image
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator

# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import sys

# Load the trained model
detection = load_model("chicken_disease_model.h5")

# Set up the interface
text = "Welcome to Chicken Disease Detector"
img = "chicken_healthy.JPG"  # Change this to an appropriate welcome image
title = "Chicken Disease Detector"
button_list = ["Select Photo", "Close"]

img_size = 48
batch_size = 32  # Adjust batch size if needed

# Assuming you have a directory with the training data for class indices
train_folder = "chic Dataset/Train"

datagen_train = ImageDataGenerator(horizontal_flip=True)
train_generator = datagen_train.flow_from_directory(
    train_folder,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode="categorical",
    shuffle=True
)

# Function to predict the disease from an image
def predict_disease(img_path):
    test_img = image.load_img(img_path, target_size=(img_size, img_size))
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0)
    result = detection.predict(test_img)
    a = result.argmax()
    return a

# Main loop for the GUI
while True:
    output = buttonbox(msg=text, title=title, image=img, choices=button_list)

    if output == "Select Photo":
        path = fileopenbox(
            msg="Please select a photo for disease detection",
            title="Select Photo",
            filetypes=["*.jpg", "*.png", "*.jpeg"],
        )

        if path:
            pred = buttonbox(
                msg="Selected Photo",
                title="Detection",
                image=path,
                choices=["Proceed", "Cancel"],
            )
            if pred == "Proceed":
                a = predict_disease(path)
                classes = train_generator.class_indices
                category = [k for k in classes]
                output_category = category[a]

                msgbox(
                    msg=f"The detected class is: {output_category}",
                    title="Result",
                    ok_button="OK",
                )
            else:
                continue
        else:
            msgbox(
                msg="No file selected. Please select a file to proceed.",
                title="Error",
                ok_button="OK",
            )
    else:
        sys.exit()