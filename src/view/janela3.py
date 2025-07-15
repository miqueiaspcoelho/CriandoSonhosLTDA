import sys
from pathlib import Path

# Configuração de caminho
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Imports necessários
from model.item import Item
from controler.itemControler import ItemControler

class Janela3:

    @staticmethod
    def mostrar_janela3(database_name: str) -> None:
        print("=== Cadastro de Item no Cardápio ===")
        
        nome = input("Nome do item: ").strip()
        descricao = input("Descrição: ").strip()
        
        try:
            preco = float(input("Preço (ex: 35.0): ").strip())
        except ValueError:
            print("⚠️ Preço inválido! Operação cancelada.")
            return

        print("Categorias disponíveis:")
        print("1 - Pizza")
        print("2 - Bebida")
        print("3 - Sobremesa")
        print("4 - Outro")

        categoria_opcao = input("Digite o número da categoria: ").strip()
        categoria_dict = {'1': 'Pizza', '2': 'Bebida', '3': 'Sobremesa', '4': 'Outro'}

        if categoria_opcao not in categoria_dict:
            print("⚠️ Categoria inválida! Operação cancelada.")
            return

        categoria = categoria_dict[categoria_opcao]

        # Validações extras
        if not nome or not descricao:
            print("⚠️ Todos os campos são obrigatórios! Operação cancelada.")
            return

        item = Item(nome, preco, categoria, descricao)
        try:
            ItemControler.insert_into_item(database_name, item)
            print("✅ Item cadastrado com sucesso!")
        except Exception as e:
            print(f"⚠️ Erro ao cadastrar item: {e}")
