#import de model
from model.database import Database

import sqlite3
from sqlite3 import Error
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class DatabaseControler:

    #conectando/criando o banco, caso ele não exista
    @staticmethod
    def conect_database(database_name: str) -> object:
        """
        Responsável por criar uma conexão com o banco de dados
    
        :param database_name: string
        :return conn: object
        """
        
        Database(database_name)
        conn = Database.conect_database(database_name)
        return conn

    #criando a tabela dos produto, caso não exista
    @staticmethod
    def create_table_itens(conn: object) -> None:
        """
        Caso não exista, cria uma tabela de chamados em um banco de dados sqlite3

        :param conn: obj
        :return result: obj
        """
        result = Database.create_table_itens(conn)
        return result
    
    #criando a tabela dos pedidos, caso não exista
    @staticmethod
    def create_table_pedidos(conn: object) -> None:
        """
        Caso não exista, cria uma tabela de pedidos em um banco de dados sqlite3

        :param conn: obj
        :return result: obj
        """
        result = Database.create_table_pedidos(conn)
        return result
    
    #criando a tabela dos itens_pedidos, caso não exista
    @staticmethod
    def create_table_itens_pedidos(conn: object) -> None:
        """
        Caso não exista, cria uma tabela de pedidos em um banco de dados sqlite3

        :param conn: obj
        :return result: obj
        """
        result = Database.create_table_itens_pedidos(conn)
        return result