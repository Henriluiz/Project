# Objetivo: Consolidar seus conhecimentos em Python através de um exercício abrangente que explore diversos conceitos e estruturas de dados.

# Enunciado:

# Crie um programa que simule um sistema de gerenciamento de uma biblioteca. O programa deve permitir:

# Cadastro de livros:
# - Título
# - Autor(es)
# - Ano de publicação
# - Gênero
# - Disponibilidade (True/False)
# Consulta de livros:
# - Por título
# - Por autor
# - Por gênero
# - Por disponibilidade
# Empréstimo de livros:
# - Verificar disponibilidade do livro
# - Atualizar status do livro para "emprestado"
# Devolução de livros:
# - Atualizar status do livro para "disponível"
# Relatórios:
# - Livros mais emprestados
# - Livros menos emprestados
# - Livros por gênero
# - Livros disponíveis
# - Livros emprestados

generos = ['Educacional'
           ,'Romance'
           , 'Fantasia'
           , 'Ficção Científica'
           , 'Suspense'
           , 'Mistério'
           , 'Terror'
           ,'Histórica',
            'Biografia', 
            'Poesia',
            'Infantil']

base_de_dados_dos_livros = "livros.json"

def ler_livros(name_arq):
    """Criação e Atualização de Arquivo em CSV 

    Args:
        dados (dict): dado que será salvo no arquivo
    """
    import json
    with open(name_arq, 'r', encoding='utf-8') as f:
        livros = json.load(f)
    
    # Iterando sobre todos os livros e imprimindo seus títulos
    if isinstance(livros, list):  # Verifica se é uma lista
        for i, dicionario in enumerate(livros):
            print(f'Nº{i + 1}\nNome: {dicionario['Nome']}\n'
                  f'Autor: {dicionario['Autor']}\n'
                  f'Gênero: {dicionario['Gênero']}\n'
                  f'Ano de Publicação: {dicionario['Ano de Publicação']}')
            print('-' * 25)
    else:
        print("O arquivo JSON não contém uma lista.")
    
    # print(len(livros))
    # for cont in range(0,len(livros)):
    #     print(f'Nº {cont}', end=" ")
    #     for chave, valor in livros.items():
    #         print(f"\033[4;33m{chave}\033[m: \033[4m{valor}\033[m")
    # ! ATÉ AQUI
    
        
def salvar_livros(name_arq,livro):
    """Salvar e alterar dados do livros

    Args:
        dados (JSON): base de dados onde se encontra os livros
    """
    import json
    with open(name_arq, 'w', encoding="utf-8") as f:
        json.dump(livro, f, indent=4)
    # Inacabado
    
base_dict = {'Nome': 'Manual do Mundo', 'Autor': 'Pedro', 'Gênero': 'Mistério', 'Ano de Publicação': \
              2020,'Disponibilidade': "True"}
# print(livro_dict)
# salvar_livros(name_arq=base_de_dados_dos_livros, livro=livro_dict)
ler_livros(base_de_dados_dos_livros)


def cadastro_livro():
    livro = {}
    livro_name = str(input('Nome do Livro: '))
    livro['Nome'] = livro_name
    autor = str(input('Autor do Livro: '))
    livro['Autor'] = autor
    ano_publicacao = int(input('Ano de Publicação: '))
    if not len(str(ano_publicacao)) == 4:
        ano_publicacao = int(input('Ano de Publicação: '))
    
    cont = 0
    for item in generos:
        print(f'{cont}º > {item}')
        cont += 1
    genero = int(input('Gênero: '))
    if 0 > genero > len(generos):    
        genero = int(input('Gênero: '))
    livro['Gênero'] = generos[genero]
    livro['Ano de Publicação'] = ano_publicacao

    disponivel = input('Disponível: ').upper() # Errado
    if 'Ss' in disponivel:
        livro['Disponibilidade'] = True
    elif 'Nn' in disponivel: 
        livro['Disponibilidade'] = False
    else:
        disponivel = input('Disponível: ').upper() # Tudo isso
        
    return livro
