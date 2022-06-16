#imports para utilizar la interfaz grafica
from distutils.cmd import Command
from mimetypes import common_types
from telnetlib import theNULL
import tkinter as tk
from tkinter import ttk
from tkinter import*
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from tkinter.ttk import *
##Interfaz grafica
dadodealta=False
cantalta=200
root = tk.Tk()
root.config(width=800, height=600) #Le damos un tamaño a la ventana
frm = ttk.Frame(root, padding=50)
root.title("Botón en Tk")
frm.grid()
root.title("Bolsa de trabajo | Menú")
#Comienzo de la declaración de las funciones a utilizar
def alta():
    MessageBox.showinfo("Alta a la bolsa de trabajo","Usted ha sido ingresado exitosamente a la bolsa de trabajo")
    dadodealta=True
    cantalta=cantalta+1
def baja():
    MessageBox.showinfo("Baja","Usted ha sido dado de baja exitosamente")
    if dadodealta==True:
        cantalta=cantalta-1
    dadodealta=False
    
def mostrar():
    MessageBox.showinfo("Cantidad de inscriptos",cantalta)
def abrir():
    fichero = FileDialog.askopenfilename(title="Abrir un fichero")
    print(fichero)
def guardar():
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero")
    print(fichero)
#Creacion del menú grafico
ttk.Label(frm, text="1. Alta",).grid(column=1, row=0)
ttk.Button(frm, text="X", command=alta).grid(column=1, row=1)
ttk.Label(frm, text="2. Baja",).grid(column=2, row=0)
ttk.Button(frm, text="X", command=baja).grid(column=2, row=1)
ttk.Label(frm, text="3. Mostrar",).grid(column=3, row=0)
ttk.Button(frm, text="X", command=mostrar).grid(column=3, row=1)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=6, row=6)
menubar = Menu(root)
root.config(menu=menubar)

def acercade():
    MessageBox.showinfo("Estudiantes","Realizado por los alumnos Gastón Toranzo y Carlos Velasquez")

def ayuda():
    MessageBox.showinfo("Materia","Realizado para la materia teoría de lenguajes")

#Definicion de las listas
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.destroy)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda",command=ayuda)
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...",command=acercade)
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
root.mainloop()