# Sistema de Cadastro de Produtos

Este código implementa um sistema simples para cadastrar, listar, editar e remover produtos. Ele mantém os dados dos produtos em um arquivo JSON (`produtos.json`) e permite ao usuário interagir com o sistema por meio de um menu de opções.

Feito para um projeto na faculdade de Análise e Desenvolvimento de Sistemas no SENAC

## Variáveis Globais

- `produtos`: Lista que armazena os produtos cadastrados. Cada produto é representado como um dicionário com os campos `id`, `nome`, `preco`, `quantidade` e `preco_com_imposto`.

## Funções

### 1. `salvar_produtos()`
**Descrição**: Salva os produtos no arquivo `produtos.json`.

**Entrada**: Nenhuma.

**Saída**: Nenhuma (grava os dados no arquivo).

```python
def salvar_produtos():
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
```

### 2. `carregar_produtos()`
**Descrição**: Carrega os produtos do arquivo `produtos.json` para a variável global `produtos`. Caso o arquivo não exista, cria uma lista vazia.

**Entrada**: Nenhuma.

**Saída**: Nenhuma (modifica a variável global `produtos`).

```python
def carregar_produtos():
    global produtos
    if os.path.exists("produtos.json"):
        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)
    else:
        produtos = []
```

### 3. `produto_existe(nome)`
**Descrição**: Verifica se já existe um produto com o nome fornecido.

**Entrada**: 
- `nome` (string) - Nome do produto.

**Saída**: 
- `True` se o produto já existir, caso contrário `False`.

```python
def produto_existe(nome):
    return any(produto["nome"].lower() == nome.lower() for produto in produtos)
```

### 4. `encontrar_produto_por_id(id_buscado)`
**Descrição**: Procura um produto na lista de produtos pelo ID fornecido.

**Entrada**: 
- `id_buscado` (inteiro) - ID do produto a ser procurado.

**Saída**: 
- O produto correspondente ao ID ou `None` se não encontrado.

```python
def encontrar_produto_por_id(id_buscado):
    for produto in produtos:
        if produto["id"] == id_buscado:
            return produto
    return None
```

### 5. `cadastrar()`
**Descrição**: Permite ao usuário cadastrar um novo produto. O nome, preço e quantidade são solicitados, com validações de entrada e cálculos de imposto.

**Entrada**: Nenhuma.

**Saída**: Nenhuma (produto é adicionado à lista `produtos` e salvo no arquivo).

```python
def cadastrar():
    while True:
        # Solicitação e validação de entrada
        # Cálculo de imposto e geração de ID
        # Adiciona produto à lista e salva
```

### 6. `listar()`
**Descrição**: Exibe a lista de produtos cadastrados em formato tabular.

**Entrada**: Nenhuma.

**Saída**: Nenhuma (apresenta os produtos no terminal).

```python
def listar():
    print("\n--- Lista de Produtos ---")
    # Exibição da lista de produtos
```

### 7. `editar()`
**Descrição**: Permite ao usuário editar as informações de um produto existente. O nome, preço e quantidade podem ser alterados, com validações para garantir dados corretos.

**Entrada**: Nenhuma.

**Saída**: Nenhuma (produto é atualizado na lista produtos e salvo no arquivo).

```python
def editar():
    while True:
        # Solicitação do ID do produto a ser editado
        # Edição do produto com validações
        # Salvamento das alterações no arquivo
```

### 8. `remover()`
**Descrição**: Permite ao usuário remover um produto da lista. A remoção só é confirmada após a validação do ID e a confirmação do usuário.

**Entrada**: Nenhuma.

**Saída**: Nenhuma (produto é removido da lista produtos e salvo no arquivo).

```python
def remover():
    while True:
        # Solicitação do ID do produto a ser removido
        # Confirmação de remoção
        # Remoção do produto e salvamento
```

### 9. `deseja_continuar(acao)`
**Descrição**: Pergunta ao usuário se ele deseja continuar realizando a mesma operação (cadastrar, editar, remover) após a execução.

**Entrada**: 
- `acao` (string) - Descrição da ação realizada (ex: "cadastrar", "editar", "remover").

**Saída**: 
- `True` se o usuário deseja continuar, `False` caso contrário.

```python
def deseja_continuar(acao: str) -> bool:
    resposta = input(f"\nDeseja {acao} outro produto? (s/n): ").strip().lower()
    return resposta == 's'
```

### 10. `menu()`
**Descrição**: Exibe o menu principal para o usuário escolher a ação desejada: cadastrar, listar, editar, remover ou sair.

**Entrada**: Nenhuma.

**Saída**: Nenhuma (controle do fluxo de execução do programa).

```python
def menu():
    while True:
        # Exibição do menu e controle de fluxo
```

## Como o Programa Funciona

O programa inicia carregando os produtos do arquivo `produtos.json`.

O usuário interage com o sistema através do menu principal, onde pode escolher entre as opções de cadastro, listagem, edição e remoção de produtos.

As ações de cadastro, edição e remoção incluem validações de entrada, como garantir que o preço e a quantidade sejam válidos.

O sistema salva automaticamente os produtos no arquivo `produtos.json` sempre que há uma alteração.

## Requisitos

- Python 3.x
- A biblioteca `json` (inclusa no Python padrão) é utilizada para armazenar os dados dos produtos no formato JSON.
- A biblioteca `os` (inclusa no Python padrão) é utilizada para verificar a existência do arquivo de produtos.
