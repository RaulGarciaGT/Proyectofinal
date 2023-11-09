import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring
import webbrowser

def open_file():
    file_path = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

def save_file_as():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

def print_to_file():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

def change_font_size():
    size = font_size_var.get()
    text.config(font=("Helvetica", size))

def toggle_underline():
    current_tags = text.tag_names(tk.SEL_FIRST)
    if "underline" in current_tags:
        text.tag_remove("underline", tk.SEL_FIRST, tk.SEL_LAST)
    else:
        text.tag_add("underline", tk.SEL_FIRST, tk.SEL_LAST)
        text.tag_config("underline", underline=True)

def undo():
    text.edit_undo()

def redo():
    text.edit_redo()

def show_info():
    info = """
    Editor Somos lo más pro txt
    Esta aplicación te permitirá abrir, editar y guardar archivos de texto.
    Licencia: Raul Licencia
    """
    tk.messagebox.showinfo("Información", info)

def open_user_manual():
    url = "https://docs.google.com/document/d/1IgMrIBnbqxPR4Gf5_2GOpPV5YmHUk1QnpL9Qhwd1m9I/edit"
    webbrowser.open(url)

def new_file():
    text.delete(1.0, tk.END)

def set_background_color(color):
    if color == "original":
        text.configure(bg="white")
    elif color == "rojo":
        text.configure(bg="red")
    elif color == "verde":
        text.configure(bg="green")

app = tk.Tk()
app.title("Editor de Texto Raul")

menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nuevo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_command(label="Guardar como", command=save_file_as)
file_menu.add_command(label="Imprimir Texto", command=print_to_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=app.quit)

format_menu = tk.Menu(menu)
menu.add_cascade(label="Formato", menu=format_menu)
format_menu.add_command(label="Cambiar Tamaño de Fuente", command=change_font_size)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label="Deshacer", command=undo)
edit_menu.add_command(label="Rehacer", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cambiar Fondo Original", command=lambda: set_background_color("original"))
edit_menu.add_command(label="Cambiar Fondo Rojo", command=lambda: set_background_color("rojo"))
edit_menu.add_command(label="Cambiar Fondo Verde", command=lambda: set_background_color("verde"))

help_menu = tk.Menu(menu)
menu.add_cascade(label="Ayuda", menu=help_menu)
help_menu.add_command(label="Información", command=show_info)
help_menu.add_command(label="Manual de Usuario", command=open_user_manual)

text = tk.Text(app)
text.pack(fill="both", expand=True)

font_size_var = tk.IntVar(value=12)
font_size_menu = tk.OptionMenu(app, font_size_var, 12, 14, 16, 18, 20)
font_size_menu.pack()

app.mainloop()
