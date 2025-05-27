n = int(input("Filas (1-9): "))
m = int(input("Columnas (1-9): "))

matriz = []
i = 0
while i < n:
    fila = []
    j = 0
    while j < m:
        valor = int(input(f"Valor [{i}][{j}]: "))
        fila = fila + [valor]
        j = j + 1
    matriz = matriz + [fila]
    i = i + 1

print("Matriz ingresada:")
i = 0
while i < n:
    print(matriz[i])
    i = i + 1

print("Suma de cada fila:")
i = 0
while i < n:
    suma = 0
    j = 0
    while j < m:
        suma = suma + matriz[i][j]
        j = j + 1
    print("Fila", i, "=", suma)
    i = i + 1

print("Promedio de cada columna:")
j = 0
while j < m:
    suma = 0
    i = 0
    while i < n:
        suma = suma + matriz[i][j]
        i = i + 1
    print("Columna", j, "=", suma / n)
    j = j + 1

mayor = matriz[0][0]
f_mayor = 0
c_mayor = 0
i = 0
while i < n:
    j = 0
    while j < m:
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            f_mayor = i
            c_mayor = j
        j = j + 1
    i = i + 1

print("Mayor valor:", mayor, "en fila", f_mayor, "columna", c_mayor)


