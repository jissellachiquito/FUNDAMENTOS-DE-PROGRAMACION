# Abrir el archivo my_notes.txt en modo escritura ('w') para agregar tres nuevas notas personales
archivo_escritura = open('my_notes.txt', 'w')

# Escribir tres nuevas notas personales, cada una en una línea diferente
archivo_escritura.write("Estas son mis notas personales:\n")
archivo_escritura.write("Nota 1: Hacer las compras.\n")
archivo_escritura.write("Nota 2: Estudiar para el examen.\n")
archivo_escritura.write("Nota 3: Limpiar la casa por la tarde.\n")

# Cerrar el archivo después de escribir las notas
archivo_escritura.close()

# Abrimos el archivo nuevamente en modo lectura ('r') para leer y mostrar las notas
archivo_lectura = open('my_notes.txt', 'r')

# Leer el archivo línea por línea utilizando readline() y mostramos cada línea
linea = archivo_lectura.readline()  # Leemos la primera línea
while linea:
    print(linea.strip())  # Mostramos la línea sin el salto de línea al final
    linea = archivo_lectura.readline()  # Leemos la siguiente línea

# Cerramos el archivo después de leerlo
archivo_lectura.close()



