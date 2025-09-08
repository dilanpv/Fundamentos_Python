import tkinter as tk
from tkinter import messagebox
import statistics

class AppNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingreso de Notas")
        self.notas = []

        self.label = tk.Label(root, text="Ingrese la nota 1:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.boton_ingresar = tk.Button(root, text="Ingresar Nota", command=self.ingresar_nota)
        self.boton_ingresar.pack()

        self.resultados = tk.Text(root, height=15, width=50)
        self.resultados.pack()
        self.resultados.config(state='disabled')

    def ingresar_nota(self):
        try:
            nota = float(self.entry.get())
            if nota < 0 or nota > 100:
                raise ValueError("La nota debe estar entre 0 y 100.")
            self.notas.append(nota)
            self.entry.delete(0, tk.END)

            if len(self.notas) < 5:
                self.label.config(text=f"Ingrese la nota {len(self.notas)+1}:")
            else:
                self.mostrar_resultados()
                self.boton_ingresar.config(state='disabled')
                self.entry.config(state='disabled')
                self.label.config(text="Ingreso completo.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def mostrar_resultados(self):
        promedio = sum(self.notas) / len(self.notas)
        notamax = max(self.notas)
        notamin = min(self.notas)
        notamediana = statistics.median(self.notas)

        self.resultados.config(state='normal')
        self.resultados.delete(1.0, tk.END)
        self.resultados.insert(tk.END, "Notas almacenadas:\n")
        for i, nota in enumerate(self.notas):
            self.resultados.insert(tk.END, f"Estudiante {i+1}: {nota}\n")
        self.resultados.insert(tk.END, f"\nPromedio: {promedio:.2f}")
        self.resultados.insert(tk.END, f"\nNota más alta: {notamax}")
        self.resultados.insert(tk.END, f"\nNota más baja: {notamin}")
        self.resultados.insert(tk.END, f"\nMediana: {notamediana}")
        self.resultados.config(state='disabled')

# Crear la ventana principal
root = tk.Tk()
app = AppNotas(root)
root.mainloop()
