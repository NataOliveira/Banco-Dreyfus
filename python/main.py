#importa o aquivo "banco de dados" dos clientes
import json
from login import login
from cadastro import cadastro
import time


#Abre o arquivo, r para ler os aquivos, cria uma variavel(arquivo) que representa o arquivo (clientes.json) aberto
with open ('clientes.json','r',encoding='utf-8') as arquivo:
    clientes = json.load(arquivo) # o (json.load(arquivo)) ele lê o .json e converte para python



while True:

    print('='*20)
    print('-- BANCO DREYFUS --')
    print('  Autoatendimento')
    print('='*20)
   
    join = str(input('\nCPF: '))
    joinsenha = str(input('SENHA: '))

    logado = False

    for cliente in clientes:
        if join == str(cliente ["CPF"]) and joinsenha == str(cliente ["Senha"]):
            logado = True
            break

    if logado:
         print("\n✅Login Efetuado com Sucesso\n")
         break
    
    
    print('\n❌ CPF OU SENHA INVÁLIDOS\n')
   
    opcao = int(input('1- Tentar novamente \n2-Cadastrar\n3-Sair\n\nDigite uma opção: '))      
  
    if opcao == 2:
        print("\nIr para cadastro\n")
        clientes.append(cadastro())

    elif opcao == 3:
        print("\nObrigado por usar o Banco Dreyfus. Até logo!\n")
        break
       


with open('clientes.json', 'w', encoding='utf-8') as arquivos :
    json.dump (clientes,arquivos,indent=4,ensure_ascii= False)
