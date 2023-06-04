import tkinter as tk
import random

class Tablero:
    def __init__(self, root):
        self.root = root
        self.root.title("Tablero Ajustable")
        
        # Variables para el tamaño del tablero
        self.num_filas = tk.IntVar()
        self.num_columnas = tk.IntVar()
        
        # Crear los widgets
        self.label_filas = tk.Label(root, text="Número de filas:")
        self.label_filas.pack()
        
        self.entry_filas = tk.Entry(root, textvariable=self.num_filas)
        self.entry_filas.pack()
        
        self.label_columnas = tk.Label(root, text="Número de columnas:")
        self.label_columnas.pack()
        
        self.entry_columnas = tk.Entry(root, textvariable=self.num_columnas)
        self.entry_columnas.pack()
        
        self.button_crear_tablero = tk.Button(root, text="Crear Tablero", command=self.crear_tablero)
        self.button_crear_tablero.pack()
        
        self.tablero_frame = tk.Frame(root)
        self.tablero_frame.pack()
        
        #  cronómetro
        self.tiempo_restante = 25
        self.cronometro_label = tk.Label(root, text="Tiempo restante: 25")
        self.cronometro_label.pack()
        
        # controlar si el cronómetro ya ha comenzado
        self.cronometro_iniciado = False
        
    def crear_tablero(self):
        # Limpiar el tablero existente
        for widget in self.tablero_frame.winfo_children():
            widget.destroy()
        
        # Obtener el tamaño del tablero
        filas = self.num_filas.get()
        columnas = self.num_columnas.get()
        
        # Crear los botones del tablero con números secretos
        for i in range(filas):
            for j in range(columnas):
                numero_secreto = random.randint(1, 100)  # Generar un número secreto aleatorio
                button = tk.Button(self.tablero_frame, width=2, height=1, command=lambda row=i, col=j, secret=numero_secreto: self.revelar_numero(row, col, secret))
                button.grid(row=i, column=j)
        
    def revelar_numero(self, fila, columna, numero):
        if not self.cronometro_iniciado:
            self.iniciar_cronometro()  # Iniciar el cronómetro solo con el primer clic en el tablero
            self.cronometro_iniciado = True
        
        # Encontrar el botón correspondiente y actualizar su texto
        for widget in self.tablero_frame.winfo_children():
            info = widget.grid_info()
            if info["row"] == fila and info["column"] == columna:
                widget.configure(text=str(numero))
                widget.configure(state=tk.DISABLED)  # Desactivar el botón después de revelar el número

    def iniciar_cronometro(self):
        if self.tiempo_restante > 0:
            self.cronometro_label.configure(text=f"Tiempo restante: {self.tiempo_restante}")
            self.tiempo_restante -= 1
            self.root.after(1000, self.iniciar_cronometro)
        else:
            self.cronometro_label.configure(text="¡Tiempo terminado!")
        
# Crear la ventana principal
root = tk.Tk()

# Crear el objeto Tablero
tablero = Tablero(root)

# Ejecutar la aplicación
root.mainloop()
