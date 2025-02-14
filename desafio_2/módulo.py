# 3 Functions of another file

def eh_numero_inteiro_loop(cpf_sem_pontos):
    for num in cpf_sem_pontos:
        if not num.isnumeric():
            if not num == '.' or num == '-':
                return False
    return True

def digito(cpf, digito_1 = True):
    somar = 0
    if digito_1:
        contagem = 10
    else:
        contagem = 11
    visuar_somar = '>>'
    for ind, valor in enumerate(cpf):
        calculo = int(cpf[ind]) * contagem
        visuar_somar = visuar_somar + f' {calculo} +'
        somar += calculo
        if contagem == 2:
            break
        contagem -= 1
    multiplicar = somar * 10 
    digito_base = multiplicar % 11
    digito = 0 if digito_base > 9 else digito_base
    return digito

def verificado_cpf():
    """Verificado de CPFs

    Returns:
        int: CPF convertido e verificado, caso ao contrário returne False
    """
    sair = False
    while True:
        entrada = str(input('Digite o CPF: '))
        if entrada.isdecimal:
            convertendo = entrada.replace('.','').replace('-','')
            verificando_num = eh_numero_inteiro_loop(convertendo)
            primeiro_num = entrada[0] * len(entrada)
            if entrada == primeiro_num:
                print('\033[1;31mCPF INVÁLIDO!\033[m')
                continue
            try:
                entrada_int = int(entrada)
            except ValueError:
                entrada_int = 14 # Quantidades de números, se '.' e '-'
            else:
                entrada_int = 11 # Caracteres em um cpf com '.' e '-'
            if verificando_num:
                if entrada_int == 14:
                    if not entrada[3] == '.':
                        print('CPF Inválido, pontos no lugares errados!')
                        continue
                    elif not entrada[7] == '.':
                        print('CPF Inválido, pontos no lugares errados!')
                        continue
                    elif not entrada[11] == '-':
                        print('CPF Inválido, pontos no lugares errados!')
                        continue
            else:
                print('Digite números inteiros!')
                continue
            if len(entrada) == entrada_int:
                cpf = convertendo
                break
            else:
                print('CPF Inválido')
        else:
            print('CPF Inválido, tente novamente')
            cpf = False
    
    digito1 = digito(cpf)
    digito2 = digito(cpf,digito_1=False)
    if int(cpf[-2]) == digito1 and int(cpf[-1]) == digito2:
        return cpf
    else:
        return False


def fecha_programa():
  import sys
  sys.exit()

     
def encontrararquivo(nome):
  try:
    teste = open(nome, "rt")
    teste.close()
  except FileNotFoundError:
    return False
  else:
    return True

def criararquivo(nome):
  try:
    criar = open(nome, 'wt+')
    criar.close()
  except:
    print('Houve um erro na criação do arquivo')
  else:
    print(f'Arquivo {nome} criado com sucesso!')

# ------------------------------------------------------------------------------------

def linha(msg, escolha=3):
    """ Títulos já pré feitos

    Args:
        msg (str): Mensagem para o título
        escolha (int, optional): Escolha 1:
        ------------------------------
          Cadastro de Funcionário    
        ------------------------------
        Escolha 2:
        =========Funcionário==========
        Deixando Vazio: 
        ------------------------------
    """
    if escolha == 1:
        print('-' * 30)
        print(f'{msg:^30}')
        print('-' * 30)
    elif escolha == 2:
        print(f'{msg:=^30}')
    else:
        print('-' * 30)

def cls():
    import os
    return os.system('cls')

def salario_com_pontuacao(wages):
    salario = str(wages)
    if len(salario) == 4: #1.000
        converte = salario[0] + '.' +salario[1:]
        return converte
    elif len(salario) == 5:# 10.000
        converte = salario[0:2] + '.' + salario[2:]
        return converte
    elif len(salario) == 6: # 100.000
        converte = salario[0:3] + '.' + salario[3:]
        return converte
    elif len(salario) == 7: # 1.000.000
        converte = salario[0] + '.' + salario[1:4] + '.' + salario[4:]
        return converte
    elif len(salario) > 7: # De preferecia do consumidor final
        return None
# sempre colocar isso: from módulo import ... no programa principal (Ao criar uma função nova)
   
