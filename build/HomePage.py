from pathlib import Path
import os

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Leaf-Health-Checker\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(x=959.0, y=315.0, width=232.0, height=270.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
)
button_2.place(x=671.0, y=315.0, width=237.0, height=270.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
)
button_3.place(x=380.0, y=323.0, width=235.0, height=262.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
)
button_4.place(x=90.0, y=323.0, width=240.0, height=262.0)


window.resizable(False, False)
window.mainloop()
