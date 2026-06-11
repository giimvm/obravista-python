from autenticacao import *

def atualizar_email(id_usuario):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["id"] == id_usuario and usuario["tipo"] == "cidadao":

            senha_atual = input(f"Digite sua senha atual: ")
            
            if senha_atual == usuario["senha"]:

                nova_senha = input("Digite sua nova senha: ")

                usuario["senha"] = nova_senha

                salvar_usuarios(usuarios)

            print("Email atualizado com sucesso!")
            return

    else:
        print("Usuário não encontrado.") 

def atualizar_senha(id_usuario):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["id"] == id_usuario and usuario["tipo"] == "cidadao":

            print(f"Email atual: {usuario['email']}")

            novo_email = input("Digite seu novo email: ")

            usuario["email"] = novo_email

            salvar_usuarios(usuarios)

            print("Senha atualizada com sucesso!")
            return

    else:
        print("Usuário não encontrado.")

def atualizar_nome(id_usuario):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["id"] == id_usuario and usuario["tipo"] == "cidadao":

            print(f"Nome atual: {usuario['nome']}")

            novo_nome = input("Digite o novo nome: ")

            usuario["nome"] = novo_nome

            salvar_usuarios(usuarios)

            print("Nome atualizado com sucesso!")
            return

    else:
        print("Usuário não encontrado.")

def deletar_usuario(id_usuario):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            
            email_usuario = input("Digite seu email: ")
            senha_usuario = input("Digite sua senha: ")
            
            if email_usuario == usuario["email"] and senha_usuario == usuario["senha"]:
                
                usuarios.remove(usuario)

                salvar_usuarios(usuarios)

                print("Usuário removido com sucesso!")
                return True

    else:
        print("Usuário não encontrado.")
        return False