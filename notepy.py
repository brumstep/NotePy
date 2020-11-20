import tkinter as tk
import random
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from time import sleep
import threading
from tkinter import scrolledtext


window = tk.Tk()

def open_file():
    filepath = askopenfilename(
        filetypes=[("Notepy File","*.np"), ("Text files","*.txt"),("All files","*.*")]
    )
    if not filepath:
        return  # in cazul in care apesi pe cancel

    text_area.delete("1.0", tk.END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_area.insert(tk.END, text)
    window.title(f"NotePy - {filepath}")

def save_file():
    def change_title():
        window.title(f"NotePy - {filepath}")

    def puncte1():
        btn_save["text"] = "Save as"
    def puncte2():
        btn_save["text"] = "Save as ."
    def puncte3():
        btn_save["text"] = "Save as .."
    def puncte4():
        btn_save["text"] = "Save as ..."

    filepath = asksaveasfilename(
        defaultextension="np",
        filetypes=[("Notepy File", "*.np"), ("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_area.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"NotePy - DOCUMENT SAVED - {filepath}")
    timer = threading.Timer(3.0, change_title)
    timer.start()

    timer_p1 = threading.Timer(0.5, puncte1)
    timer_p1.start()
    timer_p2 = threading.Timer(1.0, puncte2)
    timer_p2.start()
    timer_p3 = threading.Timer(1.5, puncte3)
    timer_p3.start()
    timer_p4 = threading.Timer(2.0, puncte4)
    timer_p4.start()
    timer_p5 = threading.Timer(2.5, puncte1)
    timer_p5.start()

window.title("NotePy")

window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)


text_area = tk.scrolledtext.ScrolledText(window, wrap=tk.WORD)
fr_buttons = tk.Frame(window, bg="black")

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As", command=save_file)

btn_open.grid(row=0, column=0, ipadx=20, ipady=20, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, ipadx=20, ipady=20, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_area.grid(row=0, column=1, sticky="nsew")

window.mainloop()