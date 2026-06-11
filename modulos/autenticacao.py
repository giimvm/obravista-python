import json

#carrega o json
def carregar_usuarios():
    with open("dados/usuarios.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

#atualiza os dados do json
def salvar_usuarios(usuarios):
    with open("dados/usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

def autenticar_usuario(email, senha):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            return True

        else:
            return False

def cadastrar_usuario(nome, email, senha, tipo):
        usuarios = carregar_usuarios()

        novo_usuario = {
        "id": "id",
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": email.split("@")[1]
    }

        usuarios.append(novo_usuario)

        with open("dados/usuarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

        return True





