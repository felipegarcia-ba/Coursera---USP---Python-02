def bubble_sort(lista):
    loop = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True

        for i in range(loop):
            if lista[i] > lista[i+1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False
        print(lista)
    return lista