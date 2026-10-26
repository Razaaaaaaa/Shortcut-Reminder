import tkinter as tk
from .key import Key, KEY_ICONS
from PIL import Image, ImageTk


def create_overlay():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry("1000x70+0+0")
    root.configure(bg="white")
    root.withdraw()  
    frame = tk.Frame(root, bg="white")
    frame.pack(expand=True)

    key_icons = [] 
    hide = None

    def start_move(event):
        root.x = event.x
        root.y = event.y

    def move_window(event):
        x = root.winfo_x() + event.x - root.x
        y = root.winfo_y() + event.y - root.y
        root.geometry(f"+{x}+{y}")

    frame.bind("<Button-1>", start_move)
    frame.bind("<B1-Motion>", move_window)

    def show_input(keys, duration=15000):
        nonlocal hide
        nonlocal key_icons

        if keys==None:
            return
        
        if hide is not None:
            root.after_cancel(hide)
            hide = None

        for widget in frame.winfo_children():
            widget.destroy()

        key_icons.clear()

        for i, key in enumerate(keys):
            key_icon_pil = KEY_ICONS.get(key)

            key_icon = ImageTk.PhotoImage(key_icon_pil)
            key_icons.append(key_icon)

            tk.Label(frame, image=key_icon, bg="white").pack(
                side="left", padx=2
            )

            if i < len(keys) - 1:
                tk.Label(
                    frame,
                    text="+",
                    font=("Arial", 18),
                    fg="black",
                    bg="white"
                ).pack(side="left", padx=2)

        width = frame.winfo_reqwidth()
        height = frame.winfo_reqheight()


        root.geometry(f"{width}x{height}")
        root.deiconify()
        hide = root.after(duration, root.withdraw)

    return root, show_input
