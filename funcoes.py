import json

""" função tenta abrir um arquivo, se ele existir a função abre ele no modo R de somente leitura, como f -- já se ele não existir, ele cria um dicionário vazio."""
def carregar_estoque(arquivo="estoque.json"):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  




"""a função salva no arquivo json, abrindo o arquivo no modo W, se o arquivo existir ele sera sobrescrito, se não existir ele será criado, como f -- então
    ele converte o dicionário "estoque" em um formato json"""
def salvar_estoque(estoque, arquivo="estoque.json"):
    with open(arquivo, "w") as f:
        json.dump(estoque, f, indent=4)




""" Recebe um produto com strip e upper para deixar sem espaços e em letra maiscula, verefica se já está no estoque, se não estiver, solicita a quantidade e o preço
do produto limitando eles a serem positivos ou 0. se todas as condições forem respeitadas o codigo adiciona o produto ao dicionário, se não, ele mostra qual foi o erro no final """
def adicionar_item(estoque):
    produto = input("Nome do item: ").strip().upper()
    

    if produto in estoque:
        print("Item já existe no estoque.")
        return

    try:
        quantidade = int(input("Quantidade do item: "))
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        
        preco = float(input("Preço do item: "))
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        
        estoque[produto] = {"quantidade": quantidade, "preco": preco}
        print("Item adicionado com sucesso.")
    
    except ValueError as e:
        print(f"Erro: {e}")




""" Função recebe o estoque, e pede ao usuário o produto que será atualizado, verifica se ele está no estoque, se ele estiver, dá a opção de mudar a quantidade
    continuando o mesmo critério de que não pode ser negativa, caso a condição seja respeitada, ele atualiza."""
def atualizar_quantidade(estoque):
    produto = input("Nome do item a atualizar: ").strip().upper()
    
    if produto not in estoque:
        print("Item não encontrado no estoque.")
        return

    try:
        quantidade = int(input("Nova quantidade: "))
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        
        estoque[produto]["quantidade"] = quantidade
        print("Quantidade atualizada com sucesso.")
    
    except ValueError as e:
        print(f"Erro: {e}")




"""A função recebe o estoque, e pede ao usuário qual é o produto da pesquisa, cria um dicionário "resultados" que terá todos os produtos do estoque que tem o termo da pesquisa.
   Para fazer isto, ele percorre o estoque.items(), que mostra todos os pares de chave e valor depois verifica se o termo da pesquisa está no nome do produto. Depois disso, ele
   verifica se tem valores no resultados, se sim, para cada item encontrado(No caso, só 1 pois não existe produtos repetidos e o code não da a opção de pesquisar 2 de uma vez) ele
   printa """
def pesquisar_item(estoque):
    termo = input("Termo de pesquisa: ").strip().upper()
    resultados = {
        produto: dados
        for produto, dados in estoque.items()
        if termo in produto
    }

    if resultados:
        for produto, dados in resultados.items():
            print(f"Item: {produto} | Quantidade: {dados['quantidade']} | Preço: R${dados['preco']:.2f}")
    else:
        print("Nenhum item encontrado.")




""" Verifica se o estoque não está vazio, se não estiver, faz o mesmo  de pegar os produtos(chaves do dicionário) e dados(valores) e printa eles."""
def exibir_estoque(estoque):
    if estoque:
        print("Estoque atual:")
        for produto, dados in estoque.items():
            print(f"Item: {produto} | Quantidade: {dados['quantidade']} | Preço: R${dados['preco']:.2f}""\n")
    else:
        print("O estoque está vazio.")


#Fiz estas por último devido a não serem solicitadas, fiz pelo extra
"""Pede o produto que será editado para o usuário, verifica se ele existe ou não, depois ele pede o novo preço, se for menos que zero o codigo mostra o
 erro que o codigo não pode ser negativo, depois ele atualiza o preço """
def editar_preco(estoque):
    produto = input("Nome do item a editar o preço: ").strip().upper()
    

    if produto not in estoque:
        print("Item não encontrado no estoque.")
        return

    try:
        novo_preco = float(input("Novo preço: "))
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        
        estoque[produto]["preco"] = novo_preco
        print("Preço atualizado com sucesso.")
    
    except ValueError as e:
        print(f"Erro: {e}")



"""Pede o produto que será excluido, verifica se ele existe, se existir, pede uma confirmação se é realmente oque 
o usuário quer, se sim, ele exclui, se não ele fala que foi cancelado """
def excluir_item(estoque):
    produto = input("Nome do item a excluir: ").strip().upper()
    

    if produto not in estoque:
        print("Item não encontrado no estoque.")
        return

    confirmacao = input(f"Tem certeza que deseja excluir '{produto}'? (s/n): ").strip().lower()
    if confirmacao == "s":
        del estoque[produto]
        print("Item excluído com sucesso.")
    else:
        print("Exclusão cancelada.")