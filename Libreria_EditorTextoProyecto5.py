import tkinter as tk
import Librerias

root = tk.Tk()
root.title("Editor de Texto")
root.geometry("600x600")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", command=Librerias.open_file, accelerator="Ctrl+A")
file_menu.add_command(label="Guardar", command=Librerias.save_file, accelerator="Ctrl+G")
file_menu.add_separator()
file_menu.add_command(label="Borrar", command=Librerias.clear_text, accelerator="Ctrl+B")
menu_bar.add_cascade(label="Archivo", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cambiar color de texto", command=Librerias.change_text_color)
menu_bar.add_cascade(label="Editar", menu=edit_menu)

text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Buscar:").grid(row=0, column=0)
find_entry = tk.Entry(frame)
find_entry.grid(row=0, column=1)

tk.Label(frame, text="Reemplazar con:").grid(row=0, column=2)
replace_entry = tk.Entry(frame)
replace_entry.grid(row=0, column=3)

tk.Button(frame, text="Reemplazar", command=Librerias.find_and_replace).grid(row=0, column=4)

root.bind("<Control-a>", lambda event: Librerias.open_file())
root.bind("<Control-g>", lambda event: Librerias.save_file())
root.bind("<Control-b>", lambda event: Librerias.clear_text())

root.mainloop()


