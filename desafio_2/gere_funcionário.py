import os
import time
from módulo import cls
from módulo import linha
from módulo import cadastro_funcionários
from módulo import exibicao
from módulo import encontrararquivo
from módulo import criararquivo
from módulo import busca_funcionário
from módulo import atualizar_json
from módulo import remocao_de_funcionario
from módulo import contador_de_funcionário
from módulo import calculo_da_folha_de_pagamento
from módulo import avaliacao

file = 'funcionário.json'
if not encontrararquivo(file):
    linha(' Criando arquivo.. ',2)
    time.sleep(0.7)
    criararquivo(file)
while True:
    linha('Menu Principal',1)
    print('[ 1 ] - Cadastro de Funcionários\n'
        '[ 2 ] - Listagem de Funcionários\n'
        '[ 3 ] - Busca de Funcionários\n'
        '[ 4 ] - Atualização de Dados\n'
        '[ 5 ] - Remoção de Funcionários\n'
        '[ 6 ] - Cálculo de Folha de Pagamento\n'
        '[ 7 ] - Cálcular o Número de Fucionários Cadastrado\n'
        '[ 8 ] - Avaliação Individual do Funcionário\n'
        '[ S ] - Sair do programa')
    try:
        opc = str(input('Opção: ')).upper()
        opc = int(opc)
    except:
        if opc == 'S':
            cls()
            break
    else:
        if opc == 1:
            cadastro_funcionários(file,2)
        elif opc == 2:
            exibicao(file)
        elif opc == 3:
            busca_funcionário(file)
        elif opc == 4:
            linha('Atualização de dados', 1) 
            atualizar_json(file) # Arruma essa função
        elif opc == 5:
            linha('Remoção de Funcionário',1)
            remocao_de_funcionario(file)
        elif opc == 6:
            linha('Folha de Pagamento',1)
            calculo_da_folha_de_pagamento(file)
        elif opc == 7:
            linha('Números de Funcionário',1)
            contador_de_funcionário(file)
        elif opc == 8:
            linha('Avaliação do Funcionário',1)
            avaliacao(file)
        else:
            print('\033[4;31mOpção Inexistente!\033[m')
# Finalizado


"""
    ## Gerenciamento de Funcionários: Um Desafio Mais Complexo

**Excelente escolha!** Criar um sistema de gerenciamento de funcionários é um projeto mais complexo e te dará a oportunidade de trabalhar com conceitos como:

* **Orientação a objetos:** Modelar funcionários como objetos com atributos (nome, cargo, salário, etc.) e métodos (calcular salário líquido, promover, etc.).
* **Estruturas de dados:** Utilizar listas ou dicionários para armazenar informações sobre os funcionários.
* **Arquivos:** Para salvar e carregar dados de forma persistente.
* **Interfaces gráficas (opcional):** Utilizar bibliotecas como Tkinter (Python) para criar uma interface mais intuitiva.

**Funcionalidades básicas:**

* **Cadastro de funcionários:** Coletar informações como nome, cargo, data de admissão, salário base.
* **Listagem de funcionários:** Mostrar todos os funcionários cadastrados, com seus respectivos dados.
* **Busca de funcionários:** Permitir buscar funcionários por nome, cargo ou outros critérios.
* **Atualização de dados:** Alterar informações de um funcionário específico.
* **Remoção de funcionários:** Excluir um funcionário da base de dados.
* **Cálculo de folha de pagamento:** Calcular o salário líquido de cada funcionário, considerando descontos e benefícios.

**Funcionalidades extras (opcional):**
* **Geração de relatórios:** Gerar relatórios com informações sobre a folha de pagamento, funcionários por departamento, etc.
* **Controle de ponto:** Registrar horários de entrada e saída dos funcionários.
* **Cálculo de férias:** Calcular o período de férias de cada funcionário.
* **Sistema de permissões:** Controlar o acesso a diferentes funcionalidades do sistema.

"""