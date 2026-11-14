import tkinter as tk
from .key import Key, KEY_ICONS
from PIL import Image, ImageTk

def create_overlay():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.wm_attributes("-alpha", 1)
    root.geometry("1000x70+0+0")
    root.wait_visibility(root)
    root.wm_attributes("-alpha", 0.3)
    root.configure(bg="white")
    root.withdraw()  
    frame = tk.Frame(root, bg="white")
    frame.pack(expand=True)

    key_icons = [] 
    hide = None

    def show_input(keys, duration=3000):

        nonlocal hide
        nonlocal key_icons

        if keys==None:
            return
        
        if hide is not None:
            root.after_cancel(hide)
            hide = None

        key_icons.clear()    
        for widget in frame.winfo_children():
            widget.destroy()

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

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - frame.winfo_reqwidth()) // 2
        y = (screen_height - frame.winfo_reqheight()) // 2

        root.geometry(f"{screen_width}x{frame.winfo_reqheight()}+0+{y}")
        hide = root.after(duration, root.withdraw)
        root.deiconify()
    return root, show_input
