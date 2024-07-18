from pathlib import Path
import os
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from tkinter import ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("FarmVitals")

window.geometry("1287x753")
window.configure(bg="#FFFFFF")


def open_leaf_page():
    leaf_page_path = Path(__file__).parent / "LeafPage.py"
    subprocess.Popen(["python", str(leaf_page_path)])
    window.destroy()


def open_chicken_page():
    chicken_page_path = Path(__file__).parent / "ChickenPage.py"
    subprocess.Popen(["python", str(chicken_page_path)])
    window.destroy()


def open_paddy_page():
    paddy_page_path = Path(__file__).parent / "PaddyPage.py"
    subprocess.Popen(["python", str(paddy_page_path)])
    window.destroy()


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

montserratExtraBold_30 = font.Font(family="Montserrat", size=30, weight="bold")
montserratBold_20_1 = font.Font(family="Montserrat", size=20, weight="bold")
montserratNormal_18 = font.Font(family="Montserrat", size=18, weight="normal")

canvas.create_text(
    643.5,  # Centered horizontally
    68.0,
    anchor="center",
    text="FarmVitals",
    fill="#FFFFFF",
    font=montserratExtraBold_30,
)

canvas.create_text(
    80.0,
    240.0,
    anchor="nw",
    text="Choose the corresponding type:",
    fill="#FFFFFF",
    font=montserratNormal_18,
)

unknown_button_image = PhotoImage(file=relative_to_assets("button_1.png"))
unknown_button = Button(
    image=unknown_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("unknown_button clicked"),
    relief="flat",
)
unknown_button.place(x=959.0, y=315.0, width=232.0, height=270.0)

chicken_button_image = PhotoImage(file=relative_to_assets("button_2.png"))
chicken_button = Button(
    image=chicken_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
)
chicken_button.place(x=671.0, y=315.0, width=237.0, height=270.0)

paddy_button_image = PhotoImage(file=relative_to_assets("button_3.png"))
paddy_button = Button(
    image=paddy_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
)
paddy_button.place(x=380.0, y=323.0, width=235.0, height=262.0)

leaf_button_image = PhotoImage(file=relative_to_assets("button_4.png"))
leaf_button = Button(
    image=leaf_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
)
leaf_button.place(x=90.0, y=323.0, width=240.0, height=262.0)

# Modify the command parameter of each button
leaf_button.configure(command=open_leaf_page)
chicken_button.configure(command=open_chicken_page)
paddy_button.configure(command=open_paddy_page)


window.resizable(False, False)
window.mainloop()
