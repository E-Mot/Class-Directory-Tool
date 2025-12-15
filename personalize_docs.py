from docx import Document
import os
import shutil

#------------------------------------------- Get the path to the desktop -------------------------------------------

DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

#------------------------------------------- Rename the parent folder -------------------------------------------

def rename_parent_folder(new_folder_name):
    old_name = "Class template"
    old_path = os.path.join(DESKTOP_PATH, old_name)
    new_path = os.path.join(DESKTOP_PATH, new_folder_name)
    shutil.move(old_path, new_path)
    return new_folder_name

#------------------------------------------- Rename the discussions files -------------------------------------------

def modify_discussion_files(new_folder_name, new_file_name):
    sub_folder_path = os.path.join(DESKTOP_PATH, new_folder_name, "1. Units")
    for folder_name in os.listdir(sub_folder_path):
        folder_path = os.path.join(sub_folder_path, folder_name)
        for sub in os.listdir(folder_path):
            if sub == "Discussions":
                file_path = os.path.join(folder_path, "Discussions", "Discussion board posts.docx")
                doc = Document(file_path)
                for p in doc.paragraphs:
                    for r in p.runs:
                        if "Class #" in r.text:
                            r.text = r.text.replace("Class #", new_file_name)
                doc.save(file_path)
    return new_file_name
