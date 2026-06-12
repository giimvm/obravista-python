from inicializacao.cadastro import cadastro
from inicializacao.login import login
from modulos.cidadao import menu_cidadao


while True:
    print("\n=== OBRAVISTA ===")
    print("1 - Login")
    print("2 - Cadastro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuario_logado = login()

        if usuario_logado:
            menu_cidadao(usuario_logado)

    elif opcao == "2":
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        if cadastro(nome, email, senha):
            print("Usuário cadastrado com sucesso!")

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
