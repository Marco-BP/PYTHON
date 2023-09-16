# PROGRAMA PARA MOSTRAR EL FUNCIONAMIENTO DE LA FUNCIÓN 'print' DENTRO Y FUERA DE UN BUCLE 'for'

print("\n")

# Self-introduction
nombre = "Marco"
profesion = "Electrical Engineer & MSc. Information Sistems."
programa = "I'm gonna show you a simple program to create a list of numbers from 1 to 30."
objetivo = "Furthermore, I'm also gonna explain the operation of the 'print' function both inside and outside the for loop."

print('Hello World, my name is', nombre, ",", 'I am', profesion, programa, objetivo, "\n", "\n")

# First option
print("PROGRAM WITH 'print' INSIDE THE 'for' LOOP", "\n")

print("lista_1 = []")
print("for i in range(1,31):")       
print("    lista_1.append(i)")
print("    print(lista_1) \n")  

lista_1 = []
for i in range(1,31):       #Python is a zero-based index language; if you want to fill the list up to 30, you should set 31 as the upper limit in the range
    lista_1.append(i)
    print(lista_1)

print("\n")
print("If you place the 'print' function inside the 'for' loop, it runs in each iteration of the loop. Therefore, every time an element is added to the list, the entire list, including the new element, is printed. This causes the list to be printed multiple times.")

# Para dar un salto de fila entre los 2 codigos
print("\n")

# First option
print("PROGRAM WITH 'print' OUTSIDE THE 'for' LOOP", "\n")

print("lista_2 = []")
print("for i in range(1,31):")       
print("    lista_2.append(i)")
print("print(lista_2) \n")  

lista_2 = []
for i in range(1,31):       #Python is a zero-based index language; if you want to fill the list up to 30, you should set 31 as the upper limit in the range
    lista_2.append(i)
print(lista_2)

print("\n")
print("If you place the 'print' function outside of the 'for' loop, it prints when the loop has finished executing, and the complete list is printed only once.")

# To leave two line breaks between the two code snippets
print("\n" * 2)