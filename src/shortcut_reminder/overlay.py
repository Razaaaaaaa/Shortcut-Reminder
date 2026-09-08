import tkinter as tk


def create_overlay():
    root = tk.Tk()

    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry("400x100+500+300")

    label = tk.Label(
        root,
        text="NOTHING",
        font=("Arial", 20),
        bg="white",
        fg="black"
    )

    label.pack(fill="both", expand=True)

    def start_move(event):
        root.x = event.x
        root.y = event.y

    def move_window(event):
        x = root.winfo_x() + event.x - root.x
        y = root.winfo_y() + event.y - root.y
        root.geometry(f"+{x}+{y}")

    def change_text(new_text):
        label.config(text=new_text)

    label.bind("<Button-1>", start_move)
    label.bind("<B1-Motion>", move_window)

    root.bind("<Escape>", lambda event: root.destroy())

    return root, change_text
