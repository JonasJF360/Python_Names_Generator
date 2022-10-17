base_m_second_name: list = [
    'alonsso',
    'carlos',
    'daniel',
    'gabriel',
    'henrique',
    'iury',
    'junior',
    'otávio',
    'vinicius',
    'yuri',
]

if __name__ == '__main__':
    # Testar se tem nomes tepetidos
    import verificar_duplicidades as vd
    print(vd.valores_duplicados(base_m_second_name))
