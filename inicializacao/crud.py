from inicializacao.autenticacao import carregar_usuarios, salvar_usuarios


def buscar_usuario_logado(usuario_logado, usuarios):
    for usuario in usuarios:
        if usuario["id"] == usuario_logado["id"]:
            return usuario

    return None


def listar_dados_usuario(usuario_logado):
    print("\n--- MEUS DADOS ---")
    print(f"ID: {usuario_logado['id']}")
    print(f"Nome: {usuario_logado['nome']}")
    print(f"Email: {usuario_logado['email']}")
    print(f"Tipo: {usuario_logado['tipo']}")


def atualizar_nome(usuario_logado):
    usuarios = carregar_usuarios()
    usuario = buscar_usuario_logado(usuario_logado, usuarios)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    print(f"Nome atual: {usuario['nome']}")
    novo_nome = input("Digite o novo nome: ")

    usuario["nome"] = novo_nome
    salvar_usuarios(usuarios)

    usuario_logado["nome"] = novo_nome

    print("Nome atualizado com sucesso!")


def atualizar_email(usuario_logado):
    usuarios = carregar_usuarios()
    usuario = buscar_usuario_logado(usuario_logado, usuarios)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    dominios_validos = ["cidadao", "empresa", "prefeitura"]

    print(f"Email atual: {usuario['email']}")
    novo_email = input("Digite o novo email: ")

    if "@" not in novo_email:
        print("Email inválido!")
        return

    novo_tipo = novo_email.split("@")[1]

    if novo_tipo not in dominios_validos:
        print("Tipo de usuário inválido!")
        return

    usuario["email"] = novo_email
    usuario["tipo"] = novo_tipo

    salvar_usuarios(usuarios)

    usuario_logado["email"] = novo_email
    usuario_logado["tipo"] = novo_tipo

    print("Email atualizado com sucesso!")


def atualizar_senha(usuario_logado):
    usuarios = carregar_usuarios()
    usuario = buscar_usuario_logado(usuario_logado, usuarios)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    nova_senha = input("Digite a nova senha: ")

    usuario["senha"] = nova_senha
    salvar_usuarios(usuarios)

    print("Senha atualizada com sucesso!")


def deletar_usuario(usuario_logado):
    usuarios = carregar_usuarios()
    usuario = buscar_usuario_logado(usuario_logado, usuarios)

    if usuario is None:
        print("Usuário não encontrado.")
        return False

    confirmar = input(f"Tem certeza que deseja deletar sua conta, {usuario['nome']}? (s/n): ")

    if confirmar.lower() == "s":
        usuarios.remove(usuario)
        salvar_usuarios(usuarios)
        print("Usuário deletado com sucesso!")
        return True

    print("Operação cancelada.")
    return False