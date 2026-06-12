# 🏗️ ObraVista

Sistema de gestão e acompanhamento de obras públicas desenvolvido em Python, utilizando arquitetura modular e persistência de dados em arquivos JSON.

O objetivo do projeto é permitir que diferentes perfis de utilizadores acompanhem, gerenciem e atualizem informações relacionadas às obras públicas do município, com controle de acesso baseado no domínio do e-mail utilizado no login.

---

## 📋 Funcionalidades

### 👤 Cidadão

* Visualização de obras públicas ativas.
* Pesquisa de obras por nome.
* Filtragem de informações relevantes.
* Consulta de detalhes das obras.

### 🏢 Empresa

* Acesso ao painel específico da empreiteira.
* Consulta de informações relacionadas às obras sob sua responsabilidade.

### 🏛️ Gestor (Prefeitura)

* Cadastro de novas obras.
* Atualização de informações das obras.
* Gerenciamento geral do sistema.

### 🔐 Gestão de Usuários

* Cadastro de novos utilizadores.
* Autenticação por e-mail e senha.
* Atualização de dados cadastrais.
* Exclusão de contas.

---

# 🗂️ Estrutura do Projeto

```text
ObraVista/
│
├── main.py
│
├── dados/
│   ├── obras.json
│   └── usuarios.json
│   └── relatorios.json
│
├── inicializacao/
│   ├── autenticacao.py
│   ├── cadastro.py
│   ├── crud.py
│   └── login.py
│
└── modulos/
    ├── cidadao.py
    ├── empresa.py
    ├── gestor.py
    └── menu_crud.py
```

---

# 🏛️ Arquitetura Modular

O sistema foi desenvolvido seguindo princípios de modularização, separando cada responsabilidade em arquivos específicos.

| Arquivo           | Responsabilidade                 |
| ----------------- | -------------------------------- |
| `main.py`         | Fluxo principal da aplicação     |
| `autenticacao.py` | Validação de credenciais         |
| `cadastro.py`     | Cadastro de novos utilizadores   |
| `crud.py`         | Atualização e exclusão de contas |
| `login.py`        | Encaminhamento dos utilizadores  |
| `cidadao.py`      | Funcionalidades do cidadão       |
| `empresa.py`      | Funcionalidades da empresa       |
| `gestor.py`       | Funcionalidades administrativas  |
| `menu_crud.py`    | Interface de gestão de perfil    |

---

# 🔄 Implementação do CRUD

## Create (Criar)

Responsável pelo cadastro de novos dados no sistema.

### Utilizado em:

* Cadastro de utilizadores
* Cadastro de obras públicas

**Arquivos:**

* `inicializacao/cadastro.py`
* `modulos/gestor.py`

---

## Read (Ler)

Responsável pela consulta e visualização dos dados.

### Utilizado em:

* Busca de obras
* Pesquisa de obras
* Exibição de informações

**Arquivos:**

* `modulos/cidadao.py`

**Funções principais:**

* `buscar_obras_ativas()`
* `exibir_card_obra()`
* `pesquisar_obra()`

---

## Update (Atualizar)

Responsável pela alteração de informações já existentes.

### Arquivo:

* `inicializacao/crud.py`

**Funções:**

* `atualizar_nome()`
* `atualizar_email()`
* `atualizar_senha()`

---

## Delete (Excluir)

Responsável pela remoção de dados.

### Arquivo:

* `inicializacao/crud.py`

**Função:**

* `deletar_usuario()`

---

# 📚 Conceitos da Disciplina Aplicados

## 1️⃣ Funções

O projeto utiliza funções para encapsular responsabilidades específicas e promover reutilização de código.

### Exemplos

```python
def login():
    pass

def pesquisar_obra():
    pass
```

---

## 2️⃣ Dicionários

Utilizados para representar entidades complexas do sistema.

### Exemplo

```python
obra["nome"]
obra["bairro"]
obra["progresso"]
```

Cada registro carregado dos arquivos JSON é convertido automaticamente para um dicionário Python.

---

## 3️⃣ Listas

Utilizadas para armazenamento e manipulação dinâmica de coleções de dados.

### Exemplos

```python
obras_ativas = []
resultados = []
```

Permitem buscas, filtragens e inserções de novos registros.

---

## 4️⃣ Tuplas

Utilizadas para armazenar conjuntos imutáveis de valores, como constantes e regras de negócio.

### Exemplo

```python
STATUS_PERMITIDOS = (
    "Planejamento",
    "Em andamento",
    "Concluída"
)
```

---

## 5️⃣ Estruturas Condicionais

Responsáveis pela validação de permissões e fluxo de navegação.

### Exemplo

```python
tipo_usuario = email.split("@")[1]

if tipo_usuario == "prefeitura":
    gestor()
elif tipo_usuario == "cidadao":
    cidadao()
```

---

## 6️⃣ Estruturas de Repetição

### While

Utilizado para manter os menus ativos até que o utilizador escolha sair.

```python
while True:
    menu()
```

### For

Utilizado para percorrer listas de utilizadores e obras.

```python
for obra in obras:
    print(obra["nome"])
```

---

## 7️⃣ Manipulação de Arquivos JSON

O sistema utiliza persistência de dados através de arquivos JSON.

### Exemplo

```python
with open("dados/obras.json", "r", encoding="utf-8") as arquivo:
    obras = json.load(arquivo)
```

O gerenciador de contexto `with` garante abertura e fechamento seguro dos arquivos.

---

# 🚀 Tecnologias Utilizadas

* Python 3
* JSON
* Programação Modular
* CRUD
* Estruturas de Dados
* Manipulação de Arquivos

---

# 👨‍💻 Equipe

**Squad 16**

Projeto desenvolvido para aplicação dos conceitos fundamentais de Lógica de Programação, Estruturas de Dados e Modularização em Python.

---

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
