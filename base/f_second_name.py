base_f_second_name: list = [
    'claudia',
    'fernanda',
    'gisela',
    'iasmyn',
    'jaqueline',
    'lorena',
    'maria',
    'nicóly',
    'paula',
    'renata',
    'vitória',
    'yasmin',
]

if __name__ == '__main__':
    # Testar se tem nomes tepetidos
    tirar_repetidos: set = set(base_f_second_name)

    print('[')
    for i in tirar_repetidos:
        print(f"\t'{i}',")
    print(']')
    print(len(base_f_second_name))
    print(len(tirar_repetidos))