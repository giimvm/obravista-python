from inicializacao.autenticacao import *
import uuid

def cadastro(nome, email, senha):
        usuarios = carregar_usuarios()

        dominios_validos = ["cidadao", "empresa", "prefeitura"]

        if "@" not in email:
            print("Email inválido!")
            return

        tipo = email.split("@")[1]

        if tipo not in dominios_validos:
            print("Tipo de usuário inválido!")
            return

        novo_usuario = {
        "id": str(uuid.uuid4()),
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": tipo
    }

        usuarios.append(novo_usuario)
        salvar_usuarios(usuarios)

        print("Cadastro realizado com sucesso!")
        return True