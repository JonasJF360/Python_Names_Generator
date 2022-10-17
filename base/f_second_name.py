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
    import verificar_duplicidades as vd
    print(vd.valores_duplicados(base_f_second_name))