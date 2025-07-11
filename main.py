# main.py
import tkinter as tk
from tkinter import ttk, messagebox
import db
from datetime import date

#FUNCIONES
def agregar_persona():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    genero = combo_genero.get()
    if nombre and edad and genero:
        db.agregar_persona(nombre, int(edad), genero)
        cargar_personas()
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        combo_genero.set("")
    else:
        messagebox.showwarning("Campos vacíos", "Completar todos los campos")

def eliminar_persona():
    seleccionado = tree_personas.selection()
    if seleccionado:
        item = tree_personas.item(seleccionado)
        id_persona = item['values'][0]
        db.eliminar_persona(id_persona)
        cargar_personas()

def agregar_habito():
    nombre = entry_habito.get()
    tipo = combo_tipo.get()
    if nombre and tipo:
        db.agregar_habito(nombre, tipo)
        cargar_habitos()
        entry_habito.delete(0, tk.END)
        combo_tipo.set("")
    else:
        messagebox.showwarning("Campos vacíos", "Completar todos los campos")

def eliminar_habito():
    seleccionado = tree_habitos.selection()
    if seleccionado:
        item = tree_habitos.item(seleccionado)
        id_habito = item['values'][0]
        db.eliminar_habito(id_habito)
        cargar_habitos()

def agregar_registro():
    fecha = entry_fecha.get()
    persona = combo_persona.get()
    habito = combo_habito.get()
    cumplido = var_cumplido.get()
    if fecha and persona and habito:
        id_persona = personas_dict[persona]
        id_habito = habitos_dict[habito]
        db.agregar_registro(fecha, id_persona, id_habito, cumplido)
        cargar_registros()
    else:
        messagebox.showwarning("Campos vacíos", "Completar todos los campos")

#CARGAS
def cargar_personas():
    tree_personas.delete(*tree_personas.get_children())
    for p in db.obtener_personas():
        tree_personas.insert("", "end", values=p)
    personas_dict.clear()
    for p in db.obtener_personas():
        personas_dict[p[1]] = p[0]
    combo_persona["values"] = list(personas_dict.keys())

def cargar_habitos():
    tree_habitos.delete(*tree_habitos.get_children())
    for h in db.obtener_habitos():
        tree_habitos.insert("", "end", values=h)
    habitos_dict.clear()
    for h in db.obtener_habitos():
        habitos_dict[h[1]] = h[0]
    combo_habito["values"] = list(habitos_dict.keys())

def cargar_registros():
    tree_registros.delete(*tree_registros.get_children())
    for r in db.obtener_registros():
        tree_registros.insert("", "end", values=r)

#VENTANA
ventana = tk.Tk()
ventana.title("HealthyTrack")
ventana.geometry("600x500")

personas_dict = {}
habitos_dict = {}

tabs = ttk.Notebook(ventana)
tabs.pack(expand=1, fill="both")

#TAB PERSONAS
frame1 = ttk.Frame(tabs)
tabs.add(frame1, text="Personas")

entry_nombre = tk.Entry(frame1)
entry_edad = tk.Entry(frame1)
combo_genero = ttk.Combobox(frame1, values=["Femenino", "Masculino", "Otro"])
btn_agregar_persona = tk.Button(frame1, text="Agregar", command=agregar_persona)
btn_eliminar_persona = tk.Button(frame1, text="Eliminar", command=eliminar_persona)

tk.Label(frame1, text="Nombre").pack()
entry_nombre.pack()
tk.Label(frame1, text="Edad").pack()
entry_edad.pack()
tk.Label(frame1, text="Género").pack()
combo_genero.pack()
btn_agregar_persona.pack(pady=5)
btn_eliminar_persona.pack()

tree_personas = ttk.Treeview(frame1, columns=("ID", "Nombre", "Edad", "Género"), show="headings")
for col in ("ID", "Nombre", "Edad", "Género"):
    tree_personas.heading(col, text=col)
tree_personas.pack(expand=True, fill="both", pady=10)

#TAB HABITOS
frame2 = ttk.Frame(tabs)
tabs.add(frame2, text="Hábitos")

entry_habito = tk.Entry(frame2)
combo_tipo = ttk.Combobox(frame2, values=["Físico", "Mental", "Nutricional"])
btn_agregar_habito = tk.Button(frame2, text="Agregar", command=agregar_habito)
btn_eliminar_habito = tk.Button(frame2, text="Eliminar", command=eliminar_habito)

tk.Label(frame2, text="Nombre del Hábito").pack()
entry_habito.pack()
tk.Label(frame2, text="Tipo").pack()
combo_tipo.pack()
btn_agregar_habito.pack(pady=5)
btn_eliminar_habito.pack()

tree_habitos = ttk.Treeview(frame2, columns=("ID", "Nombre", "Tipo"), show="headings")
for col in ("ID", "Nombre", "Tipo"):
    tree_habitos.heading(col, text=col)
tree_habitos.pack(expand=True, fill="both", pady=10)

#TAB REGISTROS
frame3 = ttk.Frame(tabs)
tabs.add(frame3, text="Registros")

entry_fecha = tk.Entry(frame3)
entry_fecha.insert(0, date.today().strftime("%Y-%m-%d"))
combo_persona = ttk.Combobox(frame3)
combo_habito = ttk.Combobox(frame3)
var_cumplido = tk.BooleanVar()
check = tk.Checkbutton(frame3, text="Cumplido", variable=var_cumplido)
btn_agregar_registro = tk.Button(frame3, text="Registrar", command=agregar_registro)

tk.Label(frame3, text="Fecha (YYYY-MM-DD)").pack()
entry_fecha.pack()
tk.Label(frame3, text="Persona").pack()
combo_persona.pack()
tk.Label(frame3, text="Hábito").pack()
combo_habito.pack()
check.pack()
btn_agregar_registro.pack(pady=5)

tree_registros = ttk.Treeview(frame3, columns=("ID", "Fecha", "Persona", "Hábito", "Cumplido"), show="headings")
for col in ("ID", "Fecha", "Persona", "Hábito", "Cumplido"):
    tree_registros.heading(col, text=col)
tree_registros.pack(expand=True, fill="both", pady=10)

cargar_personas()
cargar_habitos()
cargar_registros()

ventana.mainloop()
