def mezcla_natural(lista):
    # Función auxiliar para fusionar dos sublistas ordenadas
    def fusionar(sublista1, sublista2):
        resultado = []
        i, j = 0, 0
        while i < len(sublista1) and j < len(sublista2):
            if sublista1[i] <= sublista2[j]:
                resultado.append(sublista1[i])
                i += 1
            else:
                resultado.append(sublista2[j])
                j += 1
        # Agregar el resto de los elementos
        resultado.extend(sublista1[i:])
        resultado.extend(sublista2[j:])
        return resultado

    # Función principal que ordena la lista utilizando el método de mezcla natural
    def mezcla_natural_recursivo(lista):
        if len(lista) <= 1:
            return lista

        sublistas = []
        temp = [lista[0]]

        # Crear sublistas ordenadas de manera natural
        for i in range(1, len(lista)):
            if lista[i] >= lista[i-1]:
                temp.append(lista[i])
            else:
                sublistas.append(temp)
                temp = [lista[i]]
        sublistas.append(temp)

        print(f"Sublistas creadas: {sublistas}")

        # Fusionar las sublistas
        while len(sublistas) > 1:
            sublistas = [fusionar(sublistas[i], sublistas[i+1]) for i in range(0, len(sublistas)-1, 2)] + sublistas[-1:] if len(sublistas) % 2 == 1 else [fusionar(sublistas[i], sublistas[i+1]) for i in range(0, len(sublistas), 2)]

            print(f"Fusionando sublistas: {sublistas}")

        return sublistas[0]

    return mezcla_natural_recursivo(lista)


# Solicitar datos al usuario
entrada = input("Ingresa una lista de números separados por espacios: ")
lista = list(map(int, entrada.split()))

# Llamar al método de mezcla natural
lista_ordenada = mezcla_natural(lista)

# Imprimir el resultado final
print(f"Lista ordenada: {lista_ordenada}")
