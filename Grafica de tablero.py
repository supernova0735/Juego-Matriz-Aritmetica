import tkinter as tk

def graficar_matriz(matriz):
    

    ventana = tk.Tk()
    ventana.title("Gráficar Matriz")
    
    
    lienzo = tk.Canvas(ventana, width=400, height=400)
    lienzo.pack()
    
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    
    ancho_celda = 400 / columnas
    alto_celda = 400 / filas
    
    
    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i][j]
            

            x0 = j * ancho_celda
            y0 = i * alto_celda
            x1 = x0 + ancho_celda
            y1 = y0 + alto_celda
         
            lienzo.create_rectangle(x0, y0, x1, y1, fill=color(valor))
    
   
    ventana.mainloop()

def color(valor):
   
    if valor < 0.5:
        return "white"
    else:
        return "black"

matriz_ejemplo = [[0, 1, 0, 1],
                  [1, 0, 1, 0],
                  [0, 1, 0, 1],
                  [1, 0, 1, 0]]


graficar_matriz(matriz_ejemplo)