def valida_numero_casa(numero_casa):
  """
  Verifica se a string 'numero_casa' é um número de casa válido (apenas números e letras maiúsculas).

  Argumentos:
    numero_casa (str): A string a ser verificada.

  Retorna:
    bool: `True` se a string for um número de casa válido, `False` caso contrário.
  """
  if not numero_casa:
    return False
  for caractere in numero_casa:
    if not caractere.isalnum() or caractere.islower():
      return False
  return True

def busca_funcionário_pra_funcao(file, name, escolha = True):
    import json
    padrao = name
    with open(file, 'r') as f:
       data = json.load(f)

    # Buscando por um dicionário com a chave "nome" e valor "João"
    cont = 0
    nome_encontado = ''
    for item in data:
        if padrao in item['NAME']:
            cont += 1
            nome_encontado = item['NAME']
            if escolha:
                return True
    if escolha:
        return False
    else:
        return cont, nome_encontado

def adicionar_dicionario_json(arquivo, novo_dicionario):
    import json
    """
    Adiciona um novo dicionário a um arquivo JSON existente.

    Args:
        arquivo (str): Nome do arquivo JSON.
        novo_dicionario (dict): Dicionário a ser adicionado.
    """

    try:
        # Ler o arquivo existente (ou criar uma lista vazia se não existir)
        with open(arquivo, 'r') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = []

        # Adicionar o novo dicionário à lista
        dados.append(novo_dicionario)

        # Escrever os dados atualizados no arquivo
        with open(arquivo, 'w') as f:
            json.dump(dados, f, indent=4)
    except (IOError, OSError) as e:
        print(f"Erro ao acessar o arquivo: {e}")


def atualizar_json(file):
    import json
    """
        Atualiza um valor em um arquivo JSON.

        Args:
        arquivo: Nome do arquivo JSON.
        chave: Chave do valor a ser atualizado.
        novo_valor: Novo valor para a chave.
    """
    while True:
        name = str(input('Digite o nome do funcionário que terá os dados atualizado: ')).upper()
        contagem, nome = busca_funcionário_pra_funcao(file,name,False)
        if contagem > 1:
            print('\033[4mHá mais de uma pessoa com esse nome, digite o nome completo para maior sucesso!\033[m')
            continue
        if not busca_funcionário_pra_funcao(file,name):
            print('\033[1;31mNenhum Funcionário com esse nome!\033[m')
            return None # Encerrar o Função
        break
    print(f'campos editáveis do funcionário \033[4;33m{nome}\033[m no banco de dados.')
    print('[ 1 ] - Nome\n'
        '[ 2 ] - Idade\n'
        '[ 3 ] - Endereço\n'
        '[ 4 ] - Setor\n'
        '[ 5 ] - CPF\n'
        '[ 6 ] - Sálario\n'
        '[ 7 ] - Cancelar Atualização.')
    while True:
        try:
            opc = int(input('Qual opção será alterada?: '))
        except:
            continue
        else:
            if opc == 7:
                return None # Encerrar o Função
            if opc > 6 or 0 > opc:
                print('\033[4;31mOpção Inexistente!\033[m')
                continue
            else: # Nomeando tag de key de acordo com os números correspondede do menu
                if opc == 1:
                    key = 'NAME'
                    break
                elif opc == 2:
                    key = 'AGE'
                    break
                elif opc == 3:
                    key = 'ADDRESS'
                    break
                elif opc == 4:
                    key = 'SECTOR'
                    break
                elif opc == 5:
                    key = 'CPF'
                    break
                elif opc == 6:
                    key = 'WAGES'
                    break
    # Processo de inserir o dado novo 
    if opc == 4:
        while True:
            print('[ 1 ] - Recursos Humanos (RH)\n'
                '[ 2 ] - Financeiro\n'
                '[ 3 ] - Marketing e Vendas\n'
                '[ 4 ] - Produção ou Operações\n'
                '[ 5 ] - Tecnologia da Informação (TI)\n'
                '[ 6 ] - Administrativo\n'
                '[ 7 ] - Pesquisa e Desenvolvimento (P&D)\n'
                '[ 8 ] - Jurídico\n'
                '[ 9 ] - Comunicação\n'
                '[ 10 ] - Sustentabilidade')
            try:
                sector = int(input('OPÇÃO: '))
            except: 
                continue
            else:
                while 0 > sector or sector > 10:
                    sector = str(input('OPÇÃO: '))
                if sector == 1:
                    novo_valor = 'Recursos Humanos (RH)'
                    break
                elif sector == 2:
                    novo_valor = 'Financeiro'
                    break
                elif sector == 3:
                    novo_valor = 'Marketing e Vendas'
                    break
                elif sector == 4:
                    novo_valor = 'Produção ou Operações'
                    break
                elif sector == 5:
                    novo_valor = 'Tecnologia da Informação (TI)'
                    break
                elif sector == 6:
                    novo_valor = 'Administrativo'
                    break
                elif sector == 7:
                    novo_valor = 'Pesquisa e Desenvolvimento (P&D)'
                    break
                elif sector == 8:
                    novo_valor = 'Jurídico'
                    break
                elif sector == 9:
                    novo_valor = 'Comunicação'
                    break
                elif sector == 10:
                    novo_valor = 'Sustentabilidade'
                    break
    else: 
        while True:
            try:
                if opc == 1:
                    novo_valor = str(input('Nome Completo: ')).upper().strip()
                elif opc == 2:
                    novo_valor = int(input('Idade: '))
                elif opc == 3:
                    novo_valor = str(input('Endereço Completo [Com Número]: ')).title()
                elif opc == 5:
                    novo_valor = verificado_cpf()
                    if not novo_valor:                        
                        print('\033[1;31mCPF INVÁLIDO!\033[m')
                        int('Erro')
                elif opc == 6:
                    valor = int(input('Sálario: '))
                    novo_valor = salario_com_pontuacao(wages=valor)
            except:
                print('\033[4;31mDigite o dado corretamente!\033[m')
            else:
                break
            
    with open(file, 'r') as f:
        data = json.load(f)
    ind = 0
    complete_dict = {}
    # Localizar o dado (assumindo uma estrutura simples) # Possível erro localizado aqui
    for dicti in data:
        if name in dicti['NAME']: # Ao encontrar o funcionário, O dados são copiados e alterando a chave especifica.
            complete_dict = dicti
            complete_dict[key] = novo_valor
            break
        else:
            ind += 1
    
    def atualizar_dicionario(data, ind, complete_dict): # Criando um escopo local, para não gerar erros
        data[ind] = complete_dict
        return data

    data = atualizar_dicionario(data, ind, complete_dict)

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# Exemplo de uso:

