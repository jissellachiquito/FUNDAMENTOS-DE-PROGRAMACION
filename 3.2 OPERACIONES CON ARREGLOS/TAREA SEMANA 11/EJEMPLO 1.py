#REALIZAR UNA MATRIZ DE 3X3
matriz = [
    [33, 78, 67],
    [20, 50, 89],
    [23, 39, 19]
]
print(matriz)
# FUNCION BUSCAR UN VALOR ESPECIFICO
def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j

valor_buscado = 19
print(buscar_valor(matriz,valor_buscado))

if valor_buscado == valor_buscado:
    print(valor_buscado,',valor correcto,encontrado en la posicion',buscar_valor(matriz,valor_buscado))
else:
    print('valor incorrecto')

