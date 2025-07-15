#Crear un codigo que elimine los valores duplicados

lista=[1,2,3,5,5,6,7,8]
N_lista=[]
for num in lista:
    try:
        lista.remove(5)
    except ValueError:
        pass
print(N_lista)

