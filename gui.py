import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
from converter import convert_image
from ico_utils import generate_ico
import tkinterdnd2
import ttkbootstrap as ttkb

output_formats = ["PNG", "JPEG", "WEBP", "BMP", "TIFF", "ICO"]

def launch_gui():
    app = ttkb.Window(themename="flatly")
    app.title("Image Converter")
    app.geometry("600x400")

    image_path = tk.StringVar()
    selected_format = tk.StringVar(value="PNG")
    width = tk.IntVar()
    height = tk.IntVar()
    quality = tk.IntVar(value=85)

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp *.bmp *.tiff *.ico")])
        if file_path:
            image_path.set(file_path)
            load_preview(file_path)

    def load_preview(path):
        try:
            img = Image.open(path)
            img.thumbnail((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            preview_label.config(image=img_tk)
            preview_label.image = img_tk
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def convert():
        if not image_path.get():
            messagebox.showwarning("No Image", "Please select an image.")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=f".{selected_format.get().lower()}",
                                                 filetypes=[(f"{selected_format.get()} files", f"*.{selected_format.get().lower()}")])
        if not save_path:
            return
        try:
            if selected_format.get() == "ICO":
                generate_ico(image_path.get(), save_path)
            else:
                convert_image(image_path.get(), save_path, selected_format.get(), width.get(), height.get(), quality.get())
            messagebox.showinfo("Success", "Image converted successfully.")
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

    ttk.Label(app, text="Select Image:").pack(pady=5)
    ttk.Button(app, text="Browse", command=browse_file).pack()
    ttk.Label(app, textvariable=image_path).pack(pady=5)

    preview_label = ttk.Label(app)
    preview_label.pack(pady=10)

    ttk.Label(app, text="Format:").pack()
    ttk.OptionMenu(app, selected_format, *output_formats).pack()

    ttk.Label(app, text="Resize (Width x Height):").pack()
    ttk.Entry(app, textvariable=width, width=5).pack(side="left", padx=10)
    ttk.Entry(app, textvariable=height, width=5).pack(side="left")

    ttk.Label(app, text="Quality (JPEG/WEBP):").pack()
    ttk.Scale(app, from_=10, to=100, variable=quality, orient="horizontal").pack()

    ttk.Button(app, text="Convert", command=convert).pack(pady=20)
    app.mainloop()
