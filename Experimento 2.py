import tkinter as tk
import random

titulo = "Fixedsys 25"
letra = "Fixedsys 16"
colorletrafondo = "white"
colorletracaja = "#616161"

fondo = "#FF5F5F"
colorcajas = "#F2F2F2"

jugador1 = "Mario"
jugador2 = "David"
size = 13
turnos = 3
puntos1 = 0
puntos2 = 0

tablero = tk.Tk()
tablero.title("MATRIZ ARITMETICA")

canvastablero = tk.Canvas(tablero, width=(size*11)+200, height=(size*10)+320)
canvastablero.configure(bg=fondo)
canvastablero.pack()

etijugador1 = tk.Label(canvastablero, text=jugador1 + f": {puntos1}", bg=fondo, fg=colorletrafondo, font=letra)
etijugador1.place(x=13, y=10)
etijugador2 = tk.Label(canvastablero, text=jugador2 + f": {puntos1}", bg=fondo, fg=colorletrafondo, font=letra)
etijugador2.place(x=(size*11)+115, y=10)

etiencabezado = tk.Label(canvastablero, text="MATRIZ ARITMÉTICA", font=letra, bg=fondo, fg=colorletrafondo)
etiencabezado.place(x=((size*11)+55)//2, y=60)

tableroframe = tk.Frame(canvastablero, bg=colorcajas)
tableroframe.place(x=20, y=100)

tiemporestante = 25
eticronometro = tk.Label(tablero, text=f"Tiempo restante: {tiemporestante}")
eticronometro.pack()
cronometroiniciado = False

def creartablero():
    for i in range(size):
        for j in range(size):
            numerosecreto = random.randint(0, 12)
            botonmatriz = tk.Button(tableroframe, width=2, height=1, command=lambda row=i, col=j, secret=numerosecreto: revelarnumero(row, col, secret))
            botonmatriz.grid(row=i, column=j)

def revelarnumero(fila, columna, numero):
    global cronometroiniciado
    if not cronometroiniciado:
        iniciarcronometro()
        cronometroiniciado = True
    for widget in tableroframe.winfo_children():
        info = widget.grid_info()
        if info["row"] == fila and info["column"] == columna:
            widget.configure(text=str(numero))
            widget.configure(state=tk.DISABLED)
    
    mostrar_numeros_vecinos(fila, columna)

def mostrar_numeros_vecinos(fila, columna):
    for i in range(fila - 1, fila + 2):
        for j in range(columna - 1, columna + 2):
            if 0 <= i < size and 0 <= j < size and (i != fila or j != columna):
                for widget in tableroframe.winfo_children():
                    info = widget.grid_info()
                    if info["row"] == i and info["column"] == j:
                        widget.configure(state=tk.NORMAL)

def iniciarcronometro():
    global tiemporestante
    if tiemporestante > 0:
        eticronometro.configure(text=f"Tiempo restante: {tiemporestante}")
        tiemporestante -= 1
        tablero.after(1000, iniciarcronometro)
    else:
        eticronometro.configure(text="¡Tiempo terminado!")

creartablero()
iniciarcronometro()

tablero.mainloop()
