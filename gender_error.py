""" Configuração necessária para o caso de ser enciado um sexo errado no mapâmetro. """


def gender_error(sexo: str) -> None:
    """ Funsão de erro. é chamada quano se passa uma opção de sexo inválida. """
    if sexo.upper() != 'M' and sexo.upper() != 'F':
        raise AttributeError(
            f"Parametro '{sexo}' inválido: Use 'm' para masculino, 'f' para feminino ou deixe vazio para o sistema escolher sozinho.")
