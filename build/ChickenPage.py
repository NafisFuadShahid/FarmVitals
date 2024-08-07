import os
import re
import threading
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, messagebox
from PIL import Image, ImageTk
from tensorflow import keras
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing import image
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
import numpy as np

# Set the environment variable to disable oneDNN custom operations
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Initialize model variable
detection = None


# Function to load the model asynchronously
def load_model_async():
    global detection
    detection = load_model("ChickenDiseaseModel.h5")


# Start the model loading in a separate thread
model_loading_thread = threading.Thread(target=load_model_async)
model_loading_thread.start()

# Image processing parameters
img_size = 48
batch_size = 32


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
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame1")


def open_home_page():
    home_page_path = Path(__file__).parent / "HomePage.py"
    subprocess.Popen(["python", str(home_page_path)])
    window.destroy()


def open_result_page():
    result_page_path = Path(__file__).parent / "ResultPage.py"
    subprocess.Popen(["python", str(result_page_path)])
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
        output_category = category[a].replace("_", " ")
        output_category = re.sub(" +", " ", output_category)

        with open("detection_results.txt", "w") as file:
            file.write(f"Detected Disease: {output_category}\n")
            file.write(f"Image Path: {path}")

        new_button_image = PhotoImage(file=relative_to_assets("proceed.png"))
        select_button.config(image=new_button_image)
        select_button.image = new_button_image

        selected_image = Image.open(path)
        selected_image = selected_image.resize((300, 300), Image.LANCZOS)
        selected_image_tk = ImageTk.PhotoImage(selected_image)
        canvas.itemconfig(image_2, image=selected_image_tk)
        canvas.image_2 = selected_image_tk

        select_button.config(command=open_result_page)
    else:
        messagebox.showerror(
            "Error", "No file selected. Please select a file to proceed."
        )


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

datagen_train = ImageDataGenerator(horizontal_flip=True)
train_generator = datagen_train.flow_from_directory(
    "chic Dataset/Train",
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode="categorical",
    shuffle=True,
)

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
select_button.place(x=675.0, y=543.0, width=231.0, height=65.0)

window.resizable(False, False)
window.mainloop()

# Ensure the model loading thread has finished before exiting
model_loading_thread.join()
