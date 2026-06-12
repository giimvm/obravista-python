import json
from modulos.menu_crud import menu_crud
import uuid
from datetime import datetime
from inicializacao.autenticacao import *

#carrega todas as obras no arquivo obras.json
def carregar_obras():
    with open("dados/obras.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

#função pra buscar a obra do usuario logado    
def obra_usuario(usuario_logado):
    obras = carregar_obras()
    for obra in obras:
        if obra["empresa_responsavel"] == usuario_logado["nome"]:
            return obra

#exibe o card da obra da empresa logada
def exibir_card_obra(usuario_logado):
    obras = carregar_obras()
    
    for obra in obras:
        if obra["empresa_responsavel"] == usuario_logado["nome"]:
            
            print("\n" + "=" * 50)
            print(f"{obra['nome']}")
            print(f"📍 Bairro: {obra['bairro']}")
            print(f"🏷️ Categoria: {obra['categoria']}")
            print(f"🚧 Status: {obra['status']}")
            print(f"📊 Progresso: {obra['progresso']}%")
            print("=" * 50)
        

#apos a criação do relátorio, ele salva dentro do json relatorios.json     
def salvar_relatorio(titulo, texto_relatorio, obra, usuario_logado):
    
    caminho_arquivo = "dados/relatorios.json"
    
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        try:
            relatorios = json.load(arquivo)
        except json.JSONDecodeError:
            relatorios = []

    novo_relatorio = {
        "id": str(uuid.uuid4()),
        "titulo": titulo,
        "relatorio": texto_relatorio,
        "obra": obra["nome"],
        "nome_empresa": usuario_logado["nome"],
        "data_envio": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    
    relatorios.append(novo_relatorio)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(relatorios, arquivo, indent=4, ensure_ascii=False)
    limpar_tela()
    print("\n💾 Relatório salvo com sucesso!")

#fazer envio do relatório    
def enviar_relatorio(usuario_logado, obra):
    
    print(f"\n📝 Criando relatório para a obra: {obra['nome']}")
    print("Descreva os avanços, insumos utilizados e intercorrências.")
    
    loop = True
    while loop:
        titulo = input("Digite o título do relátorio: ")
        texto_relatorio = input("Digite o relátorio: ")
        
        print("1 - Enviar relatório")
        print("2 - Visualizar relatório")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            salvar_relatorio(titulo, texto_relatorio, obra, usuario_logado)
            loop = False
        elif escolha == 2:
            print(f"\n--- {titulo} ---")
            print(texto_relatorio)
            print("-" * 20)
            
            print("1 - Confirmar e Enviar")
            print("2 - Voltar para o menu")
            
            sub_escolha = int(input("Escolha uma opção: "))
            
            if sub_escolha == 1:
                salvar_relatorio(titulo, texto_relatorio, obra, usuario_logado)
                loop = False
            elif sub_escolha == 2: 
                limpar_tela()
                print("Voltando para o menu . . .")
                menu_empresa(usuario_logado)
                return
                

    
def menu_empresa(usuario_logado):
    limpar_tela()
    obra = obra_usuario(usuario_logado)
    while True:

        print("\nAÇÕES")
        print("1 - Ver detalhes da obra")
        print("2 - Enviar relatório")
        print("3 - Meu perfil")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            exibir_card_obra(usuario_logado)

        elif opcao == "2":
            limpar_tela()
            enviar_relatorio(usuario_logado, obra)

        elif opcao == "3":
            limpar_tela()
            menu_crud(usuario_logado)

        elif opcao == "4":
            limpar_tela()
            print("Saindo...")
            break

        else:
            print("Opção inválida.")