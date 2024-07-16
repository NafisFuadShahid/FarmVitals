from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage, font

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame4")


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

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(861.0, 380.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(262.0, 273.0, image=image_image_3)

# Define custom fonts
montserratExtraBold_20 = font.Font(family="Montserrat", size=20, weight="bold")
montserratBold_20_1 = font.Font(family="Montserrat", size=20, weight="bold")
montserratNormal_18 = font.Font(
    family="Montserrat", size=18, weight="normal"
)  # Slightly larger normal font

# Text box for "POTATO LATE BLIGHT DISEASE"
canvas.create_text(
    67.0 + 391 / 2,  # Center align text by adjusting x-coordinate
    476.0 + 95 / 2,  # Center align text by adjusting y-coordinate
    anchor="center",
    text="POTATO LATE BLIGHT DISEASE",
    fill="#FFFFFF",
    font=montserratExtraBold_20,
    width=391,  # Set the width for text wrapping
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
    text="1. SEPARATE THE INFECTED LEAVES\n2. BURN THEM\n3. THEN BURN YOUR FAMILY AND THEN YOURSELF",
    fill="#FFFFFF",
    font=montserratNormal_18,
    width=662,  # Set the width for text wrapping
)

window.resizable(False, False)
window.mainloop()
