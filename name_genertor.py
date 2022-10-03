""" importação das bibliotecas nescessárias """

from random import randint, choice
from typing import NoReturn
from base.f_first_name import base_f_first_name
from base.f_second_name import base_f_second_name
from base.last_name import base_last_name
from base.m_first_name import base_m_first_name
from base.m_second_name import base_m_second_name
from base.cpf_generator import new_cpf

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


def gender_error(sexo: str) -> NoReturn:
    raise RuntimeError(f"Parametro '{sexo}' inválido: Use 'm' para masculino, 'f' para feminino ou deixe vazio para o sistema escolher sozinho.")


def generate_name(sexo: str) -> str:
    """ Gera um nome aleatóriamente """
    if sexo.upper() != 'M' and sexo.upper() != 'F':
        gender_error(sexo)
    return male_name() if sexo.upper() == 'M' else fame_name()


def second_name(sexo: str) -> str:
    """ Gera um nome do meio aleatóriamente """
    if sexo.upper() != 'M' and sexo.upper() != 'F':
        gender_error(sexo)

    return choice(base_m_second_name) if sexo.upper() == 'M' else choice(base_f_second_name)


def last_name() -> str:
    """ Gera um sobrenome aleatóriamente """
    return choice(base_last_name)


def generate_complit_name(sexo: str = 'n') -> list:
    """ Retorna uma lista com o nome completo aleatóriamente """
    number = randint(0, 100)
    have_second_name: bool = bool(number > 50 and number % 2)

    if sexo == 'n':
        sexo = 'm' if bool(randint(0, 1)) else 'f'

    name: str = generate_name(sexo)
    complite_name: list = [name]

    if have_second_name:
        while True:
            temp_second_name: str = second_name(sexo)
            if temp_second_name == name:
                continue
            complite_name.append(temp_second_name)
            break

    size_lest_name: int = randint(1, randint(2, randint(3, 5)))

    while True:
        temp_last_name = last_name()
        if temp_last_name in complite_name:
            continue

        complite_name.append(temp_last_name)
        size_lest_name -= 1

        if size_lest_name == 0:
            break

    return complite_name


if __name__ == '__main__':
    for i in range(10):
        print(f"{i + 1}:\t{new_cpf()}\t", " ".join(generate_complit_name('m')).title())

    print()
    for i in range(10):
        print(f"{i + 1}:\t{new_cpf()}\t", " ".join(generate_complit_name('f')).title())

    print()
    for i in range(10):
        print(f"{i + 1}:\t{new_cpf()}\t", " ".join(generate_complit_name()).title())
