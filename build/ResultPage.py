from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Leaf-Health-Checker\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(262.0, 273.0, image=image_image_3)

canvas.create_text(
    67.0,
    476.0,
    anchor="nw",
    text="POTATO LATE BLIGHT DISEASE",
    fill="#FFFFFF",
    font=("Montserrat-ExtraBold", 24 * -1),
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(x=142.0, y=596.0, width=243.0, height=49.0)

canvas.create_text(
    544.0,
    110.0,
    anchor="nw",
    text="STEPS TO FOLLOW:\n\nSEPARATE THE INFECTED LEAVES\nBURN THEM\nTHEN BURN YOUR FAMILY AND THEN YOURSELF",
    fill="#FFFFFF",
    font=("Montserrat-ExtraBold", 20 * -1),
)
window.resizable(False, False)
window.mainloop()
