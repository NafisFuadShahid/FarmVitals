import os
import re  # Import the regular expressions module
import threading
from easygui import *
from tensorflow import keras
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing import image
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, messagebox
import subprocess

# Set the environment variable to disable oneDNN custom operations
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Initialize model variable
detection = None


# Function to load the model asynchronously
def load_model_async():
    global detection  # Use global variable to store the loaded model
    detection = load_model("LeafModel.h5")


# Image processing parameters
img_size = 48
batch_size = 64


# Function to predict disease
def predict_disease(img_path):
    global detection
    test_img = image.load_img(img_path, target_size=(img_size, img_size))
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0)
    result = detection.predict(test_img)
    a = result.argmax()
    return a


# Tkinter UI setup
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def open_home_page():
    home_page_path = Path(__file__).parent / "HomePage.py"
    subprocess.Popen(["python", str(home_page_path)])  # Start HomePage.py
    window.destroy()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def select_photo():
    path = filedialog.askopenfilename(
        title="Please select a photo for disease detection",
        filetypes=[("Image files", "*.jpg *.png *.jpeg")],
    )
    if path:
        a = predict_disease(path)
        classes = train_generator.class_indices
        category = [k for k in classes]
        output_category = category[a].replace(
            "_", " "
        )  # Replace underscores with spaces
        output_category = re.sub(
            " +", " ", output_category
        )  # Ensure only one whitespace between words

        messagebox.showinfo("Result", f"The detected class is: {output_category}")

        # Write the result to a file
        with open("./detection_results.txt", "w") as file:
            file.write(f"Detected Disease: {output_category}\n")
            file.write(f"Image Path: {path}")
    else:
        messagebox.showerror(
            "Error", "No file selected. Please select a file to proceed."
        )


# Data generator
datagen_train = ImageDataGenerator(horizontal_flip=True)
train_generator = datagen_train.flow_from_directory(
    "My Drive/train_set",
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode="categorical",
    shuffle=True,
)

# Initialize the Tkinter window
window = Tk()
window.title("FarmVitals")
window.geometry("1287x753")
window.configure(bg="#F0F0F0")

canvas = Canvas(
    window,
    bg="#F0F0F0",
    height=753,
    width=1287,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(276.0, 376.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(927.0, 276.0, image=image_image_2)

home_button_image = PhotoImage(file=relative_to_assets("button_1.png"))
home_button = Button(
    image=home_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=open_home_page,
    relief="flat",
)
home_button.place(x=945.0, y=543.0, width=231.0, height=65.0)

select_button_image = PhotoImage(file=relative_to_assets("button_2.png"))
select_button = Button(
    image=select_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=select_photo,
    relief="flat",
)
select_button.place(x=679.0, y=543.0, width=231.0, height=65.0)

window.resizable(False, False)
window.mainloop()

# Start the model loading in a separate thread after the UI has been set up
model_loading_thread = threading.Thread(target=load_model_async)
model_loading_thread.start()

# Ensure the model loading thread has finished before exiting
model_loading_thread.join()
