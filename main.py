from inicializacao.cadastro import cadastro
from inicializacao.login import login
from modulos.cidadao import menu_cidadao
from modulos.empresa import menu_empresa
from inicializacao.autenticacao import *


while True:
    print("\n=== OBRAVISTA ===")
    print("1 - Login")
    print("2 - Cadastro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        limpar_tela()
        usuario_logado = login()     

    elif opcao == "2":
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        if cadastro(nome, email, senha):
            limpar_tela()
            print("Usuário cadastrado com sucesso!")

    elif opcao == "0":
        limpar_tela()
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
