# Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controler.itemControler import ItemControler

class Janela3:
    @staticmethod
    def mostrar_janela3(database_name: str) -> None:
        """
        View para cadastro de novos itens no menu
        
        :param database_name: Nome do banco de dados
        :return: None
        """
        print("\n---------- Cadastro de Itens ----------")
        
        while True:
            # Solicitação dos dados do item
            print("\nPreencha os dados do novo item:")
            
            # Nome (campo obrigatório)
            nome = input("Nome do item: ")
            while not nome.strip():
                print("Erro: O nome do item é obrigatório!")
                nome = input("Nome do item: ")
            
            # Descrição (campo obrigatório)
            descricao = input("Descrição: ")
            while not descricao.strip():
                print("Erro: A descrição é obrigatória!")
                descricao = input("Descrição: ")
            
            # Preço (deve ser numérico)
            preco = None
            while preco is None:
                try:
                    preco = float(input("Preço (R$): "))
                    if preco <= 0:
                        print("Erro: O preço deve ser maior que zero!")
                        preco = None
                except ValueError:
                    print("Erro: Digite um valor numérico válido!")
            
            # Categoria
            print("\nSelecione a categoria:")
            print("1 - Pizza")
            print("2 - Bebida")
            print("3 - Sobremesa")
            print("4 - Outro")
            
            opcao = input("Opção: ")
            while opcao not in ['1', '2', '3', '4']:
                print("Erro: Selecione uma opção válida (1-4)!")
                opcao = input("Opção: ")
            
            categorias = {
                '1': 'Pizza',
                '2': 'Bebida',
                '3': 'Sobremesa',
                '4': 'Outro'
            }
            tipo = categorias[opcao]
            
            # Confirmação
            print("\nConfirme os dados do item:")
            print(f"Nome: {nome}")
            print(f"Descrição: {descricao}")
            print(f"Preço: R$ {preco:.2f}")
            print(f"Categoria: {tipo}")
            
            confirmacao = input("\nConfirmar cadastro? (S/N): ").lower()
            while confirmacao not in ['s', 'n']:
                print("Erro: Digite S ou N!")
                confirmacao = input("Confirmar cadastro? (S/N): ").lower()
            
            if confirmacao == 'n':
                print("Cadastro cancelado.")
                break
            
            # Criação e inserção do item
            item_data = [nome, preco, tipo, descricao]
            item = ItemControler.create_item(item_data)
            
            if item is False:
                print("\nErro ao criar o item!")
                continue
            
            resultado = ItemControler.insert_into_item(database_name, item)
            
            if resultado is True:
                print("\nItem cadastrado com sucesso!")
            else:
                print(f"\nErro ao cadastrar item: {resultado}")
            
            # Verificar se deseja continuar
            continuar = input("\nDeseja cadastrar outro item? (S/N): ").lower()
            while continuar not in ['s', 'n']:
                print("Erro: Digite S ou N!")
                continuar = input("Deseja cadastrar outro item? (S/N): ").lower()
            
            if continuar == 'n':
                print("Retornando ao menu principal...")
                break