O ObraVista é uma aplicação de linha de comando desenvolvida em Python estruturada de forma modular. O sistema gerencia o ciclo de vida de obras públicas e perfis de utilizadores através de permissões baseadas no domínio do e-mail informado no login.


 Estrutura do Repositório (Modularização)
O projeto foi dividido em pacotes e módulos seguindo as boas práticas de separação de responsabilidades:


📁 obravista-python
├── 📄 main.py                 # Ponto de entrada (Fluxo principal do sistema)
├── 📁 dados/                  # Persistência de dados locais (Arquivos JSON)
│   ├── 📄 obras.json          # Registo de obras públicas
│   └── 📄 usuarios.json       # Registo de credenciais e perfis de utilizadores
├── 📁 inicializacao/          # Módulos de autenticação e gestão de contas
│   ├── 📄 autenticacao.py     # Lógica de validação de credenciais
│   ├── 📄 cadastro.py         # Inserção de novos utilizadores
│   ├── 📄 crud.py             # Funções de atualização e eliminação de contas
│   └── 📄 login.py            # Captura de dados de acesso e tratamento de permissões
└── 📁 modulos/                # Dashboards e menus interativos por perfil
    ├── 📄 cidadao.py          # Painel de visualização e pesquisa para cidadãos
    ├── 📄 empresa.py          # Painel da empreiteira
    ├── 📄 gestor.py           # Painel da prefeitura (Gestor)
    └── 📄 menu_crud.py        # Interface interativa de edição de perfil do utilizador
 Mapeamento do CRUD no Sistema
As operações essenciais de manipulação de dados estão distribuídas pelos seguintes módulos:

Create (Criação): Executado em inicializacao/cadastro.py (cadastro de novos utilizadores) e no módulo do Gestor (adição de obras).

Read (Leitura): Executado em modulos/cidadao.py através das funções buscar_obras_ativas(), exibir_card_obra() e pesquisar_obra().

Update (Atualização): Executado em inicializacao/crud.py com as funções de mutação de estado (atualizar_nome(), atualizar_email() e atualizar_senha()).

Delete (Eliminação): Executado em inicializacao/crud.py através da função deletar_usuario().

Aplicação dos Conceitos Obrigatórios da Disciplina
Para fins de avaliação, segue a localização e a justificativa técnica do uso de cada conceito de lógica de programação exigido:

1. Funções (def)
O projeto é totalmente procedural e modular. Cada funcionalidade possui um escopo isolado e reutilizável.

Exemplo no código: def login(), def carregar_obras(), def pesquisar_obra().

2. Dicionários (dict)
Utilizados para modelagem de entidades complexas estruturadas em par chave-valor.

Exemplo no código: Cada registo dentro do arquivo obras.json é convertido num dicionário Python em tempo de execução para aceder diretamente a propriedades como obra["nome"], obra["bairro"] ou obra["progresso"].

3. Listas (list)
Utilizadas como matrizes de dados dinâmicas para armazenamento em memória RAM, permitindo filtragens, buscas e append de novos objetos.

Exemplo no código: As variáveis de escopo local obras_ativas = [] e resultados = [] no arquivo modulos/cidadao.py.

4. Tuplas (tuple)
Utilizadas para definir coleções imutáveis que representam constantes e regras de negócio fixas do sistema (como tipos de status permitidos ou permissões de rotas), garantindo a integridade dos dados contra alterações acidentais.

5. Estruturas Condicionais (if / elif / else)
Aplicadas no encaminhamento de menus e no algoritmo de validação de permissões baseado em strings.

Exemplo no código (inicializacao/login.py):

Python
tipo_usuario = email.split("@")[1]
if tipo_usuario == "prefeitura":
    # Direciona para o dashboard do gestor
elif tipo_usuario == "cidadao":
    # Direciona para o dashboard do cidadão
6. Estruturas de Repetição (while / for)
while True: Utilizado no arquivo main.py e em modulos/menu_crud.py para garantir que as interfaces de menus continuem em execução contínua até o acionamento de um evento de paragem (break).

for: Utilizado para percorrer coleções de dados, como na renderização do catálogo ou na busca por correspondências de texto (for obra in obras:).

7. Manipulação de Arquivos e Persistência (JSON)
Substituição de ficheiros .txt simples pela biblioteca estruturada json para garantir persistência robusta em formato de dicionários serializados.

Exemplo no código (modulos/cidadao.py):

Python
with open("dados/obras.json", "r", encoding="utf-8") as arquivo:
    return json.load(arquivo)
O gerenciador de contexto with open assegura a abertura segura em modo de leitura ("r") e garante o fecho automático do descritor de arquivo.

Desenvolvido pelo Squad 16.
