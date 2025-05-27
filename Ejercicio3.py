matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

linealizado = []
for j in 0,1,2:
    for fila in matriz:
        linealizado = linealizado + [fila[j]]

print("Matriz linealizada por columnas:")
print(linealizado)
