#importa o aquivo "banco de dados" dos clientes
import json
from login import login
from cadastro import cadastro
import time


#Abre o arquivo, r para ler os aquivos, cria uma variavel(arquivo) que representa o arquivo (clientes.json) aberto
with open ('clientes.json','r',encoding='utf-8') as arquivo:
    clientes = json.load(arquivo) # o (json.load(arquivo)) ele lê o .json e converte para python



while True:

    join = int(input('''--BANCO DREYFUS--
    Autoatendimento\n\nCPF:  '''))

    joinsenha = int(input('SENHA:  '))
    

    logado = False

    for cliente in clientes:
        if join == cliente ["CPF"] and joinsenha == cliente ["Senha"]:
            logado = True
            break

    if logado:
         print("\nLogin Efetuado com Sucesso\n")
         break
    
    
    print('\nCPF OU SENHA INVÁLIDOS\n')
    opcao = int(input('1- Tentar novamente \n2-Cadastrar\nDigite uma opção: \n\n'))
            
  
    if opcao == 2:
        print("Ir para cadastro")
        cadastro()
        break



 



# clientes.append(cadastro())

# with open('clientes.json', 'w', encoding='utf-8') as arquivos :
#     json.dump (clientes,arquivos,indent=4,ensure_ascii= False)
