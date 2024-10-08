import os
import sqlite3
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, font, Label
from PIL import Image, ImageTk, ImageOps

# Explicit imports to satisfy Flake8
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Adjust the path to point to the parent directory
parent_directory = OUTPUT_PATH.parent
detection_results_path = parent_directory / "detection_results.txt"
db_path = parent_directory / "disease_remedy.db"


def load_detection_results(filepath: str):
    with open(filepath, "r") as file:
        lines = file.readlines()
        detected_disease = lines[0].strip().split(": ")[1]
        image_path = lines[1].strip().split(": ")[1]
    return detected_disease, image_path


# Load detection results
detected_disease, image_path = load_detection_results(detection_results_path)


def fetch_remedy_steps(db_path: str, disease_name: str) -> str:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT steps FROM remedy WHERE name = ?", (disease_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "No remedy steps found."


# Fetch remedy steps
remedy_steps = fetch_remedy_steps(db_path, detected_disease)


def resize_image_with_border(
    image_path,
    size=(329, 329),
    border_width=2,
    border_color="white",
):
    # Load original image
    original_image = Image.open(image_path)

    # Resize the image
    resized_image = original_image.resize(size, Image.LANCZOS)

    # Create a border
    border_image = ImageOps.expand(
        resized_image, border=border_width, fill=border_color
    )

    return border_image


def open_home_page():
    home_page_path = Path(__file__).parent / "HomePage.py"
    subprocess.Popen(["python", str(home_page_path)])  # Start HomePage.py
    window.destroy()


window = Tk()
window.title("FarmVitals")
window.geometry("1287x753")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=753,
    width=1287,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(643.0, 376.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(861.0, 380.0, image=image_image_2)

# Resize image with border only
pil_image_3 = resize_image_with_border(image_path, size=(329, 329), border_width=2)
image_image_3 = ImageTk.PhotoImage(pil_image_3)
image_label_3 = Label(window, image=image_image_3)
image_label_3.place(x=98, y=109)

# Define custom fonts
montserratExtraBold_20 = font.Font(family="Montserrat", size=20, weight="bold")
montserratBold_20_1 = font.Font(family="Montserrat", size=20, weight="bold")
montserratNormal_18 = font.Font(
    family="Montserrat", size=18, weight="normal"
)  # Slightly larger normal font

# Text box for the detected disease
canvas.create_text(
    67.0 + 391 / 2,  # Center align text by adjusting x-coordinate
    476.0 + 95 / 2,  # Center align text by adjusting y-coordinate
    anchor="center",
    text=detected_disease.upper() + " DISEASE",
    fill="#FFFFFF",
    font=montserratExtraBold_20,
    width=391,  # Set the width for text wrapping
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_home_page,
    relief="flat",
)
button_1.place(x=142.0, y=596.0, width=243.0, height=49.0)

# Text box for "STEPS TO FOLLOW" and subsequent steps
canvas.create_text(
    544.0,
    110.0,
    anchor="nw",
    text="STEPS TO FOLLOW: \n\n",
    fill="#FFFFFF",
    font=montserratBold_20_1,
    width=662,  # Set the width for text wrapping
)

canvas.create_text(
    544.0,
    160.0,  # Adjusted position to start below "STEPS TO FOLLOW:"
    anchor="nw",
    text=remedy_steps.replace("\\n", "\n"),
    fill="#FFFFFF",
    font=montserratNormal_18,
    width=662,  # Set the width for text wrapping
)

window.resizable(False, False)
window.mainloop()
