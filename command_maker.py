import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess


def add_apps():

    #do dobrania sie do przypientych rzeczy do frame:
    #for widget in frame.winfo_children()
    #    widget.destroy()

    home_path = os.path.expanduser("~")
    filename = filedialog.askopenfilename(initialdir=home_path)
    print(filename)
    apps.append(filename)
    
    label = tk.Label(frame, text=filename, bg="grey")
    label.pack()


def run_apps():
    for app in apps:
        file_type = recognize_file_type(app)
        if file_type == "py":
            run_python_script(app)
        elif file_type == "no extention":
            os.system(app)
        else:
            open_file(app)

def recognize_file_type(filename):
    aparted_filename = filename.strip(".").split(".")
    if len(aparted_filename) > 1:
        extention = filename.split(".")[-1]
        return extention
    return "no extention"

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def run_python_script(filename):
    if sys.platform == "win32" or "win64":
        p = "python "
    else:
        p = "python3 "
    os.system(p + filename)


root = tk.Tk()
apps = []

canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(canvas, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

if os.path.isfile("save.txt"):
    with open("save.txt", 'r') as f:
        apps = [i for i in f.read().split(",") if i.strip()]
        print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()




openFile = tk.Button(root, text="Open File", padx=10, pady=5, bg="#263D42", command=add_apps)
openFile.pack()

runApps = tk.Button(root, text="Run apps", padx=10, pady=5, bg="#263D42", command=run_apps)
runApps.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")