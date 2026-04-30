import json
def cadastro ():
    
    with open ('clientes.json','r',encoding='utf-8') as arquivo:
        clientes = json.load(arquivo)

    print( "Insira seus dados para cadastro ")                   #Cadastro do cliente    

    nome = input('Nome: ')
    # cpf = int(input('CPF: '))
    # renda = float(input('Renda Mensal: '))
    # profissao = input('Profissão:')
    # endereco =  input('Endereço:')
    # score = int(input('Score: '))
    # senha = input('Senha:')

    ultimo_id = clientes[-1]["ID"]+1             #pega o ultimo ID e incrementa +1

    novo_cliente = {                             #Pega dados inseridos do novo cliente
    "ID": ultimo_id,
    "Nome": nome, 
    # "CPF": cpf,
    # "Renda": renda,
    # "Profissao": profissao,
    # "Endereco": endereco,
    # "Score": score,
    # "Senha": senha, 
}

    #Inserir novo cliente a lista
    

    return novo_cliente