def exibicao(files):
    linha('Listagem de Funcionários', 1)
    import json
    try: 
        with open(files, encoding='utf-8') as file:
            data = json.load(file)
            for dictionary in data:
                for key, value in dictionary.items():
                    print(f'{key}: {value}')
                print('=-' * 15)
    except Exception as erro:
        print(f'\033[4;31mNão foi possível exibir os dados! Porque: {erro}\033[m')

def cadastro_funcionários(file,escolha=1):
    """ Cadastro de Funcionário
    agrs: File: Arquivo Base de Salvamento
    Escolha: 1 para inserir salário manualmente / 2 para gerar sálario de acordo com setor
    
    return:
        adicione o dicionário ao json e mande um print de "Salvo com sucesso"
    """
    linha('Cadastro de Funcionários', 1)
    functionary = {
    }
    name = str(input('NOME: ')).upper().strip()
    functionary['NAME'] = name
    # Idade
    while True:
        try:
            age = int(input('IDADE: '))
        except Exception:
            print(f'ERR0! Indetificamos um erro: {Exception}')
        else:
            if 18 < age < 70:
                break
            else:
                print('\033[1;31mValor da Idade é Inválida\033[m')
    functionary['AGE'] = age
    # CPF
    while True:
        cpf = verificado_cpf()
        if cpf:
            functionary['CPF'] = cpf
            break
        print('\033[1;31mCPF INVÁLIDO!\033[m') 
    while True:
        address = str(input('ENDEREÇO [Sem núm]: ')).upper().rstrip()
        if len(address) > 5:
            conver_address = address.replace(' ','')
            if conver_address.isalpha():
                break
            else:
                print('\033[4;31mO ENDEREÇO NÃO PODER CONTÊM NÚMEROS.\033[m')
        else:
          print('\033[4;37mINSIRA O ENDEREÇO COMPLETO\033[m')
    while True:
        núm_casa = str(input('Nº DA CASA: '))
        if valida_numero_casa(núm_casa):
            functionary['ADDRESS'] = address + ', ' + núm_casa
            break
        else:
            print('\033[1;31mNÚMERO INVÁLIDO, APENAS UMA LETRA É POSSÍVEL!\033[m')
    # Setor
    while True:
        print('[ 1 ] - Recursos Humanos (RH)\n'
            '[ 2 ] - Financeiro\n'
            '[ 3 ] - Marketing e Vendas\n'
            '[ 4 ] - Produção ou Operações\n'
            '[ 5 ] - Tecnologia da Informação (TI)\n'
            '[ 6 ] - Administrativo\n'
            '[ 7 ] - Pesquisa e Desenvolvimento (P&D)\n'
            '[ 8 ] - Jurídico\n'
            '[ 9 ] - Comunicação\n'
            '[ 10 ] - Sustentabilidade')
        try:
            sector = int(input('OPÇÃO: '))
        except: 
            continue
        else:
            while 0 > sector or sector > 10:
                sector = str(input('OPÇÃO: '))
            if sector == 1:
                functionary['SECTOR'] = 'Recursos Humanos (RH)'
                break
            elif sector == 2:
                functionary['SECTOR'] = 'Financeiro'
                break
            elif sector == 3:
                functionary['SECTOR'] = 'Marketing e Vendas'
                break
            elif sector == 4:
                functionary['SECTOR'] = 'Produção ou Operações'
                break
            elif sector == 5:
                functionary['SECTOR'] = 'Tecnologia da Informação (TI)'
                break
            elif sector == 6:
                functionary['SECTOR'] = 'Administrativo'
                break
            elif sector == 7:
                functionary['SECTOR'] = 'Pesquisa e Desenvolvimento (P&D)'
                break
            elif sector == 8:
                functionary['SECTOR'] = 'Jurídico'
                break
            elif sector == 9:
                functionary['SECTOR'] = 'Comunicação'
                break
            elif sector == 10:
                functionary['SECTOR'] = 'Sustentabilidade'
                break
  
    # Sálario
    if escolha == 1:
        while True:
            wages_original = int(input('SÁLARIO: ')) # Continua aqui
            if wages_original < 1000 or wages_original > 50000:
                print('Sálario Inválido!')
                continue
            else:
                break
        
        wages = salario_com_pontuacao(wages_original)
        functionary['WAGES'] = wages
    else:
        from random import randint
        if sector == 1:
            wagesl = randint(5000,12000)
        elif sector == 2:
            wagesl = randint(7000,15000)
        elif sector == 3:
            wagesl = randint(6000,14000)
        elif sector == 4:
            wagesl = randint(5500,13000)
        elif sector == 5:
            wagesl = randint(8000,16000)
        elif sector == 6:
            wagesl = randint(5000,12000)
        elif sector == 7:
            wagesl = randint(9000,18000)
        elif sector == 8:
            wagesl = randint(7500,15000)
        elif sector == 9:
            wagesl = randint(6500,14000)
        elif sector == 10:
            wagesl = randint(7000,15000)
        
        wages = salario_com_pontuacao(wagesl)
        functionary['WAGES'] = wages
        
    adicionar_dicionario_json(file, functionary)
    print('\033[4;32mSalvo com sucesso!\033[m')

