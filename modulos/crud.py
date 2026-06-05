from autenticacao import autenticar_usuario, carregar_usuarios
import json

def autenticar_id_cidadao():
  pass

def atualizar_email():
    pass

def atualizar_senha():

def atualizar_nome():
    usuarios = carregar_usuarios()

    id_usuario = int(input("Digite seu ID: "))

    for usuario in usuarios:

        if usuario["id"] == id_usuario and usuario["tipo"] == "cidadao":

            print(f"Nome atual: {usuario['nome']}")

            novo_nome = input("Digite o novo nome: ")

            usuario["nome"] = novo_nome

            salvar_usuarios(usuarios)

            print("Nome atualizado com sucesso!")
            return

    print("Usuário não encontrado.")

def deletar_usuario():