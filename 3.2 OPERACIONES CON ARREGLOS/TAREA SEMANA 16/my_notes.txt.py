
# Crear y escribir en el archivo my_notes.txt
with open('my_notes.txt', 'w') as file:  # Abre el archivo
    file.write("Estas son mis notas personales:\n")
    file.write("Tarea 1: Hacer la compra \n")  # la primera línea
    file.write("Tarea 2: Estudiar para el examen \n")  # la segunda línea
    file.write("Tarea 3: Limpiar la casa \n")  # la tercera línea

# Leer el archivo my_notes.txt
with open('my_notes.txt', 'r') as file:# Abre el archivo
    # Leer cada línea del archivo
    line = file.readline()  # Lee la primera línea
    while line:  # Mientras haya líneas lee
        print(line.strip())  # Imprime la línea
        line = file.readline()  # Lee la siguiente línea

# El archivo se cierra automáticamente al salir del bloque with



