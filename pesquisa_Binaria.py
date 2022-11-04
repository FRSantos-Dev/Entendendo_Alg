def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) / 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meo - 1
        else:
            baxo = meio + 1
        return None