# PROGRAMA PARA MOSTRAR EL FUNCIONAMIENTO DE LA FUNCIÓN 'print' DENTRO Y FUERA DE UN BUCLE 'for'

print("\n")

# Presentación inicial
nombre = "Marco"
profesion = "Electrical Engineer"
programa = "I'm gonna show you a simple program to make a list of numbers from 1 to 30",
objetivo = "Furthermore, I'm also gonna explain the operation of the 'print' function both inside and outside the for loop."

print('Hello World, my name is', nombre, ",", 'I am', profesion, programa, objetivo, "\n", "\n")

# Primera opción
print("PROGRAMA CON EL 'print' DENTRO DEL BUCLE 'for'", "\n")
lista_1 = []
for i in range(1,30):
    lista_1.append(i)
    print(lista_1)

# Para dar un salto de fila entre los 2 codigos
print("\n")

# Segunda opción
print("PROGRAMA CON EL 'print' FUERA DEL BUCLE 'for'", "\n")
lista_2 = []
for i in range(1,30):
    lista_2.append(i)
print(lista_2)

# Para dar dos saltos de fila entre los 2 codigos
print("\n" * 2)