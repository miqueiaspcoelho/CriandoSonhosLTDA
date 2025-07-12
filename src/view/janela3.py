#para pegar a data de hoje
from datetime import date
import time

#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#importando os módulos de model
from model.item import Item

#importando os módulos de controle
from controler.itemControler import ItemControler

#Importando os módulos de banco de dados
from model.item import Item

#criação da classe janela
class Janela3:
    
    @staticmethod
    def mostrar_janela3(database_name: str) -> None:
        """
        View para cadastro de itens
        
        return None
        """
        
        a = 'y'
        lista_itens = []
        
        print('----------Cadastro de Item do Menu----------\n')
        print('Deseja continuar? y-Sim, n-Nao: ')
        deseja_continuar = input('-> ')
        

        if deseja_continuar=='y':
          nome = str(input('Nome do item: '))
          preco = float(input('Preço do item: '))
          tipo = str(input('Tipo do item: '))
          descricao = str(input('Descrição do item: '))
          objetoItem = Item(nome, preco, tipo, descricao)
          
          a = str(input('Cadastrar item (y-Sim, n-Nao): '))
          if a.lower() in 'y sim':
            ItemControler.insert_into_item(database_name, objetoItem)
            print('Item cadastrado com sucesso!')
          elif a.lower() in 'n nao':
            print('Voltando ao Menu inicial')
            time.sleep(2)
            return
          else:
            print('Opção inválida. Voltando ao Menu inicial')
            time.sleep(2)
            return

        elif a=='n':
          print('Voltando ao Menu inicial')
          time.sleep(2)
          return