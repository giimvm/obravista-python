from inicializacao.crud import *
from inicializacao.autenticacao import *

def menu_crud(usuario_logado):
    while True:
        print("\n--- MEU PERFIL ---")
        print("1 - Ver meus dados")
        print("2 - Atualizar nome")
        print("3 - Atualizar email")
        print("4 - Atualizar senha")
        print("5 - Excluir conta")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            listar_dados_usuario(usuario_logado)

        elif opcao == "2":
            limpar_tela()
            atualizar_nome(usuario_logado)

        elif opcao == "3":
            limpar_tela()
            atualizar_email(usuario_logado)

        elif opcao == "4":
            limpar_tela()
            atualizar_senha(usuario_logado)

        elif opcao == "5":
            limpar_tela()
            conta_excluida = deletar_usuario(usuario_logado)

            if conta_excluida:
                return True

        elif opcao == "0":
            return False

        else:
            print("Opção inválida.")