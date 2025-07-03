#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#importando a classe Pedido
from model.pedido import Pedido


#definindo a classe PedidoControler, nela estão os métodos
class PedidoControler:
    
    #adiciona um pedido ao banco de dados
    @staticmethod
    def insert_into_pedidos(database_name: str, data: object):
       """
        Adiciona um novo pedido ao banco de dados.
        
        :param database_name: Nome do banco de dados (string)
        :param data: Objeto contendo os dados do pedido (Pedido)
        :return: True se inserção for bem-sucedida, código de erro caso contrário
        """
       result  = Pedido.insert_into_pedidos(database_name,data)
       return result
        
    #busca todos os pedidos existentes    
    @staticmethod
    def search_in_pedidos_all(database_name: str) -> list:
        """
        Recupera todos os pedidos do banco de dados.
        
        :param database_name: Nome do banco de dados (string)
        :return: Lista de todos os pedidos, ou código de erro em caso de falha
        """
        search = Pedido.search_in_pedidos_all(database_name)
        result=[]
        new_item = ''
        if len(search)>0:            
            for elem in search:

                new_item = Pedido(elem[1],elem[2],elem[3],elem[4],elem[5])
                result.append(new_item)

        return result
        
        
        
    #buscar pedido por id
    @staticmethod
    def search_in_pedidos_id(database_name: str, indice: int) -> list:
       """
        Recupera um pedido específico pelo seu ID.
        
        :param database_name: Nome do banco de dados (string)
        :param indice: ID do pedido a ser recuperado (int)
        :return: Lista contendo o pedido encontrado, ou código de erro em caso de falha
        """
       result = Pedido.search_in_pedidos_id(database_name,indice)
       return result
    
    @staticmethod
    def update_pedido_status_id(database_name: str, indice:int, status: str) -> bool:
        """
        Atualiza status de um determinado pedido informado pelo indice
        :param database_name: Nome do banco de dados (string).
        :param indice: ID do pedido a ser buscado (int).
        :param status: Novo estado do pedido a ser atualizado (int)
        :return: Dados do pedido (list) ou código de erro (string).
        """
        if status==1:
            status = 'preparo'
        elif status==2:
            status = 'pronto'
        elif status==3:
            status = 'entregue'
        else:
            return False
        result = Pedido.update_pedido_status(database_name, indice, status)
        return result
    
    @staticmethod
    def get_id_all(database_name):
        lista = []
        id_pedidos = Pedido.get_id_all(database_name)
        if id_pedidos:
            for id in id_pedidos:
                lista.append(id[0])
        return lista
        
        
#---------------MANUTENÇÕES---------------#
#pefectiva - atualizar estado do pedido - fazendo
#perfectiva - saber quanto está sendo o faturamento da loja em um período definido pelo usuário
    
#adaptiva - mostrar todos os pedidos - feita
#adaptativa - migrar de txt para um banco de dados sqlite3 - não se aplica
    