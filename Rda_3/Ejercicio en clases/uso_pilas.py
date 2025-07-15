tareas=[]
tareas.append("Estudiar pilas en Python")
tareas.append("Hacer ejercicios de estructuras de datos")
tareas.append("Leer documemtos oficiales de Python")
print("Tareas pendiente", tareas)

# Mostramos la tarea más reciente (el tope de la pila)
if tareas:
    print("Tarea mas reciente", tareas[-1])
else:
    print("No hay tareas pendientes")

# Quitamos la última tarea (la más reciente)
if tareas:
    completada = tareas.pop()
    print("Tarea completada:", completada)
else:
    print("No hay tareas para completar.")

# Verificamos si aún hay tareas pendientes
if len(tareas) == 0:
    print("Todas las tareas han sido completadas.")
else:
    print("Tareas restantes:", tareas)

