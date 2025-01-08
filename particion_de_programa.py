# asignacion de variables
tam_part = 0
tam_tarea = 0
tareas = []
particiones = [[32000],[0]]
n_tar = 0
tar_elim = 0
respuesta = ""
tar_cola = []
n_tar_cola = 0
print ("el tamaño de su memoria es 32'000 KB (KB = kilobytes).\n")

#creacion de las tareas y particiónes
respuesta = input("¿desea crear una particion de memoria? (si/no): ")

while(respuesta == "si"): #bucle para crear particiones
    tam_part = int(input("ingrese el tamaño de la partición en kilobytes: "))
    if(tam_part >= particiones[0][0] or tam_part <= 0):    
        print("El valor de la partición no es valido.")
    else:
        particiones[0].append(tam_part)
        particiones[1].append(0)
        particiones[0][0] -= tam_part
    print(f"particiones en la memoria: {particiones[0]}")
    respuesta = input("¿desea agregar otra partición? (si/no): ")

respuesta = input("¿desea crear una tarea? (si/no): " )

while(respuesta == "si"): #bucle para crear tareas
    tam_tarea = int(input("ingrese el tamaño de la tarea en kilobytes: "))
    if(tam_tarea >= 0):
        tareas.append(tam_tarea)
        n_tar +=1 
    else:
        print("el tamaño ingresado es invalido...\n")
    print(f"el tamaño de las tareas es: {tareas}\n")
    respuesta = input("¿desea agregar otra tarea? (si/no): ")
print(f"el tamaño de las tareas es: {tareas}\n")
respuesta = input("¿Desea eliminar una tarea? (si/no): ")

#bucle para mostrar que tareas no lograron guardarse
for i in range(n_tar):
    if(not(tareas[i] in particiones[1])):
        tar_cola.append(tareas[i])
        print(f"\nla tarea #{i+1} con tamano {tareas[i]}kb no cabe en ninguna particion.")
        
while(respuesta == "si"):#bucle para eliminar tareas
    tar_elim = int(input("ingrese la posicion de la tarea a eliminar: "))
    for i in range(n_tar):
        if((tar_elim-1) == i):
            tareas[i] = 0
    respuesta = input("¿Desea eliminar otra tarea?:")
    
print(f"las tareas a organizar son: {tareas}\n")
tareas = sorted(tareas, reverse=True)  # Organizar la lista de tareas para evitar errores
# Dos for para organizar las tareas en las particiones
for i in range(n_tar):
    for tamano, espacio in zip(particiones[0], particiones[1]):
        if tareas[i] <= tamano:
            if(espacio == 0):
                particiones[1][particiones[1].index(espacio)] = tareas[i]  # Asignar tarea
                break

#un bucle for para mostrar el orden de las tareas en las particiones
print("las tareas ordenadas son: \n")
for i in range(len(particiones[0])):
    print(f"particion #{i+1} - {particiones[1][i]}")
print(f"\nlas tareas en cola son: {tar_cola}")
#insertar las tareas en la cola en las particiones
if(len(tar_cola) <= 1):
    print("fin")
else:
    respuesta = input("¿Desea reemplazar una tarea? (si/no):")
    print(f"las tareas en cola son: {tar_cola}")
    while(respuesta == "si"):
        n_tar = int(input("ingrese la pocision de la tarea que desea reemplazar: "))
        n_tar_cola = int(input("ingrese la posicion de la tarea que quiera ejecutar: "))
        if(particiones[1][n_tar-1] >= tar_cola[n_tar_cola-1]):
            tar_cola.append(particiones[1][n_tar-1])
            particiones[1][n_tar-1] = tar_cola[n_tar_cola-1]
            del tar_cola[n_tar_cola-1]
        else:
            print("la particion selecionada no es valida")
        respuesta = input("¿Desea reemplazar otra tarea? (si/no):")
        
    for i in range(len(particiones[0])):
        print(f"particion #{i+1} - {particiones[1][i]}")
    print(f"\nlas tareas en cola son: {tar_cola}")