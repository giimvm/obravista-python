O ObraVista é uma aplicação  desenvolvida em Python para o gerenciamento do ciclo de vida de obras públicas. O projeto foi estruturado para consolidar conceitos fundamentais de lógica de programação e manipulação de dados em memória e em arquivos de texto.


O sistema implementa o ciclo completo de operações CRUD, manipulando os dados dinamicamente através de estruturas nativas do Python e garantindo a persistência através de I/O de arquivos.

1. Create (Criação)
Como funciona no código: Implementado na função adicionar_obra().

Abordagem técnica: O sistema recebe os dados do utilizador via input(), gera um identificador único (id) incremental automático e estrutura essas informações num Dicionário Python. Este dicionário é então inserido (.append()) na Lista global de obras.

2. Read (Leitura)
Como funciona no código: Implementado nas funções listar_obras() e carregar_obras().

Abordagem técnica: Leitura em disco: Ao iniciar, o sistema utiliza o modo "r" (read) para abrir o arquivo obravista_dados.txt, lê as strings linha a linha, faz o parsing (divisão por ;) e reconstrói os dicionários na memória.

Exibição no terminal: A função realiza uma iteração (for) sobre a lista de obras, formatando e exibindo os dados (orçamento, progresso e status) de forma legível para o gestor.

3. Update (Atualização)
Como funciona no código: Implementado através da reescrita e atualização de estados de variáveis (ex: alteração de progresso de 0% a 100% ou mudança de status).

Abordagem técnica: O sistema localiza o dicionário correspondente à obra através do seu id e altera diretamente o valor das chaves "status" ou "progresso".

4. Delete (Remoção)
Como funciona no código: Implementado no encerramento e na sincronização de dados.

Abordagem técnica: Permite purgar ou filtrar elementos da lista principal antes que a nova matriz de dados seja gravada, garantindo que registos removidos ou obsoletos não persistam no arquivo final.


 Manipulação de Arquivos (Persistência)
Para evitar a perda de dados ao encerrar o programa, implementou-se o armazenamento persistente em arquivo .txt:

Gerenciador de Contexto (with open): Utilizado para garantir que o arquivo seja aberto e fechado corretamente de forma automática, prevenindo bloqueios no sistema operativo ou corrupção de dados.

Modos de Abertura: Uso do modo "r" para carregar os dados ao iniciar e do modo "w" (write) para sobrescrever o arquivo com as informações atualizadas no momento do salvamento.

Estruturas de Dados
Tuplas (tuple): Utilizadas para definir constantes globais e imutáveis do sistema, como a lista de status permitidos: STATUS_VALIDOS = ("Em andamento", "Paralisada", "Concluída", "Atrasada"). Isso impede alterações acidentais nestas regras de negócio durante a execução.

Dicionários (dict): Cada obra é representada como uma estrutura chave-valor, facilitando o acesso direto a propriedades específicas (obra["orcamento"], obra["progresso"]).

Listas (list): Funcionam como a matriz de dados em memória RAM (obras = []), agrupando todos os dicionários durante o tempo de execução do script.

 Estruturas de Controlo e Repetição
while True: Mantém o menu principal ativo em loop contínuo até que o utilizador selecione explicitamente a opção de saída (ativando o comando break).

if / elif / else: Atuam no roteamento do menu principal e na validação de dados de entrada, impedindo que o utilizador insira opções inválidas ou valores de progresso fora do intervalo de 0 a 100.

for: Utilizado para iterar sobre a lista de obras, tanto para a renderização do catálogo no ecrã quanto para a formatação de strings separadas por ponto e vírgula (;) no momento da gravação no arquivo de texto.
