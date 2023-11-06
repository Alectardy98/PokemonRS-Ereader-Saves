import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import simpledialog
import re

def modify_files(file_paths, new_data):
    try:
        new_data = new_data.encode().hex()
        byte_data = bytes.fromhex(new_data)
        if len(byte_data) < 29:
            byte_data += bytes.fromhex('00' * (29 - len(byte_data)))
        elif len(byte_data) > 29:
            byte_data = byte_data[:29]

        for file_path in file_paths:
            file_path = file_path.strip('{}')  # Remove curly braces from the file path
            with open(file_path, 'r+b') as file:
                file.seek(4)
                file.write(byte_data)
                print("Bytes 4 to 32 have been modified for", file_path)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def on_drop(event):
    # Use regular expression to extract file paths enclosed in curly braces
    file_paths = re.findall(r'\{.*?\}', event.data)
    file_paths = [path.strip('{}') for path in file_paths]  # Remove curly braces
    print("Extracted file paths:", file_paths)  # Check the extracted paths
    new_data = simpledialog.askstring("Input", "Enter the text:")
    if new_data is not None:
        modify_files(file_paths, new_data)

def on_drag_enter(event):
    status_label.config(text='Drag and drop bin files here to rename the header')

def on_drag_leave(event):
    status_label.config(text='')

def open_window():
    root = TkinterDnD.Tk()
    root.title("Drag and Drop File Modifier")  # Change the window title
    root.geometry("1000x1000")  # Adjust window size (width x height)

    global status_label
    status_label = tk.Label(root, text='', width=80)
    status_label.pack(pady=20)

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', on_drop)
    root.dnd_bind('<<DragEnter>>', on_drag_enter)
    root.dnd_bind('<<DragLeave>>', on_drag_leave)

    on_drag_enter(None)  # Update the label at the start
    root.mainloop()

# Open the window
open_window()