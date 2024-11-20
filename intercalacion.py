def intercalacion(lista1, lista2):
    print("Iniciando intercalación...")
    i = j = 0
    resultado = []
    
    while i < len(lista1) and j < len(lista2):
        print(f"Comparando: {lista1[i]} y {lista2[j]}")
        if lista1[i] < lista2[j]:
            print(f"Agregando {lista1[i]} al resultado")
            resultado.append(lista1[i])
            i += 1
        else:
            print(f"Agregando {lista2[j]} al resultado")
            resultado.append(lista2[j])
            j += 1
    
    print(f"Agregando elementos restantes de la lista1: {lista1[i:]}")
    resultado.extend(lista1[i:])
    print(f"Agregando elementos restantes de la lista2: {lista2[j:]}")
    resultado.extend(lista2[j:])
    
    print("Intercalación completada.")
    return resultado

# Solicitar datos al usuario
lista1 = list(map(int, input("Introduce los elementos de la primera lista ordenada, separados por espacios: ").split()))
lista2 = list(map(int, input("Introduce los elementos de la segunda lista ordenada, separados por espacios: ").split()))

# Asegurarse de que las listas estén ordenadas antes de intercalarlas
lista1.sort()
lista2.sort()

print("Lista ordenada:", intercalacion(lista1, lista2))
