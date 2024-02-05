# Made By Ali Hany | Arrow-DV <3
# visit Us https://arrow-dev.rf.gd
# Created in 2/5/2024 | Last Updated 2/5/2024
"""
-> Gui Program To Download Youtube Videos Or Youtube Shorts In High Quality 
"""


# Import Needed Library's
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button,filedialog
from tkinter import messagebox
import tkinter as tk
from os import system
from PIL import ImageTk
from pytube import YouTube
from customtkinter import CTkFont as Font


# Make The Root
root = Tk()
root.geometry("578x255")
root.configure(bg="#FFFFFF")
root.title("Pytuber")
root.resizable(False, False)

# Variables
link = tk.StringVar(root)

# Make Functions We Will Use
def download_video(link) -> YouTube:
    link = link.get()
    if len(link) > 10:
        try:
            save_path = filedialog.askdirectory(title="Save Location")
            youtube_object = YouTube(link)
            video = youtube_object.streams.get_highest_resolution()
            label.configure(text=youtube_object.title[:20] 
                            + "..." if len(youtube_object.title) > 20 else "")
            video.download(save_path)  # Specify the save path here
            messagebox.showinfo("Success", "Video downloaded successfully!")
            system(f"start {save_path}")
        except Exception as error:
            messagebox.showerror("Error", f"Error: {error}")
# Design The Gui
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"
def relative_to_assets(path: str) -> Path:
    """Translate The Path To Make Tkinter Library Understand It"""
    return ASSETS_PATH / path


# Canvas
canvas = Canvas(
    root,bg="#FFFFFF",height=255,
    width=578,bd=0,
    highlightthickness=0,relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    578.0,
    255.0,
    fill="#FF5A5A",
    outline=""
)
canvas.create_rectangle(
    0.0,
    0.0,
    335.0,
    255.0,
    fill="#CD4646",
    outline=""
)
# Label
font = Font(size=30)
label = tk.Label(root,text="Insert a Link",font=font,bg="#CD4646",fg="white")
label.pack()
label.place(x=35,y=70)
# The Youtube Image
image_1 = ImageTk.PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(
    447.0,
    132.0,
    image=image_1
)
entry_image_1 = ImageTk.PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(
    161.15770721435547,
    131.52353191375732,
    image=entry_image_1
)
# TextBox
entry_1 = Entry(
    textvariable=link,
    bd=0,
    bg="#E8E8E8",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=36.02349853515625,
    y=117.5975112915039,
    width=250.26841735839844,
    height=25.852041244506836
)

# Button
button_image_1 = ImageTk.PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,activebackground="#CD4646",
    command=lambda: download_video(link),
    relief="flat"
)
button_1.place(
    x=36.0,
    y=179.0,
    width=250.0,
    height=47.0
)

# Run The App
root.mainloop()
