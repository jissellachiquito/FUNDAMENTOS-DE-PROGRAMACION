#REALIZAR UNA MATRIZ DE 3X3
matriz = [
    [4, 15, 8],
    [6, 21, 9],
    [8, 3, 5]
]
print(matriz)
#metodo de ordenamiento buble_sort
def buble_sort(fila):
    #algoritmo buble_sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1,i,-1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j - 1] = fila[j - 1], fila[j]
                print(fila)
print('matriz original')
print(matriz)
buble_sort(matriz[1])
print(matriz)


