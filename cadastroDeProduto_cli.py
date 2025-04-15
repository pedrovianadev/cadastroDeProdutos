import json
import os

produtos = []

# Função para salvar os produtos no arquivo
def salvar_produtos():
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

# Função para carregar os produtos do arquivo
def carregar_produtos():
    global produtos
    if os.path.exists("produtos.json"):
        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)
    else:
        produtos = []

# Função para verificar se o produto já existe
def produto_existe(nome):
    return any(produto["nome"].lower() == nome.lower() for produto in produtos)

# Função para encontrar produto por ID
def encontrar_produto_por_id(id_buscado):
    for produto in produtos:
        if produto["id"] == id_buscado:
            return produto
    return None

# Função para cadastrar produtos
def cadastrar():
    while True:
        print("\n--- Cadastrar Produto---")
        nome = input("Nome do produto: ")

        if produto_existe(nome):
            print("Erro: Produto já cadastrado. Tente outro nome.")
            continue  # Volta ao início do loop

        try:
            preco = float(input("Preço do produto: R$ "))
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Erro: valor inválido. Use apenas números. Tente novamente.")
            continue  # Retorna ao início do loop, tentando novamente

        if preco <= 0:
            print("Erro: O preço deve ser maior que zero. Tente novamente.")
            continue  # Retorna ao início do loop, tentando novamente

        if quantidade < 0:
            print("Erro: A quantidade não pode ser negativa. Tente novamente.")
            continue  # Retorna ao início do loop, tentando novamente

        try:
            # Cálculo do imposto de 15%
            imposto = preco * 0.15
            preco_com_imposto = preco + imposto
        except Exception as e:
            print(f"Erro ao calcular o imposto: {e}")
            continue  # Caso ocorra algum erro no cálculo, continua no loop

        # Gera ID automaticamente
        novo_id = 1 if not produtos else produtos[-1]["id"] + 1

        # Cria o produto como dicionário
        produto = {
            "id": novo_id,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "preco_com_imposto": round(preco_com_imposto, 2)
        }

        produtos.append(produto)
        salvar_produtos()
        print("\nProduto cadastrado com sucesso")

        if not deseja_continuar("cadastrar"):
            break

# Função para listar os produtos
def listar():
    print("\n--- Lista de Produtos ---")

    if not produtos:
        print("\n Nenhum produto cadastrado.")
        return

    # Cabeçalho da tabela
    print(f"{'ID':<4} | {'Nome':<15} | {'Preço':<10} | {'Qtd':<5} | {'Preço c/ Imposto':<18}")
    print("-" * 60)

    for produto in produtos:
        print(f"{produto['id']:<4} | {produto['nome']:<15} | R$ {produto['preco']:<8.2f} | {produto['quantidade']:<5} | R$ {produto['preco_com_imposto']:<.2f}")

# Função para editar produtos
def editar():
    if not produtos:
        print("\nNenhum produto cadastrado para editar.")
        return

    while True:
        listar()  # Mostra os produtos antes de editar

        try:
            id_editar = int(input("\nDigite o ID do produto que deseja editar: "))
        except ValueError:
            print("Erro: ID inválido. Tente novamente.")
            continue  # Retorna ao início do loop, pedindo novamente o ID

        produto_encontrado = False

        for produto in produtos:
            if produto["id"] == id_editar:
                produto_encontrado = True
                print(f"\nEditando produto: {produto['nome']}")

                novo_nome = input(f"Novo nome (atual: {produto['nome']}): ")
                if novo_nome.strip() == "":  # Evita que o nome seja vazio
                    print("Erro: O nome não pode ser vazio.")
                    continue  # Volta ao início do loop, pedindo um nome válido

                try:
                    novo_preco = input(f"Novo preço (atual: R$ {produto['preco']:.2f}): ")
                    if novo_preco.strip():  # Verifica se o preço foi alterado
                        produto["preco"] = float(novo_preco)
                        if produto["preco"] <= 0:
                            print("Erro: O preço deve ser maior que zero. Tente novamente.")
                            continue
                except ValueError:
                    print("Erro: Preço inválido. Mantido o valor anterior.")
                    continue  # Caso o preço seja inválido, continua sem alterações

                try:
                    nova_quantidade = input(f"Nova quantidade (atual: {produto['quantidade']}): ")
                    if nova_quantidade.strip():  # Verifica se a quantidade foi alterada
                        produto["quantidade"] = int(nova_quantidade)
                        if produto["quantidade"] < 0:
                            print("Erro: A quantidade não pode ser negativa. Tente novamente.")
                            continue
                except ValueError:
                    print("Erro: Quantidade inválida. Mantido o valor anterior.")
                    continue  # Caso a quantidade seja inválida, continua sem alterações

                try:
                    # Recalcula o imposto
                    imposto = produto["preco"] * 0.15
                    produto["preco_com_imposto"] = round(produto["preco"] + imposto, 2)
                except Exception as e:
                    print(f"Erro ao recalcular o imposto: {e}")
                    continue  # Caso ocorra algum erro no cálculo, continua o loop

                salvar_produtos()
                print("\nProduto atualizado com sucesso.")
                break  # Sai do loop de edição após atualizar o produto

        if not produto_encontrado:
            print("Produto com esse ID não foi encontrado.")

        if not deseja_continuar("editar"):
            break

# Função para remover produto
def remover():
    if not produtos:
        print("\nNenhum produto cadastrado para remover.")
        return

    while True:
        listar()  # Mostra os produtos antes de remover

        try:
            id_remover = int(input("\nDigite o ID do produto que deseja remover: "))
        except ValueError:
            print("Erro: ID inválido. Tente novamente.")
            continue  # Retorna ao início do loop, pedindo novamente o ID

        encontrado = False
        for produto in produtos:
            if produto["id"] == id_remover:
                encontrado = True
                confirmacao = input(f"Tem certeza que deseja remover '{produto['nome']}'? (s/n): ").strip().lower()
                
                if confirmacao == 's':
                    try:
                        produtos.remove(produto)  # Tenta remover o produto da lista
                        salvar_produtos()  # Salva as alterações no arquivo
                        print("\nProduto removido com sucesso.")
                    except Exception as e:
                        print(f"Erro ao tentar remover o produto: {e}")
                elif confirmacao == 'n':
                    print("\nRemoção cancelada.")
                else:
                    print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
                break  # Sai do loop após a remoção ou cancelamento

        if not encontrado:
            print("Produto com esse ID não foi encontrado.")

        if not deseja_continuar("remover"):
            break

# Função para perguntar se o usuário deseja continuar com a operação
def deseja_continuar(acao: str) -> bool:
    resposta = input(f"\nDeseja {acao} outro produto? (s/n): ").strip().lower()
    return resposta == 's'

# Função menu
def menu():
    while True:
        print("\n--- Menu ---")
        print("[1] - Cadastrar Produto")
        print("[2] - Listar Produtos")
        print("[3] - Editar Produto")
        print("[4] - Remover Produto")
        print("[0] - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            editar()
        elif opcao == "4":
            remover()
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Carrega a lista de produtos
carregar_produtos()

# Inicia o programa chamando a função menu
menu()
