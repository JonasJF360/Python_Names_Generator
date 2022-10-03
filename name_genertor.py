""" importação das bibliotecas nescessárias """
from random import randint, choice
from base.f_first_name import base_f_first_name
from base.f_second_name import base_f_second_name
from base.last_name import base_last_name
from base.m_first_name import base_m_first_name
from base.m_second_name import base_m_second_name

# Esse é um programa gerador de nomes
# Nele você poderá gerar nomes masculinos
# e femininos com a opção de garar tanto
# o nome completo quanto o nome separado.
# Também é possível gerar uma lista de nomes
# com as mesmas especificações.


def fame_name() -> str:
    """ Gera um nome feminino """
    return choice(base_f_first_name)


def male_name() -> str:
    """ Gera um nome feminino """
    return choice(base_m_first_name)


def generate_name(sexo: str) -> str:
    """ Gera um nome aleatóriamente """
    return male_name() if sexo.upper() == 'M' else fame_name()


def second_name(sexo: str) -> str:
    """ Gera um nome do meio aleatóriamente """
    if sexo.upper() == 'M':
        return choice(base_m_second_name)
    else:  # if sexo == 'F'
        return choice(base_f_second_name)


def last_name() -> str:
    """ Gera um sobrenome aleatóriamente """
    return choice(base_last_name)


def generate_complit_name() -> list:
    """ Retorna uma lista com o nome completo aleatóriamente """
    number = randint(0, 100)
    have_second_name: bool = bool(number > 50 and number % 2)

    sexo: str = 'm' if bool(randint(0, 1)) else 'f'

    if not have_second_name:
        max_size: int = randint(2, 5)
        size_lest_name: int = randint(1, max_size)
        complite_name: list = [generate_name(sexo)]
        while True:
            temp_last_name = last_name()
            if temp_last_name in complite_name:
                continue
            else:
                complite_name.append(temp_last_name)
                size_lest_name -= 1

            if size_lest_name == 0:
                break
    else:
        complite_name: list = [generate_name(
            sexo), second_name(sexo), last_name()]

    return complite_name


if __name__ == '__main__':
    for i in range(200):
        print(f"{i + 1}:\t", " ".join(generate_complit_name()).title())
