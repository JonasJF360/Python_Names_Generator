""" Importação do módulo de garação de números inteiros aleatórios """
from random import randint


def new_cpf() -> str:
    """ Essa função gera um cpf válidado automáticamente """
    novo_cpf: str = ''.join([str(randint(0, 9)) for _ in range(9)])  # 9 números aleatórios
    reverso: int = 10  # Contador reverso
    total: int = 0  # O total das multiplicações

    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9,
            index -= 9  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1  # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            digito: int = 11 - (total % 11)

            if digito > 9:  # Se o digito for > que 9 o valor é 0
                digito = 0
            total = 0  # Zera o total
            novo_cpf += str(digito)  # Concatena o digito gerado no novo cpf

    return f'{novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:]}'


if __name__ == '__main__':
    print(new_cpf())
