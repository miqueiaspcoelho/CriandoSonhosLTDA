from model.database import Database
#classe pedido
class Pedido:
    def __init__(self,
                status: str,
                delivery: bool,
                endereco: str,
                date: str,
                valor_total: float
                ) -> None:
        """
        Modelo de objeto Pedido
        
        :param status: string
        :param delivery: bool
        :param endereco: string
        
        :return None
        """
        self.status = status
        self.delivery = delivery
        self.endereco = endereco,
        self.date = date
        self.valor_total = valor_total
    

    #adiciona um pedido ao banco de dados
    @staticmethod
    def insert_into_pedidos(database_name: str, data: object):
        """
        Insere um novo pedido no banco de dados.

        :param database_name: Nome do banco de dados (string).
        :param data: Objeto Pedido contendo as informações do pedido (Pedido).
        :return: True se a inserção for bem-sucedida, ou código de erro (string).
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO Pedidos (Status, Delivery, Endereco, Data, ValorTotal) VALUES (?,?,?,?,?);
                    ''', (data.status, data.delivery, data.endereco[0], data.date, data.valor_total))# (manutenção) - bug(corretiva) -> sem endereco[0] quando endereço vazio ele quebra
                conn.commit()
                return True
        except OSError as e:
            print(e)
            return 'P1'
        
    #busca todos os pedidos existentes    
    @staticmethod
    def search_in_pedidos_all(database_name: str) -> list:
        """
        Busca todos os pedidos existentes no banco de dados.

        :param database_name: Nome do banco de dados (string).
        :return: Lista de todos os pedidos (list) ou código de erro (string).
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                SELECT * FROM Pedidos order by IdPedido asc;
                ''')
                rows = cursor.fetchall()               
                return(rows)

        except OSError as e:
            print(e)
            return 'P2'
        
        
    #buscar pedido por id
    @staticmethod
    def search_in_pedidos_id(database_name: str, indice: int) -> list:
        """
        Busca um pedido específico pelo seu ID.

        :param database_name: Nome do banco de dados (string).
        :param indice: ID do pedido a ser buscado (int).
        :return: Dados do pedido (list) ou código de erro (string).
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f'''
                SELECT * FROM Pedidos WHERE IdPedido = {indice};
                ''')
                rows = cursor.fetchall()               
                return(rows)

        except OSError as e:
            print(e)
            return 'P3'
    
    @staticmethod
    def update_pedido_status(database_name: str, indice: int, status: str) -> bool:
        """
        Atualiza status de um determinado pedido informado pelo indice
        :param database_name: Nome do banco de dados (string).
        :param indice: ID do pedido a ser buscado (int).
        :param status: Novo estado do pedido a ser atualizado (string)
        :return: Dados do pedido (list) ou código de erro (string).
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f'''
                SELECT * FROM Pedidos WHERE IdPedido = {indice};
                ''')
                rows = cursor.fetchall()
                if len(rows)>0:
                    cursor.execute(f'''
                        UPDATE Pedidos SET status='{status}' WHERE IdPedido={indice};
                    ''')
                    return True
                else:
                    return False

        except OSError as e:
            print(e)
            return False
        
    @staticmethod
    def get_id_all(database_name):
        """
        Retorna o id de todos os pedidos existentes
        :param database_name: nome do banco de dados a ser acessado (str)
        :return: lista com os id || código de erro
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                SELECT IdPedido FROM Pedidos order by IdPedido asc;
                ''')
                rows = cursor.fetchall()               
                return(rows)

        except OSError as e:
            print(e)
            return 'P4'
'''
Códigos de Erro

insert_into_pedidos - P1
search_in_pedidos_all - P2
search_in_pedidos_id - P3
get_id_all - P4

'''