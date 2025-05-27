#2. Se desea realizar un programa en donde se capture el nombre y tres calificaciones para
#5 estudiantes de la facultad de Ingeniería, y después se pueda procesar dándonos el
#promedio final de cada uno de los alumnos, el resultado se mostrará en pantalla.

cant_estudiante = 5
cant_materia = 3
#Definimos el numero de estudiantes y materias para nuestro bucle

estudiante = []
#Se crea una lista vacía para ingresar el nombre de los estudiantes y luego sus notas

for alumno in range(cant_estudiante):
    nombre = (input(f"Ingrese el nombre del estudiante {cant_estudiante}: "))
    nota = []
    #Se crea un bucle para obtener el nombre del estudiante y se  crea una lista vacía para almacenar las notas
    
    for asignatura in range(cant_materia):
        while True:
            calificacion = float(input(f"Ingrese la nota {cant_materia} del estudiante {nombre}; "))
            #Cree un while true para una validación de error
            
            if calificacion <0 or calificacion > 100: 
            #Si no se cumple la condición, le saltara el error 
                print("ERROR, INGRESE UNA NOTA VÁLIDA [0 - 100]: ") 
                break      
        nota.append(calificacion) 
        #Al arreglo nota se le introduce los valores de las calificaciones
    estudiante.append([nombre] + nota)      
    #Al arreglo estudiante se le introduce los nombres y el arreglo nota
    


print("n\ Resumen ")
print(f"{'Nombre':<15} {'Calificación 1':<15} {'Calificación 2':<15} {'Calificación 3':<15} {'Promedio':<10}")
print("=" * 70)
for n_alumnos in estudiante:
    print(f"{estudiante[0]:<15} {estudiante[1]:<15.2f} {estudiante[2]:<15.2f} {estudiante[3]:<15.2f} {estudiante[4]:<10.2f}") 
    #Se imprime cada estudiante por su posición con su respectiva nota
