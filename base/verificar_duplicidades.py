def valores_duplicados(dados) -> str:
    """ Mostrar Valores repetidos """
    valores = []
    repetidos = set()
    for dado in dados:
        if dado not in valores:
            valores.append(dado)
        else:
            repetidos.add(dado)
    return f'> Duplicado: {repetidos}' if len(repetidos) > 0 else '> Não há duplicidades'
