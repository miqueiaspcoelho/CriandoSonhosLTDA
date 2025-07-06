from model.item import Item
from collections import defaultdict

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
class ItemControler:
    @staticmethod
    def estruturar_dados(data: object)-> list:
        """
        Estrutura os dados de um objeto `Item` em uma lista.

        :param data: Objeto `Item` contendo as informações do item.
        :return: Lista com os dados do item (list).
        """
        result = []
        for item in data:
            result.append({"id": item[0],
                            "nome": item[1],
                            "preco": item[2],
                            "tipo": item[3],
                            "descricao": item[4]})
        return result

   

    def gerarMenuTexto(itens: list) -> str:
        """
        Gera uma string formatada com os itens do menu, agrupados por tipo e alinhados em colunas.

        :param itens: Lista de itens a serem formatados (list).
        :return: String formatada com os itens do menu (str).
        """
        # Cabeçalho padrão com colunas alinhadas
        header = f"{'ID':<4} {'Nome':<25} {'Preço':<10} {'Descrição'}"
        linha_sep = '-' * 70

        menu_texto = ''
        for item in itens:
            menu_texto += "\n" + linha_sep + "\n"
            menu_texto += f"{item['id']:<4} {item['nome']:<25} R$ {item['preco']:<7.2f} {item['descricao']}\n"

        return menu_texto.strip()

    
    #exibir todos os itens do menu
    @staticmethod
    def mostrar_itens_menu(database_name: str)-> str:
        """
        Chama a função que exibe todos os itens do menu no banco de dados.

        :param database_name: Nome do banco de dados a ser consultado (string).
        :return: Lista de itens (list) ou código de erro (string).
        """
        
        result  = Item.mostrar_itens_menu(database_name)
        itensMenu: list = ItemControler.estruturar_dados(result)
        itensMenuTexto: str = ItemControler.gerarMenuTexto(itensMenu)
        return itensMenuTexto
    
    
    #inserindo um item no banco de dados
    @staticmethod
    def insert_into_item(database_name: str, data: list) -> bool:
        """
        Insere um novo item na tabela de Itens no banco de dados.

        :param database_name: Nome do banco de dados (string).
        :param data: Objeto `Item` contendo as informações do item a ser inserido (Item).
        :return: True se a inserção for bem-sucedida, ou código de erro (string).
        """
        result = Item.insert_into_item(database_name,data)
        return result
    
    
    #tabela que liga cada pedido ao menu
    @staticmethod
    def insert_into_itens_pedidos(database_name: str, data: list) -> bool:
        """
        Insere a relação entre os itens e os pedidos na tabela ItensPedidos.

        :param database_name: Nome do banco de dados (string).
        :param data: Lista com o `IdPedido` e `IdItem` a serem inseridos (list).
        :return: True se a inserção for bem-sucedida, ou código de erro (string).
        """
        result = Item.insert_into_itens_pedidos(database_name,data)
        return result
    
    #tabela que liga cada pedido ao menu pesquisando
    @staticmethod
    def search_into_itens_pedidos_id(database_name: str, indice: int) -> list:
        """
        Pesquisa a lista de itens associados a um pedido, fornecendo o `IdPedido`.

        :param database_name: Nome do banco de dados (string).
        :param indice: ID do pedido para o qual os itens serão consultados (int).
        :return: Lista de itens relacionados ao pedido (list) ou código de erro (string).
        """
        result = Item.search_into_itens_pedidos_id(database_name,indice)
        return result
        
    #valor de um item informado pelo seu indice
    @staticmethod
    def valor_item(database_name: str, indice: int)-> object:
        """
        Retorna o valor (preço) de um item a partir do seu `IdItens`.

        :param database_name: Nome do banco de dados (string).
        :param indice: ID do item para o qual o preço será consultado (int).
        :return: Lista com o valor do item pesquisado ou código de erro (string).
        """
        result = Item.valor_item(database_name,indice)
        return result
    
    @staticmethod
    def search_item_id(database_name: str, indice:int) -> list:
        """
        Pesquisa as informações de um item (Nome, Tipo, Descrição, Preço) pelo seu `IdItens`.

        :param database_name: Nome do banco de dados (string).
        :param indice: ID do item para o qual as informações serão consultadas (int).
        :return: Informações do item (tuple) ou código de erro (string).
        """
        result = Item.search_item_id(database_name,indice)
        return result
    
    @staticmethod
    def create_item(data: list):
        """
        Cria um novo item
        :param data: Lista com as informações para criar um novo item
        :return: obj Item | false - em caso de erro
        """
        nome = data[0]
        preco = data[1]
        tipo = data[2]
        descricao = data[3]
        try:
            result = Item(nome, preco, tipo, descricao)
            return result
        except OSError as e:
            return False
        