def busca_funcionário(file):
    import json
    linha(' Buscando Funcionário.. ', 2)
    sector = False
    padrao = str(input('Digite o NOME, [Digite 3 para o setor]: ')).upper()
    if padrao == '3':
        while True:
            sector = True
            print('[ 1 ] - Recursos Humanos (RH)\n'
                '[ 2 ] - Financeiro\n'
                '[ 3 ] - Marketing e Vendas\n'
                '[ 4 ] - Produção ou Operações\n'
                '[ 5 ] - Tecnologia da Informação (TI)\n'
                '[ 6 ] - Administrativo\n'
                '[ 7 ] - Pesquisa e Desenvolvimento (P&D)\n'
                '[ 8 ] - Jurídico\n'
                '[ 9 ] - Comunicação\n'
                '[ 10 ] - Sustentabilidade')
            try:
                sector = int(input('OPÇÃO: '))
            except: 
                continue
            else:
                while 0 > sector or sector > 10:
                    sector = str(input('OPÇÃO: '))
                if sector == 1:
                    padrao = '(RH)'
                    break
                elif sector == 2:
                    padrao = 'Financeiro'
                    break
                elif sector == 3:
                    padrao = 'Marketing/Vendas'
                    break
                elif sector == 4:
                    padrao = 'Produção/Operações'
                    break
                elif sector == 5:
                    padrao = '(TI)'
                    break
                elif sector == 6:
                    padrao = 'Administrativo'
                    break
                elif sector == 7:
                    padrao = '(P&D)'
                    break
                elif sector == 8:
                    padrao = 'Jurídico'
                    break
                elif sector == 9:
                    padrao = 'Comunicação'
                    break
                elif sector == 10:
                    padrao = 'Sustentabilidade'
                    break

    with open(file, 'r') as f:
       data = json.load(f)

    # Buscando por um dicionário com a chave "nome" e valor "João"
    cont = 0
    for item in data:
        if sector:
            if padrao in item.get('SECTOR'):
                cont += 1
                linha(f'Funcionários do Setor: {padrao[0:5]}',1)
                for chave, valor in item.items():
                    print(f'{chave}: {valor}')
        else:
            if padrao in item.get('NAME'):
                linha(f'Funcionário: {padrao}',1)
                cont += 1
                for chave, valor in item.items():
                    print(f'{chave}: {valor}')
    linha('')
    return cont

