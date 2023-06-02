import tkinter as tk
from datetime import datetime




# Botones de inicio y reinicio
boton_inicio = tk.Button(text="Iniciar", command=lambda: iniciar_temporizador())
boton_inicio.pack(pady=10)

boton_reinicio = tk.Button(text="Reiniciar", command=lambda: reiniciar_temporizador())
boton_reinicio.pack(pady=10)









def actualizar_temporizador():
    global tiempo_restante


    
     # Verificar si el temporizador ha terminado
    if tiempo_restante <= 0:
        etiqueta_temporizador.config(text="00:00")
        return

    # Calcular los minutos y segundos restantes
    minutos = tiempo_restante // 60
    segundos = tiempo_restante % 60

    # Formatear el tiempo restante en formato MM:SS
    tiempo_formateado = "{:02d}:{:02d}".format(minutos, segundos)

    # Actualizar la etiqueta del temporizador
    etiqueta_temporizador.config(text=tiempo_formateado)

    # Actualizar el tiempo restante
    tiempo_restante -= 1

    # Llamar a la función nuevamente después de 1 segundo
    ventana.after(1000, actualizar_temporizador)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Temporizador")

# Variable para almacenar el tiempo restante
tiempo_restante = 25

# Crear una etiqueta para mostrar el temporizador
etiqueta_temporizador = tk.Label(ventana, font=("Arial", 24), text="00:00")
etiqueta_temporizador.pack(pady=20)

# Iniciar el temporizador
actualizar_temporizador()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()