import json
import uuid
from modulos.menu_crud import menu_crud
from inicializacao.autenticacao import *

# --- FUNÇÕES AUXILIARES DE PERSISTÊNCIA ---
def carregar_obras():
    try:
        with open("dados/obras.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def carregar_usuarios():
    try:
        with open("dados/usuarios.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def empresa_existe(nome_empresa):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["tipo"] == "empresa" and usuario["nome"].strip().lower() == nome_empresa:
            return True

    return False

def salvar_obras(obras):
    with open("dados/obras.json", "w", encoding="utf-8") as arquivo:
        json.dump(obras, arquivo, indent=4, ensure_ascii=False)
    

# --- TELA 1: DASHBOARD DE OBRAS (Visualização e Filtros) ---
def exibir_card_gestor(usuario_logado):
    obras = carregar_obras()
    
    for obra in obras:
        if obra["gestor_responsavel"] == usuario_logado["nome"]:
            encontrou_obra = True
            
            print("\n" + "=" * 50)
            print(f"{obra['nome']}")
            print(f"📍 Bairro: {obra['bairro']}")
            print(f"🏷️ Categoria: {obra['categoria']}")
            print(f"🚧 Status: {obra['status']}")
            print(f"📊 Progresso: {obra['progresso']}%")
            print("=" * 50)
            

    if not encontrou_obra:
        print("\nNenhuma obra encontrada para a sua empresa.")

def dashboard_gestor():
    obras = carregar_obras()
    if not obras:
        print("\nNenhuma obra cadastrada no sistema.")
        return obras

    print("\n" + "=" * 60)
    print("DASHBOARD DE OBRAS - VISÃO DO GESTOR".center(60))
    print("=" * 60)

    return obras

# --- TELA 2: ADICIONAR NOVA OBRA (Formulário) ---
def adicionar_obra(usuario_logado):
    print("\n" + "=" * 60)
    print("ADICIONAR NOVA OBRA".center(60))
    print("=" * 60)
    
    while True:
        nome = input("Nome da obra: ")
        categoria = input("Categoria (ex: Educação, Saúde, Infraestrutura): ")
        bairro = input("Bairro: ")
        endereco = input("Endereço completo: ")
        empresa = input("Empresa Responsável (Deixe em branco se em licitação): ").strip().lower()

        if empresa == "" or empresa_existe(empresa):
            
            try:
                valor_previsto = float(input("Orçamento Previsto (R$): "))
            except ValueError:
                print("Valor inválido. O orçamento será definido como 0.0")
                valor_previsto = 0.0
                
            data_inicio = input("Data de Início (DD-MM-AAAA): ")
            previsao_entrega = input("Previsão de Entrega (DD-MM-AAAA): ")
            descricao = input("Breve descrição do projeto: ")

            nova_obra = {
                "id": str(uuid.uuid4()), # Gera um ID único automaticamente
                "nome": nome,
                "categoria": categoria,
                "bairro": bairro,
                "endereco": endereco,
                "status": "em andamento", # Status padrão inicial
                "progresso": 0,
                "valor_previsto": valor_previsto,
                "empresa_responsavel": empresa if empresa else "A definir",
                "gestor_responsavel": usuario_logado["nome"],
                "data_inicio": data_inicio,
                "previsao_entrega": previsao_entrega,
                "descricao": descricao
            }

            obras = carregar_obras()
            obras.append(nova_obra)
            salvar_obras(obras)
            print("\n✅ Obra cadastrada com sucesso!")
            break

        else:
            print("Empresa inválida")

# --- TELA 3: ATUALIZAR OBRA (Edição de Status e Progresso) ---
def atualizar_obra(obras):
    try:
        escolha = int(input("\nDigite o número da obra que deseja atualizar (0 para voltar): "))
        if escolha == 0:
            return
        
        obra = obras[escolha - 1]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    print(f"\nAtualizando: {obra['nome']}")
    print("1 - Alterar Status (em andamento, parada, atrasada, concluida)")
    print("2 - Atualizar Progresso (%)")
    print("3 - Atualizar Orçamento")
    
    opcao = input("O que deseja atualizar? ").strip()
    
    if opcao == "1":
        novo_status = input("Novo status: ").lower()
        obra['status'] = novo_status
    elif opcao == "2":
        try:
            novo_progresso = int(input("Novo progresso (0 a 100): "))
            if 0 <= novo_progresso <= 100:
                obra['progresso'] = novo_progresso
            else:
                print("Valor deve ser entre 0 e 100.")
        except ValueError:
            print("Valor inválido.")
    elif opcao == "3":
        try:
            novo_valor = float(input("Novo orçamento (R$): "))
            obra['valor_previsto'] = novo_valor
        except ValueError:
            print("Valor inválido.")
    else:
        print("Opção inválida.")
        return

    salvar_obras(obras)
    print("\n✅ Obra atualizada com sucesso!")

# --- TELA 4: RELATÓRIOS DA OBRA (Estatísticas e Gráficos de Texto) ---
def relatorios_obra(obras):
    try:
        escolha = int(input("\nDigite o número da obra para gerar o relatório (0 para voltar): "))
        if escolha == 0:
            return
        obra = obras[escolha - 1]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    # Simulando os gráficos da tela 4 usando barras de texto
    progresso = obra['progresso']
    barra_progresso = "█" * (progresso // 5) + "░" * (20 - (progresso // 5))
    
    # Simulação de Score da Empresa (Fictício para demonstração)
    score_empresa = 85 
    barra_score = "█" * (score_empresa // 5) + "░" * (20 - (score_empresa // 5))

    print("\n" + "=" * 60)
    print(f"RELATÓRIO GERENCIAL: {obra['nome'].upper()}")
    print("=" * 60)
    print(f"Empresa: {obra['empresa_responsavel']}")
    print(f"Status Atual: {obra['status'].capitalize()}")
    print("-" * 60)
    print("📈 PROGRESSO FÍSICO:")
    print(f"[{barra_progresso}] {progresso}%")
    print("\n⭐ SCORE DE CONFIANÇA DA EMPRESA:")
    print(f"[{barra_score}] {score_empresa}/100 (Confiável)")
    print("\n💰 SAÚDE FINANCEIRA:")
    print(f"Orçamento Liberado: R$ {obra['valor_previsto']:,.2f}")
    print("=" * 60)

# --- MENU PRINCIPAL DO GESTOR ---
def menu_gestor(usuario_logado):
    while True:
        print("\n" + "=" * 40)
        print(f"🏢 PAINEL DA PREFEITURA")
        print(f"👤 Gestor: {usuario_logado['nome']}")
        print("=" * 40)
        print("1 - Ver Dashboard de Obras")
        print("2 - Adicionar Nova Obra")
        print("3 - Atualizar Obra Existente")
        print("4 - Gerar Relatórios")
        print("5 - Meu Perfil (Configurações)")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            limpar_tela()
            exibir_card_gestor(usuario_logado)
  
        elif opcao == "2":
            limpar_tela()
            adicionar_obra(usuario_logado)
        elif opcao == "3":
            limpar_tela()
            obras_carregadas = dashboard_gestor()
            if obras_carregadas:
                atualizar_obra(obras_carregadas)
        elif opcao == "4":
            limpar_tela()
            obras_carregadas = dashboard_gestor()
            if obras_carregadas:
                relatorios_obra(obras_carregadas)
        elif opcao == "5":
            limpar_tela()
            menu_crud(usuario_logado)
        elif opcao == "0":
            limpar_tela()
            print("Saindo do painel do gestor...")
            break
        else:
            print("Opção inválida. Tente novamente.")
