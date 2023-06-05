import tkinter as tk
import random

#Definiendo tipografía
titulo = "Fixedsys 25"
letra = "Fixedsys 16"
colorletrafondo = "white"
colorletracaja = "#616161"

#Definiendo colores a utilizar
fondo = "#FF5F5F"
colorcajas = "#F2F2F2"

#Definiendo variables que contienen el nombre de los jugadores
jugador1 = "Mario"
jugador2 = "David"
#Variable que define el tamaño de la matriz (n x n)
size = 13
#Limites: 3 - 20
#Variable que define la cantidad de turnos disponibles por jugador
turnos = 3
#Variables que definen los respectivos punteos
puntos1 = 0
puntos2 = 0
#Variable que almacenará el producto de la sumatoria de los números de la periferia con el número central
total = 0
#Definiendo opciones de texto para los botones, estos valores se modificarán aleatoriamente para que le usuario escoja posibles respuestas
opcion1 = 0
opcion2 = 0
opcion3 = 0
opcion4 = 0
#Creando ventana para el programa
tablero = tk.Tk()
tablero.title("MATRIZ ARITMETICA")
#Creando canvas
if(size<=13):
    canvastablero = tk.Canvas(tablero, width=400, height=450)
    canvastablero.configure(bg=fondo)
    canvastablero.pack()
    #Etiquetas de encabezado que muestran los punteos por jugador
    etijugador1 = tk.Label(canvastablero, text=jugador1 + f": {puntos1}", bg=fondo, fg=colorletrafondo, font=letra)
    etijugador1.place(x=13, y=10)
    etijugador2 = tk.Label(canvastablero, text=jugador2 + f": {puntos2}", bg=fondo, fg=colorletrafondo, font=letra)
    etijugador2.place(x=310, y=10)
    #Etiqueta que muestra el nombre del juego
    etiencabezado = tk.Label(canvastablero, text="MATRIZ ARITMÉTICA", font=letra, bg=fondo, fg=colorletrafondo)
    etiencabezado.place(x=132, y=10)
    #Definiendo el Frame del tablero
    tableroframe = tk.Frame(canvastablero, bg=colorcajas)
    tableroframe.place(x=(205-(12*size)), y=100)
    #Botones opciones para responder
    boton21=tk.Button(canvastablero, text=f"{opcion1}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
    boton21.place(x=20,y=50)
    boton22=tk.Button(canvastablero, text=f"{opcion2}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
    boton22.place(x=90,y=50)
    boton23=tk.Button(canvastablero, text=f"{opcion3}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
    boton23.place(x=160,y=50)
    boton24=tk.Button(canvastablero, text=f"{opcion4}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
    boton24.place(x=230,y=50)
else:
    canvastablero = tk.Canvas(tablero, width=800, height=650)
    canvastablero.configure(bg=fondo)
    canvastablero.pack()
    #Etiquetas de encabezado que muestran los punteos por jugador
    etijugador1 = tk.Label(canvastablero, text=jugador1 + f": {puntos1}", bg=fondo, fg=colorletrafondo, font=letra)
    etijugador1.place(x=20, y=10)
    etijugador2 = tk.Label(canvastablero, text=jugador2 + f": {puntos2}", bg=fondo, fg=colorletrafondo, font=letra)
    etijugador2.place(x=700, y=10)
    #Etiqueta que muestra el nombre del juego
    etiencabezado = tk.Label(canvastablero, text="MATRIZ ARITMÉTICA", font=letra, bg=fondo, fg=colorletrafondo)
    etiencabezado.place(x=330, y=10)
    #Definiendo el Frame del tablero
    tableroframe = tk.Frame(canvastablero, bg=colorcajas)
    tableroframe.place(x=(405-(12*size)), y=100)
    #Botones opciones para responder
    boton21=tk.Button(canvastablero, text=f"{opcion1}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
    boton21.place(x=170,y=50)
    boton22=tk.Button(canvastablero, text=f"{opcion2}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
    boton22.place(x=240,y=50)
    boton23=tk.Button(canvastablero, text=f"{opcion3}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
    boton23.place(x=310,y=50)
    boton24=tk.Button(canvastablero, text=f"{opcion4}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
    boton24.place(x=380,y=50)



#Definiendo condiciones y valores del temporizador
tiemporestante = 25
etitemporizador = tk.Label(tablero, text=f"Tiempo restante: {tiemporestante}")
etitemporizador.pack()
temporizadoriniciado = False

def creartablero():
    for i in range(size):
        for j in range(size):
            numerosecreto = random.randint(0, 11)
            botonmatriz = tk.Button(tableroframe, width=2, height=1, command=lambda row=i, col=j, secret=numerosecreto: revelarnumero(row, col, secret))
            botonmatriz.grid(row=i, column=j)

def revelarnumero(fila, columna, numero):
    global temporizadoriniciado
    if not temporizadoriniciado:
        iniciartemporizador()
        temporizadoriniciado = True
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
                        numerovecino = random.randint(0, 11)
                        widget.configure(text=str(numerovecino))

def iniciartemporizador():
    global tiemporestante
    if tiemporestante > 0:
        etitemporizador.configure(text=f"Tiempo restante: {tiemporestante}")
        tiemporestante -= 1
        tablero.after(1000, iniciartemporizador)
    else:
        etitemporizador.configure(text="¡Tiempo terminado!")

creartablero()
iniciartemporizador()

tablero.mainloop()
