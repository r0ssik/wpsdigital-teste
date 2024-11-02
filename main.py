import json
from funcoes import (
    carregar_estoque,
    salvar_estoque,
    adicionar_item,
    atualizar_quantidade,
    editar_preco,           
    excluir_item,           
    pesquisar_item,
    exibir_estoque,
)

#Basicamente a main dá as opções pro usuário, e conforme ele escolhe, ela chama as funções que estão no outro arquivo.
def main():
    estoque = carregar_estoque()
    while True:
        print("\nSistema de Gerenciamento de Estoque")
        print("1. Adicionar novo item")
        print("2. Atualizar quantidade de item existente")
        print("3. Editar preço de um item")  
        print("4. Excluir item")             
        print("5. Pesquisar item")
        print("6. Exibir todo o estoque")
        print("7. Salvar e sair")

        opcao = input("Escolha uma opção (Digite o número da opção): ")

        if opcao == "1":
            adicionar_item(estoque)
        elif opcao == "2":
            atualizar_quantidade(estoque)
        elif opcao == "3":
            editar_preco(estoque)  
        elif opcao == "4":
            excluir_item(estoque) 
        elif opcao == "5":
            pesquisar_item(estoque)
        elif opcao == "6":
            exibir_estoque(estoque)
        elif opcao == "7":
            salvar_estoque(estoque)
            print("Estoque salvo. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")



main()
