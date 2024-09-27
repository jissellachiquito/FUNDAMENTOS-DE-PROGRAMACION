# Crear el diccionario con información
informacion_personal = {
    "nombres": "karla Suarez",
    "edad": 30,
    "ciudad": "Cuenca",
    "profesion": "Ingeniera"
}
print(informacion_personal)

#cambiar y agregar claves
informacion_personal["ciudad"] = "Guayaquil"# acceder a la clave "ciudad" y modificarlo
informacion_personal["profesion"] = "ingeniera civil"# agregar una nueva clave-valor para la profesion
print(informacion_personal)

# Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = ("0991457567")


# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]


# Imprimir el diccionario final
print ("la informacion personal :")
print("nombres :",informacion_personal["nombres"])
print("ciudad :",informacion_personal["ciudad"])
print("profesion: ",informacion_personal["profesion"])
print("telefono: ",informacion_personal["telefono"])

