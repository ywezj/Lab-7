import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

def get_random_fox_image():
    response = requests.get("https://randomfox.ca/floof/")
    if response.status_code == 200:
        data = response.json()
        return data['image']
    else:
        return None

def update_image():
    image_url = get_random_fox_image()
    if image_url:
        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image.thumbnail((300, 300)) 
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  

root = tk.Tk()
root.title("Random Fox Generator")

label = ttk.Label(root)
label.pack(pady=10)

button = ttk.Button(root, text="Следующая лиса", command=update_image)
button.pack(pady=10)

update_image()

root.mainloop()