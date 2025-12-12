import tkinter as tk
from tkinter import font
from tkinter import messagebox
import os
from create_template import execute_template_functions
from personalize_docs import rename_parent_folder, modify_discussion_files

def resource_path(relative_path):
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, relative_path)

def get_entry_1():
    if entry_1.get() == "":
        return False
    else:
        value = entry_1.get()
        return value
    
def get_entry_2():
    if entry_2.get() == "":
        return False
    else:
        value = entry_2.get()
        return value

def create_new_directory():
    if entry_1.get() and get_entry_2():
        execute_template_functions()
        rename_parent_folder(get_entry_1())
        modify_discussion_files(get_entry_1(), get_entry_2())
        entry_1.delete(0, tk.END)
        entry_2.delete(0, tk.END)
    elif not entry_1.get():
        messagebox.showerror("Error","Please enter folder name")
    elif not entry_2.get():
        messagebox.showerror("Error","Please enter class name")

root = tk.Tk()
root.geometry("450x250")
root.minsize(450,250)
root.maxsize(450,250)
root.title("Class Directory Tool")
root.iconbitmap(resource_path("foldericon.ico"))
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

label_1_font = font.Font(weight="bold", size=10, family="Segoe UI")
label_1 = tk.Label(root, text="Fill out the fields to create a new directory", font=label_1_font)
label_1.grid(row=0, column=0, columnspan=2, pady=(10,20), sticky="nsew")

frame_1 = tk.Frame(root, borderwidth=2, relief="groove", bg="#f7f7f7")
frame_1.grid(row=1, column=0, columnspan=2, padx=(20,20), sticky="ew")
frame_1.grid_rowconfigure(0, weight=1)
frame_1.grid_rowconfigure(1, weight=1)
frame_1.grid_columnconfigure(0, weight=1)
frame_1.grid_columnconfigure(1, weight=1)

label_2 = tk.Label(frame_1, text="Parent folder name:", bg="#f7f7f7")
label_2.grid(row=0, column=0, pady=(20,0), sticky="e")
entry_1 = tk.Entry(frame_1)
entry_1.grid(row=0, column=1, sticky="ew", padx=(20,20), pady=(20,0))

label_3 = tk.Label(frame_1, text="Class name for Discussions files:", bg="#f7f7f7")
label_3.grid(row=1, column=0, pady=(20,20), sticky="e")
entry_2 = tk.Entry(frame_1)
entry_2.grid(row=1, column=1, sticky="ew", padx=(20,20), pady=(20,20))

button_1_font = font.Font(size=10, family="Segoe UI")
button_1 = tk.Button(root, text="Create", command=create_new_directory, font=button_1_font, width=9, height=1, pady=6, relief="raised", bg="#f7f7f7", bd=2)
button_1.grid(row=2, column=0, columnspan=2, pady=(10,20))

if __name__ == "__main__":
    root.mainloop()