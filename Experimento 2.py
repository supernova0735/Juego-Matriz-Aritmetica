"""
Descripción: Juego Matriz Aritmética - Proyecto Final Progra I
Programadores: David Mayen - 202308035, Mariano Norato - 202308068, Mario Rodríguez - 202307029
Fecha: 05/06/2023
"""
#Importando Bibliotecas
import tkinter as tk
import random
import time

#Definiendo tipografía
titulo = "Fixedsys 25"
letra = "Fixedsys 16"
colorletrafondo = "white"
colorletracaja = "#616161"
#Definiendo Colores
fondo = "#FF5F5F"
colorcajas = "#F2F2F2"
#Variables para el tablero
jugador1 = " "
jugador2 = " "
size = 0
turnos = 0
sumatoria = 0
inicio  = 0 
resultado = 0
#Variable que servirá de contador para determinar el turno actual
turno = 0
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
#Definiendo condiciones y valores del temporizador
tiemporestante = 25
temporizadoriniciado = False
#DEFINIENDO FUNCIONES OPERACIONALES
#Crear Partida
def crearpartida(jugador1, jugador2, size, turnos):
    #Definiendo errores
    etierror = tk.Label(canvasinicio, text="ERROR", font=titulo, fg=colorletrafondo, bg=fondo)
    etivacio = tk.Label(canvasinicio, text="Asegúrese de llenar todos los campos", font=letra, fg=colorletrafondo, bg=fondo)
    etienteros = tk.Label(canvasinicio, text="Tablero y Turnos deben números", font=letra, fg=colorletrafondo, bg=fondo)
    #Validando datos para crear partida
    if not jugador1 or not jugador2 or not size or not turnos or not size.isdigit() or not turnos.isdigit():
        etierror.place(x=375,y=170)
        etivacio.place(x=290,y=235)
        etienteros.place(x=313,y=275)
    else:
        if(turno%2==0):
            jugadoractual = jugador2
        if(turno%2!=0):
            jugadoractual = jugador1
        size = int(size)
        turnos = int(turnos)
        #Creando ventana para el programa
        tablero = tk.Tk()
        tablero.title("MATRIZ ARITMETICA")
        canvastablero = tk.Canvas(tablero)
        etiturno = tk.Label(canvastablero, font=letra, fg=colorletrafondo, bg=fondo,text="Turno de: "+jugadoractual)
        #Creando canvas
        if(size<=13):
            canvastablero.configure(bg=fondo, width=500, height=450)
            canvastablero.pack()
            #Etiquetas de encabezado que muestran los punteos por jugador
            etijugador1 = tk.Label(canvastablero, text=jugador1 + f": {puntos1}", bg=fondo, fg=colorletrafondo, font=letra)
            etijugador1.place(x=13, y=10)
            etijugador2 = tk.Label(canvastablero, text=jugador2 + f": {puntos2}", bg=fondo, fg=colorletrafondo, font=letra)
            etijugador2.place(x=410, y=10)
            #Etiqueta que muestra el nombre del juego
            etiencabezado = tk.Label(canvastablero, text="MATRIZ ARITMÉTICA", font=letra, bg=fondo, fg=colorletrafondo)
            etiencabezado.place(x=180, y=10)
            #Definiendo el Frame del tablero
            tableroframe = tk.Frame(canvastablero, bg=colorcajas)
            tableroframe.place(x=(255-(12*size)), y=100)
            #CREANDO BOTONES DE JUEGO
            boton21=tk.Button(canvastablero, text=f"{opcion1}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
            boton21.place(x=20,y=50)
            boton22=tk.Button(canvastablero, text=f"{opcion2}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
            boton22.place(x=90,y=50)
            boton23=tk.Button(canvastablero, text=f"{opcion3}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
            boton23.place(x=160,y=50)
            boton24=tk.Button(canvastablero, text=f"{opcion4}", font=letra,bg=colorcajas,fg=colorletracaja,padx=15,pady=7)
            boton24.place(x=230,y=50)
            #Etiqueta turnos
            etiturno.place(x=320,y=60)
           
        else:
            canvastablero.configure(bg=fondo, width=800, height=650)
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
            #Etiqueta turnos
            etiturno.place(x=500,y=60)

        etitemporizador = tk.Label(tablero, text=f"Tiempo restante: {tiemporestante}")
        etitemporizador.pack()

        def creartablero():
            for i in range(size):
                for j in range(size):
                    numerosecreto = random.randint(0, 11)
                    botonmatriz = tk.Button(tableroframe, width=2, height=1, command=lambda row=i, col=j, secret=numerosecreto: revelarnumero(row, col, secret))
                    botonmatriz.grid(row=i, column=j)

        def revelarnumero(fila, columna, numero):
            
            inicio = time.time()
            for widget in tableroframe.winfo_children():
                info = widget.grid_info()
                if info["row"] == fila and info["column"] == columna:
                    widget.configure(text=str(numero))
                    widget.configure(state=tk.DISABLED)
    
            mostrar_numeros_vecinos(fila, columna, numero)

        def mostrar_numeros_vecinos(fila, columna, numero):
            global sumatoria
            global resultado 
            resultado = 0
            sumatoria = 0
            for i in range(fila - 1, fila + 2):
                for j in range(columna - 1, columna + 2):
                    if 0 <= i < size and 0 <= j < size and (i != fila or j != columna):
                        for widget in tableroframe.winfo_children():
                            info = widget.grid_info()
                            if info["row"] == i and info["column"] == j:
                                widget.configure(state=tk.NORMAL)
                                numerovecino = random.randint(0, 11)
                                sumatoria = sumatoria + numerovecino
                                resultado = sumatoria * numero
                                #print(sumatoria)
                                widget.configure(text=str(numerovecino))
                                botonesrespuesta(resultado)
        def botonesrespuesta(respuesta):
            opcion = random.randint(1,4)
            if(opcion==1):
                boton21.configure(text=f"{respuesta}")
                valorrandom1 = random.randint(20,1000)
                boton22.configure(text=f"{valorrandom1}", command=lambda: puntos(valorrandom1))
                valorrandom2 = random.randint(20,1000)
                boton23.configure(text=f"{valorrandom2}", command=lambda: puntos(valorrandom2))
                valorrandom3 = random.randint(20,1000)
                boton24.configure(text=f"{valorrandom3}", command=lambda: puntos(valorrandom3))
            if(opcion==2):
                boton22.configure(text=f"{respuesta}")
                valorrandom1 = random.randint(20,1000)
                boton21.configure(text=f"{valorrandom1}", command=lambda: puntos(valorrandom1))
                valorrandom2 = random.randint(20,1000)
                boton23.configure(text=f"{valorrandom2}", command=lambda: puntos(valorrandom2))
                valorrandom3 = random.randint(20,1000)
                boton24.configure(text=f"{valorrandom3}", command=lambda: puntos(valorrandom3))    
            if(opcion==3):
                boton23.configure(text=f"{respuesta}")
                valorrandom1 = random.randint(20,1000)
                boton22.configure(text=f"{valorrandom1}", command=lambda: puntos(valorrandom1))
                valorrandom2 = random.randint(20,1000)
                boton21.configure(text=f"{valorrandom2}", command=lambda: puntos(valorrandom2))
                valorrandom3 = random.randint(20,1000)
                boton24.configure(text=f"{valorrandom3}", command=lambda: puntos(valorrandom3))
            if(opcion==4):
                boton24.configure(text=f"{respuesta}")
                valorrandom1 = random.randint(20,1000)
                boton21.configure(text=f"{valorrandom1}", command=lambda: puntos(valorrandom1))
                valorrandom2 = random.randint(20,1000)
                boton22.configure(text=f"{valorrandom2}", command=lambda: puntos(valorrandom2))
                valorrandom3 = random.randint(20,1000)
                boton23.configure(text=f"{valorrandom3}", command=lambda: puntos(valorrandom3))
            
        def puntos(decision):
            decision = int(decision)
            if(decision==resultado) and (turno%2==0):
                puntos2+=3
                turno+=1
            elif(decision==resultado) and(turno%2!=0):
                puntos1+=3
                turno+=1
            else:
                turno+=1
            #Actualizando Marcador
            if(size<=13):
                etijugador1.configure(text=jugador1+f": {puntos1}")
                etijugador1.place(x=13, y=10)
                etijugador2.configure(text=jugador2+f": {puntos2}")
                etijugador2.place(x=410, y=10)
                etiturno.configure(text="Turno de: "+jugadoractual)
                etiturno.place(x=320,y=60)
            else:
                etijugador1.configure(text=jugador1+f": {puntos1}")
                etijugador1.place(x=20, y=10)
                etijugador2.configure(text=jugador2+f": {puntos2}")
                etijugador2.place(x=700, y=10)
                etiturno.configure(text="Turno de: "+jugadoractual)
                etiturno.place(x=500,y=60)
                
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

#Creando Pantalla de inicio
menuinicio = tk.Tk()
menuinicio.title("Inicio")

#Generando Canvas Inicio
canvasinicio = tk.Canvas(menuinicio, width=600, height=500)
canvasinicio.configure(bg=fondo)
canvasinicio.pack()

#Generando Pantalla de inico

#ENCABEZADOS BIENVENIDA
etimatriz = tk.Label(canvasinicio,text="M A T R I Z", font = titulo, bg = fondo, fg=colorletrafondo)
etimatriz.place(x = 167 , y = 10)
etiaritmetica = tk.Label(canvasinicio,text="A R I T M E T I C A", font = titulo, bg = fondo, fg=colorletrafondo)
etiaritmetica.place(x = 72 , y = 60)
etiencabezadoinfo = tk.Label(canvasinicio, text = "CONFIGURA LA PARTIDA", font = letra, bg=fondo, fg = colorletrafondo)
etiencabezadoinfo.place(x = 20, y = 140)

#CONFIGURACIÓN DE LA PARTIDA
#Etiqueta Jugador 1
etinombrejugador1 = tk.Label(canvasinicio, text = "JUGADOR 1:", font = letra, bg=fondo, fg = colorletrafondo)
etinombrejugador1.place(x = 20, y = 175)
#Caja de Texto Jugador 1
text1jugador1 = tk.Entry(canvasinicio, font=letra, fg=colorletracaja, bg=colorcajas, width=30)
text1jugador1.place(x = 20, y = 210)
#Etiqueta Jugador 2
etinombrejugador2 = tk.Label(canvasinicio, text = "JUGADOR 2:", font = letra, bg=fondo, fg = colorletrafondo)
etinombrejugador2.place(x = 20, y = 250)
#Caja de Texto Jugador 2
text1jugador2 = tk.Entry(canvasinicio, font=letra, fg=colorletracaja, bg=colorcajas, width=30)
text1jugador2.place(x = 20, y = 285)
#Etiqueta Tablero
etitablero = tk.Label(canvasinicio, text = "TAMAÑO N DEL TABLERO (N x N):", font = letra, bg = fondo, fg = colorletrafondo)
etitablero.place(x = 20, y = 325)
#Caja de Texto Tablero
text1tablero = tk.Entry(canvasinicio, font=letra, fg=colorletracaja, bg=colorcajas, width=30)
text1tablero.place(x = 20, y = 360)
#Etiqueta Turnos
etiturnos = tk.Label(canvasinicio, text = "TURNOS PERMITIDOS:", font = letra, bg = fondo, fg = colorletrafondo)
etiturnos.place(x = 20, y = 400)
#Caja de Texto Turnos
text1turnos = tk.Entry(canvasinicio, font=letra, fg=colorletracaja, bg=colorcajas, width=30)
text1turnos.place(x = 20, y = 435)

#BOTON CREAR PARTIDA
boton1crear = tk.Button(canvasinicio, padx = 50, pady = 25,font=letra, fg=colorletracaja, text="CREAR PARTIDA", command= lambda: crearpartida(text1jugador1.get(),text1jugador2.get(),text1tablero.get(),text1turnos.get()))
boton1crear.place(x = 330, y = 335)

menuinicio.mainloop()
