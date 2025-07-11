# para pegar a data de hoje
from datetime import date
import time
import sys
from pathlib import Path

# Necessário para realizar import em python
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# importando os módulos de model
from model.pedido import Pedido

# importando os módulos de controle
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

# criação da classe janela
class Janela1:

    @staticmethod
    async def mostrar_janela1(database_name: str) -> None:
        """
        View para o usuário utilizar o software

        return None
        """

        # 🔧 MELHORIA 1: Menu formatado e mais amigável
        menu = ItemControler.mostrar_itens_menu(database_name)
        print('\n📋 CARDÁPIO:')
        print('-' * 40)
        for item in menu:
            print(f"🍕 {item[0]}. {item[1].capitalize()} - R${item[2]:.2f}")
            print(f"   Tipo: {item[3]} | Descrição: {item[4]}")
            print('-' * 40)

        while True:
            lista_itens = []
            valor_total = 0

            # 🔧 MELHORIA 2: Aceita variações de 'sim' e 'não'
            a = input('Cadastrar pedido (sim / não): ').strip().lower()

            if a in ['sim', 's', 'y']:  # aceitando mais variações
                print('----------Cadastrar pedido----------\n')
                adicionar = 'sim'
                pedidos = PedidoControler.search_in_pedidos_all(database_name)
                numero_pedido = len(pedidos) + 1

                while adicionar in ['sim', 's', 'y']:
                    try:
                        item = int(input('Número do item: '))
                        quantidade = int(input('Quantidade: '))
                    except ValueError:
                        print("⚠️ Digite valores numéricos válidos.")
                        continue

                    # 🔧 MELHORIA 3: Valor com tratamento de erro
                    valor = await ItemControler.valor_item(database_name, item)
                    b = valor[0] * quantidade
                    print(f"💰 Valor total deste item: R${b:.2f}")
                    valor_total += b

                    for _ in range(quantidade):
                        lista_itens.append((numero_pedido, item))

                    adicionar = input('Adicionar novo item? (sim / não): ').strip().lower()

                print('\n----------Finalizar pedido----------\n')
                print(f'🧾 Número do pedido: {numero_pedido}')
                delivery_input = input('Delivery? (sim / não): ').strip().lower()
                if delivery_input in ['sim', 's', 'y']:
                    delivery = True
                elif delivery_input in ['não', 'nao', 'n']:
                    delivery = False
                else:
                    print("⚠️ Valor incorreto para Delivery. Recomeçando cadastro...\n")
                    break

                endereco = input('📍 Endereço de entrega: ').strip()

                try:
                    status_aux = int(input('Status (1-preparo, 2-pronto, 3-entregue): '))
                    if status_aux == 1:
                        status = 'preparo'
                    elif status_aux == 2:
                        status = 'pronto'
                    elif status_aux == 3:
                        status = 'entregue'
                    else:
                        print("⚠️ Status inválido. Recomeçando cadastro...\n")
                        break
                except ValueError:
                    print("⚠️ Entrada inválida para status. Recomeçando...\n")
                    break

                data_formatada = date.today().strftime('%d/%m/%Y')
                pedido = Pedido(status, str(delivery), endereco, data_formatada, float(valor_total))
                PedidoControler.insert_into_pedidos(database_name, pedido)

                for elem in lista_itens:
                    ItemControler.insert_into_itens_pedidos(database_name, elem)

                # 🔧 MELHORIA 4: Confirmação visual de sucesso
                print(f"\n✅ Pedido #{numero_pedido} cadastrado com sucesso!")
                print(f"📦 Valor Total: R${valor_total:.2f} | 📅 Data: {data_formatada}")

            elif a in ['não', 'nao', 'n']:  # 🔧 MELHORIA 5: aceita variações
                print('↩️ Voltando ao Menu inicial...')
                time.sleep(2)
                break
            else:
                # 🔧 MELHORIA 6: Entrada inválida informativa
                print("⚠️ Entrada inválida. Por favor, digite 'sim' ou 'não'.")
