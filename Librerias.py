import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))

def clear_text():
    text_area.delete("1.0", tk.END)

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(fg=color)

def find_and_replace():
    find_str = find_entry.get()
    replace_str = replace_entry.get()
    content = text_area.get("1.0", tk.END)
    new_content = content.replace(find_str, replace_str)
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", new_content)
    messagebox.showinfo("Buscar y Reemplazar", "Reemplazo completado.")

    