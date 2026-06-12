import json
from modulos.menu_crud import menu_crud
from inicializacao.autenticacao import *

def carregar_obras():
    with open("dados/obras.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def buscar_obras_ativas():
    obras = carregar_obras()

    obras_ativas = []

    for obra in obras:
        if obra["status"].lower() != "concluida":
            obras_ativas.append(obra)

    return obras_ativas


def exibir_card_obra(indice, obra):
    print("\n" + "=" * 50)
    print(f"{indice}. {obra['nome']}")
    print(f"📍 Bairro: {obra['bairro']}")
    print(f"🏷️ Categoria: {obra['categoria']}")
    print(f"🚧 Status: {obra['status']}")
    print(f"📊 Progresso: {obra['progresso']}%")
    print("=" * 50)


def dashboard_obras(usuario_logado):
    obras = buscar_obras_ativas()

    print("\n" + "=" * 60)
    print(f"Olá, {usuario_logado['nome']}!")
    print("Obras públicas ocorrendo no momento")
    print("=" * 60)

    if len(obras) == 0:
        print("Nenhuma obra ativa no momento.")
        return

    for indice, obra in enumerate(obras, start=1):
        exibir_card_obra(indice, obra)


def detalhes_da_obra():
    obras = buscar_obras_ativas()

    try:
        escolha = int(input("\nDigite o número da obra: "))
    except ValueError:
        print("Opção inválida.")
        return

    if escolha < 1 or escolha > len(obras):
        print("Obra não encontrada.")
        return

    obra = obras[escolha - 1]

    print("\n" + "=" * 60)
    print("DETALHES DA OBRA")
    print("=" * 60)
    print(f"Nome: {obra['nome']}")
    print(f"Categoria: {obra['categoria']}")
    print(f"Bairro: {obra['bairro']}")
    print(f"Endereço: {obra['endereco']}")
    print(f"Status: {obra['status']}")
    print(f"Progresso: {obra['progresso']}%")
    print(f"Empresa responsável: {obra['empresa_responsavel']}")
    print(f"Valor previsto: R$ {obra['valor_previsto']}")
    print(f"Data de início: {obra['data_inicio']}")
    print(f"Previsão de entrega: {obra['previsao_entrega']}")
    print(f"Descrição: {obra['descricao']}")


def pesquisar_obra():
    obras = carregar_obras()

    termo = input("\nDigite a obra que deseja conferir: ").lower()

    resultados = []

    for obra in obras:

        if (
            termo in obra["nome"].lower()
            or termo in obra["bairro"].lower()
            or termo in obra["categoria"].lower()
            or termo in obra["status"].lower()
        ):
            resultados.append(obra)

    if len(resultados) == 0:
        print("Nenhuma obra encontrada.")
        return

    print("\nRESULTADOS DA PESQUISA")

    for indice, obra in enumerate(resultados, start=1):
        exibir_card_obra(indice, obra)


def menu_cidadao(usuario_logado):
    dashboard_obras(usuario_logado)

    while True:

        print("\nAÇÕES")
        print("1 - Ver detalhes de uma obra")
        print("2 - Pesquisar obra")
        print("3 - Meu perfil")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            detalhes_da_obra()

        elif opcao == "2":
            limpar_tela()
            pesquisar_obra()

        elif opcao == "3":
            limpar_tela()
            menu_crud(usuario_logado)

        elif opcao == "4":
            limpar_tela()
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
