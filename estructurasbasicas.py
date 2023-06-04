 #Importo tkinter pero la abrevio para uso más sencillo
import tkinter as tk
#Creo y asigno una variable a la función Tk para operar a través de ella
ventana = tk.Tk()

#Creo la ventana donde se ejecutará el programa
ventana.geometry("300x400")
#Selecciono el tamaño de la pantalla


#Creo y asigno una variable a la función Label de tkinter para trabajarla
etiqueta = tk.Label(ventana, text = "Hola", bg = "yellow", font = "Arial 15")
"""
Definición de atributos de Label:
ventana es el lugar donde quiero alojar el Label
text asigna el texto que contendrá
bg "BackGroundColor"
font Tipo de fuente y tamaño
"""

etiqueta.pack(fill=tk.X)
#El método pack coloca los elementos en pantalla
"""
Este método tiene otros atributos como
tk.y que abarca el eje Y con el label
tk.X para el eje X
y tk.BOTH para que los labels ocupen todo el eje x y y al mismo tiempo
"""

#Este segmento permite ubicar un label del lado derecho de la pantalla
etiqueta1 = tk.Label(ventana, text = "Mundo", bg = "blue")
etiqueta1.pack(side = tk.RIGHT)
"""
Se pueden usar otros atributos de localización como
Bottom, Right, Left, Top
"""



#BOTONES

def funcionboton1():
    print("Hola")

def funcionboton2(parametro):
    print(parametro)

boton1 = tk.Button(ventana, text = "Boton Funcion", padx  = 40, pady = 20, command = funcionboton1)
boton1.pack()

"""
Creé un botón que dice "Presiona"
Los atributos padx y pady determinan las dimensiones x y y del botón
El atributo command permite ejecutar una función al presionar el botón
IMPORTANTE: La función, al ser llamada por command, no debe llevar paréntesis
"""

boton2 = tk.Button(ventana, text = "Boton Parametro", padx  = 40, pady = 20, command = lambda: funcionboton2("Parametro Enviado"))
boton2.pack()
"""
El atributo lambda permite enviar parámetros a una función a través del click al botón
Este atributo me permite usar los paréntesis de la función para enviar los parámetros
"""



#CAJAS DE TEXTO PARA LEER DATOS

#Creando función para obtener datos de la caja
def leerdatoscaja():
    texto = CajaTexto.get()
    #.get Recoge los datos de la caja
    print(texto)

CajaTexto = tk.Entry(ventana, font = "Arial 10")
CajaTexto.pack()

#Función corre hasta que se presiona el botón
botonCaja = tk.Button(ventana, text = "Enviar", padx = 20, pady = 12, command = leerdatoscaja)
botonCaja.pack()



#CAJA QUE RECOLECTA TEXTO Y LO IMPRIME EN PANTALLA A TRAVÉS DE UNA ETIQUETA

#Función que recolecta datos de la caja y los asigna a una etiqueta
def leertextoeimprimir():
    textocaja = CajaTexto.get()
    etiqueta2["text"] = textocaja

#Creando la etiqueta que mostrará el texto
etiqueta2 = tk.Label(ventana)
etiqueta2.pack()
#Creando el botón que leerá la info del cuadro de texto y llamará a la función
botonimprimir = tk.Button(ventana, text= "Imprimir", font="Arial", command = leertextoeimprimir)
botonimprimir.pack()

#REORGANIZAR ELEMENTOS EN PANTALLA
#MÉTODO GRID

#SECCIONA LA PANTALLA A TRAVÉS DE 4 FILAS Y 3 COLUMNAS

#Creando elementos para aplicar el método
""""
boton4 = tk.Button(ventana, text = "Botón 1", width = 10, height = 5)
boton5 = tk.Button(ventana, text = "Botón 2", width = 10, height = 5)
boton6 = tk.Button(ventana, text = "Botón 3", width = 10, height = 5)
boton4.grid(row = 3, column = 0)
boton5.grid(row = 3, column = 1)
boton6.grid(row = 3, column = 2)"""

ventana.mainloop()
