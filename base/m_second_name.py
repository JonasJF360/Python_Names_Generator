base_m_second_name: list = [
    'alonsso',
    'carlos',
    'daniel',
    'gabriel',
    'henrique',
    'iury',
    'junior',
    'otávio',
    'nonato',
    'vinicius',
    'yuri',
]

if __name__ == '__main__':
    # Testar se tem nomes tepetidos
    tirar_repetidos: set = set(base_m_second_name)

    print('[')
    for i in tirar_repetidos:
        print(f"\t'{i}',")
    print(']')
    print(len(base_m_second_name))
    print(len(tirar_repetidos))