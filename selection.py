import pyatspi
import tkinter as tk
import threading
import os

DEBUG = True 

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



def change_text(new_text):
    label.config(text=new_text)

    

def on_text_caret_moved(event):

    if event.type == "object:text-caret-moved:system":
        return

    try:
        source = event.source
        accessible_text = source.queryText()

        selection_count = accessible_text.getNSelections()

        if selection_count == 0:
            return

        if selection_count == 1:
            selection_start, selection_end = accessible_text.getSelection(0)

            full_content = accessible_text.getText(
                0,
                accessible_text.characterCount
            )

            selection_content = repr(
                accessible_text.getText(selection_start, selection_end)
            )

            caret_offset = accessible_text.caretOffset

            line_text, line_start, line_end = accessible_text.getStringAtOffset(
                selection_end if selection_start == caret_offset else selection_start,
                pyatspi.TEXT_GRANULARITY_LINE,
            )



            if (DEBUG) :
                os.system('clear')
                print("line_start", line_start, "line_end", line_end)
                print("selection_start", selection_start, "selection_end", selection_end)
                #print("selection_content", selection_content)
                #print("line_text", line_text)
                print("caret_offset", caret_offset)

            shortcuts = {
                "CTRL + A": (
                    selection_start == 0
                    and selection_end == accessible_text.characterCount
                ),
                 "CTRL + SHIFT + HOME" : (
                    caret_offset == 0 
                ), 
                "CTRL + SHIFT + END" : (
                    caret_offset == accessible_text.characterCount
                ),
                "SHIFT + END": (
                    caret_offset == line_end
                ),
                "SHIFT + HOME": (
                    caret_offset == line_start
                ),
                "SHIFT + UP" : ( caret_offset > line_start and caret_offset > line_end ),
                "SHIFT + DOWN" : ( caret_offset < line_start and caret_offset < line_end ),

                "CTRL + SHIFT + LEFT": (
                    (
                        full_content[max(caret_offset - 1, 0)] == " "
                        or " " in selection_content
                    )
                    and caret_offset == selection_start
                ),

                "CTRL + SHIFT + RIGHT": (
                    (
                        full_content[min(caret_offset, accessible_text.characterCount-1)] == " "
                        or " " in selection_content
                    )
                    and caret_offset == selection_end
                ),

                "SHIFT + RIGHT": (
                    (
                       
                        " " not in selection_content
                    )
                    and caret_offset == selection_end
                ),
                "SHIFT + LEFT": (
                    (
                         " " not in selection_content
                    )
                    and caret_offset == selection_start
                )         
            }

            for action, condition in shortcuts.items():
                if condition:
                    print(action)

                    root.after(
                        0,
                        change_text,
                        action
                    )

                    return

            print("NOTHING")
            root.after(0, change_text, "NOTHING")

    except Exception as e:
        print("Error PyAT-SPI :", e)




def start_pyatspi():

    pyatspi.Registry.registerEventListener(
        on_text_caret_moved,
        "object:text-caret-moved"
    )

    pyatspi.Registry.registerEventListener(
        on_text_caret_moved, 
        "object:text-selection-changed"
    )

    print("PyAT-SPI Listening...")

    pyatspi.Registry.start()


def start_move(event):
    root.x = event.x
    root.y = event.y


def move_window(event):

    x = root.winfo_x() + event.x - root.x
    y = root.winfo_y() + event.y - root.y

    root.geometry(f"+{x}+{y}")


label.bind("<Button-1>", start_move)
label.bind("<B1-Motion>", move_window)



root.bind(
    "<Escape>",
    lambda event: root.destroy()
)



pyatspi_thread = threading.Thread(
    target=start_pyatspi,
    daemon=True
)

pyatspi_thread.start()


root.mainloop()
