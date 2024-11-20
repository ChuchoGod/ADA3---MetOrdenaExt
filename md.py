def merge_sort(lista):
    print(f"Dividiendo lista: {lista}")
    if len(lista) <= 1:
        print(f"Retornando lista base: {lista}")
        return lista
    
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    return intercalar(izquierda, derecha)

def intercalar(izquierda, derecha):
    print(f"Intercalando {izquierda} y {derecha}")
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        print(f"Comparando: {izquierda[i]} y {derecha[j]}")
        if izquierda[i] < derecha[j]:
            print(f"Agregando {izquierda[i]} al resultado")
            resultado.append(izquierda[i])
            i += 1
        else:
            print(f"Agregando {derecha[j]} al resultado")
            resultado.append(derecha[j])
            j += 1
    
    print(f"Agregando elementos restantes de izquierda: {izquierda[i:]}")
    resultado.extend(izquierda[i:])
    print(f"Agregando elementos restantes de derecha: {derecha[j:]}")
    resultado.extend(derecha[j:])
    
    print(f"Resultado intercalado: {resultado}")
    return resultado

# Solicitar datos al usuario
lista = list(map(int, input("Introduce los elementos de la lista desordenada, separados por espacios: ").split()))
print("Lista original:", lista)
print("Lista ordenada:", merge_sort(lista))