def remocao_de_funcionario(file):
    import json
    name = str(input('Nome completo: '))
    contador = busca_funcionário_pra_funcao(file,name,False)
    if contador > 1:
        print(f'\033[4mFoi encontrado {contador} pessoas com nome de {name}\033[m')

    with open(file, 'r') as f:
       data = json.load(f)

    ind = 0
    complete_dict = {}
    
    for dicti in data:
        if name in dicti['NAME']:
            del data[ind]
            break
        else:
            ind += 1

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def contador_de_funcionário(file):
    import json
    with open(file, 'r') as f:
       data = json.load(f)
    
    tamanho = len(data)

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f'\033[4mNo banco de dados há {tamanho} Funcionários\033[m')

def calculo_da_folha_de_pagamento(file):
    import json
    with open(file, 'r') as f:
       data = json.load(f)
    
    folha_original = 0
    for item in data:
        valor = ''
        for num in item['WAGES']:
            if not num == '.':
                valor = valor + num
        folha_original += int(valor)

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

    folha = salario_com_pontuacao(wages=folha_original)
    print(f'\033[4mA Folha de Pagamento é de R${folha}\033[m')

def avaliacao(file):
    """ Notas do Funcionários
        return:
            O dicionário alterado com a nova chave ou novo valor
    """
    import json
    while True:
        name = str(input('Digite o nome do funcionário que terá os dados atualizado: ')).upper()
        contagem, nome = busca_funcionário_pra_funcao(file,name,False)
        if contagem > 1:
            print('\033[4mHá mais de uma pessoa com esse nome, digite o nome completo para maior sucesso!\033[m')
            continue
        if not busca_funcionário_pra_funcao(file,name):
            print('\033[1;31mNenhum Funcionário com esse nome!\033[m')
            return None # Encerrar o Função
        break

    while True:
        nota = float(input('NOTA [1/10]: '))
        if not nota > 10 or nota < 1:
            break

    with open(file, 'r') as f:
        data = json.load(f)
    
    ind = 0
    complete_dict = {}
    for dicti in data:
        if name in dicti['NAME']: # Ao encontrar o funcionário, O dados são copiados e alterando a chave especifica.
            complete_dict = dicti
            if complete_dict.get('Evaluation'):
                nota_antiga = complete_dict['Evaluation']
                print(f'Houve um aumento da nota de \033[1;33m+{nota-nota_antiga}\033[m' if \
                    nota_antiga < nota else f'Houve uma diminuição da nota de \033[1;31m-{nota_antiga-nota}\033[m')
            complete_dict['Evaluation'] = nota
            break
        else:
            ind += 1
    
    def atualizar_dicionario(data, ind, complete_dict): # Criando um escopo local, para não gerar erros
        data[ind] = complete_dict
        return data

    data = atualizar_dicionario(data, ind, complete_dict)

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
    print('\033[1;33mSalvo com Sucesso!\033[m')