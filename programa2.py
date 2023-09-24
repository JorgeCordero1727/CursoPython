#Ejercicio 1
# Definicion de variables (Se puede reemplazar con cualquier cadena)

lista_1 = 'Roberto'
lista_2 = 'Jorge'


def superposicion(lista_x, lista_y):
    for x in  lista_x: # En x se guarda los elementos dentro de la lista x (lista 1)
        for y in lista_y: # En y se guarda los elementos dentro de la lista y (lista 2)
            if x == y :
                return True
    
    return False

print(f'El resultado de la comparacion es: {superposicion(lista_1,lista_2)}')