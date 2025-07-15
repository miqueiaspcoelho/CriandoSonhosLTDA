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
from model.pedido import Pedido

#importando os módulos de controle
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

#criação da classe janela
class Janela1:
    
    @staticmethod
    def mostrar_janela1(database_name: str) -> None:
        """
        View para o usuário utilizar o software
        
        return None
        """
        
        a = 'y'
        
        # SOLUÇÃO Nº 1 (Perfectiva): Melhorando a exibição do menu.
        menu_itens = ItemControler.mostrar_itens_menu(database_name)
        print('\n-------------------- Menu --------------------')
        print(f'{"ID":<5}| {"Nome":<20}| {"Preço":<10}| {"Tipo":<15}')
        print('-' * 55)
        for item in menu_itens:
            print(f'{item[0]:<5}| {item[1]:<20}| R$ {item[2]:<7.2f}| {item[3]:<15}')
        print('-' * 55)
        
        while a=='y':
            lista_itens = []
            valor_total=0
            
            # SOLUÇÃO Nº 2 (Corretiva): Validação de entrada robusta para 'sim'/'não'
            # Lista de possíveis respostas afirmativas
            respostas_positivas = ['s', 'sim']
            # Lista de possíveis respostas negativas (agora incluindo a versão com acento)
            respostas_negativas = ['n', 'nao', 'não']
            # Trata a entrada do usuário: remove espaços, converte para minúsculas e normaliza (remove acentos)
            # A normalização não é nativa, mas a lógica de verificação cobre isso
            entrada_usuario = str(input('Deseja cadastrar um novo pedido? (s-Sim / n-Não): ')).lower().strip()
            
            if entrada_usuario in respostas_positivas: # A verificação agora é com as respostas positivas:
                print('----------Cadastrar pedido----------\n')
                adicionar = 'y'
                pedidos = PedidoControler.search_in_pedidos_all(database_name)
                numero_pedido = len(pedidos)+1
                while adicionar == 'y':
                    item = int(input('Numero do item: '))
                    quantidade = int(input('Quantidade: '))
                    
                    #calculando em tempo de execução o valor do pedido
                    a = ItemControler.valor_item(database_name, item)
                    b = a[0][0]*quantidade
                    print(b)
                    valor_total+=b
                    
                    for x in range(0,quantidade):#acrescentado o mesmo item várias vezes, de acordo com a quantidade
                        lista_itens.append((numero_pedido,item))
                    
                    # Validação robusta para adicionar novo item
                    while True:
                        adicionar_input = str(input('Adicionar novo item? (s-Sim, n-Nao): ')).lower().strip()
                        if adicionar_input in respostas_positivas:
                            adicionar = 's'
                            break
                        elif adicionar_input in respostas_negativas:
                            adicionar = 'n'
                            break
                        else:
                            print('Resposta inválida! Digite "s" para Sim ou "n" para Não.')
                
                print('\n----------Finalizar pedido----------\n')
                print(f'Numero do pedido: {numero_pedido}')
                delivery = str(input('Delivery (S/N): ')).lower()
                if delivery=='s':
                    delivery = True
                elif delivery=='n':
                    delivery = False
                else:
                    print('Valor incorreto, recomeçando')
                    break
                endereco = str(input('Endereco:'))
                status_aux = int(input('status: 1-preparo, 2-pronto, 3-entregue: '))
                if status_aux == 1:
                    status = 'preparo'
                if status_aux == 2:
                    status = 'pronto'
                else:
                    status = 'entregue'
 
                print(f'Valor Final: R${valor_total}')
                data_hoje = date.today()
                data_formatada = data_hoje.strftime('%d/%m/%Y')
                print(data_formatada)
                print(endereco)
                pedido = Pedido(status, str(delivery), endereco,data_formatada,float(valor_total))
                PedidoControler.insert_into_pedidos(database_name,pedido)
                for elem in lista_itens:
                    ItemControler.insert_into_itens_pedidos(database_name,elem)
                
            elif entrada_usuario in respostas_negativas:
                print('Voltando ao Menu inicial')
                time.sleep(2)
                break