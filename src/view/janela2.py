#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

class Janela2:
    def mostrar_janela2(database_name:str):
        faturamento = 0
        print('------Pesquisar Pedido--------')
        q = input('Unico-1\nTodos-2\nAtualizar Estado-3\nDigite: ') 
        #verificação de entrada de índice do pedido
+       if q=='1': 
            try:
                indice = int(input('Indice do pedido: '))
            except ValueError:
                print('ERRO: Digite um número válido para o índice do pedido.')
                return

            informacoes_pedido = PedidoControler.search_in_pedidos_id(database_name, indice)
            if not informacoes_pedido:
                print(f'Pedido com o índice {indice} não encontrado.')
                return
            
            resume = ItemControler.search_into_itens_pedidos_id(database_name, indice)
            quantidade_itens = len(resume)
            exibir_tela = ''
            for elem in resume:
                exibir_tela += f'Tipo: {elem[2]}| Sabor: {elem[0]}| Descricao: {elem[3]}| R$ {elem[1]}|\n'
            print(f'\nResumo do pedido {indice}: \n {exibir_tela}\nItens: {quantidade_itens}\n\n')
            
            pedido_data = informacoes_pedido[0] 
            print(f'Status: {pedido_data[1]}\nDelivery: {pedido_data[2]}\nEndereco: {pedido_data[3]}\nData: {pedido_data[4]}\nR$ {pedido_data[5]}')
            print('Voltando ao menu inicial\n')
            
        elif q=='2': 
            row = PedidoControler.search_in_pedidos_all(database_name)            
            faturamento = 0
            exibir_tela = ''
            endereco =''
            i=1
            for elem in row:
                endereco_raw = elem.endereco
                if isinstance(endereco_raw, (tuple, list)):
                    endereco_raw = endereco_raw[0]
                faturamento+=elem.valor_total
                endereco = endereco_raw or 'Nao informado'
                exibir_tela+= f'Nº: {i}| Estado: {elem.status}| Delivery: {elem.delivery}| Endereco: {endereco}| Valor: R$ {elem.valor_total} \n'
                i+=1
            print(f'\nPedidos \n\n{exibir_tela}')
            print(f'Faturamento R$ {faturamento}')
        
        elif q=='3':
            while True:  
                #bloco para tratamento do índice
                while True:
                    try:
                        indice = int(input('Indice do pedido (ou 0 para cancelar): '))
                        if indice == 0:
                            print('Operação cancelada.')
                            return
                        break
                    except ValueError:
                        print('ERRO: Digite um número válido (ou 0 para cancelar).')
                        continue

                #verificação de existência do pedido
                informacoes_pedido = PedidoControler.search_in_pedidos_id(database_name, indice)
                if not informacoes_pedido:
                    print(f'Pedido {indice} não encontrado. Tente outro índice.')
                    continue  

                #exibe informações do pedido encontrado
                resume = ItemControler.search_into_itens_pedidos_id(database_name, indice)
                if len(resume) > 0:
                    exibir_tela = '\n'.join([f'Tipo: {elem[2]}| Sabor: {elem[0]}| Descricao: {elem[3]}| R$ {elem[1]}|' for elem in resume])
                    print(f'\nResumo do pedido {indice}:\n{exibir_tela}\nItens: {len(resume)}\n')
                else:
                    print(f'\nPedido {indice} sem itens registrados.\n')

                pedido_data = informacoes_pedido[0]
                print(f'Status atual: {pedido_data[1]}\nEndereco: {pedido_data[3]}\nValor: R$ {pedido_data[5]}')
                
                #atualização do status de pedido
                while True:
                    try:
                        novo_status = int(input('\npreparo-1 | pronto-2 | entregue-3 (ou 0 para cancelar): '))
                        if novo_status == 0:
                            print('Atualização cancelada.')
                            break 
                        elif novo_status in [1, 2, 3]:
                            if PedidoControler.update_pedido_status_id(database_name, indice, novo_status):
                                status_map = {1: 'PREPARO', 2: 'PRONTO', 3: 'ENTREGUE'}
                                print(f'Status alterado para {status_map[novo_status]}') 
                                break 
                            else:
                                print('Falha na atualização. Tente novamente.')
                                break 
                        else:
                            print('Digite 1, 2, 3 ou 0 para cancelar.') 
                    except ValueError:
                        print('Digite apenas números.')
                        
                # Pergunta se deseja tentar com outro pedido
                while True:
                    continuar = input('\nDeseja atualizar outro pedido? (s/n): ').lower()
                    if continuar in ['s', 'n']:
                        break
                    print('ERRO: Digite apenas "s" para SIM ou "n" para NÃO')

                if continuar == 'n':
                    return  
                    
        else:
            print('Entrada inválida, retornando')
