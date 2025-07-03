#necessário para importar arquivos de outras pastas
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#responsável por gerar o pdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

#import dos controladores
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

class RelatorioControler:
    """
    Controlador responsável por preparar os dados utilizados na geração de relatórios.
    """

    @staticmethod
    def preparar_dados_relatorio(database_name: str) -> dict:
        """
        Coleta, organiza e retorna os dados necessários para o relatório em PDF.

        :param database_name: Nome do banco de dados a ser utilizado.
        :type database_name: str
        :return: Um dicionário contendo a lista de pedidos com detalhes dos itens e o faturamento total.
        :rtype: dict

        Estrutura do retorno:
        {
            "pedidos": [
                {
                    "id": int,
                    "data": str,
                    "valor": float,
                    "itens": list  # Lista de tuplas ou listas com detalhes do item
                },
                ...
            ],
            "faturamento_total": float
        }
        """
        id_pedidos = PedidoControler.get_id_all(database_name) #criado para evitar modificar o model pedido.py
        pedidos = PedidoControler.search_in_pedidos_all(database_name)
        dados_relatorio = []
        faturamento_total = 0
        for id_pedido, pedido in zip(id_pedidos, pedidos):
            itens_pedido = ItemControler.search_into_itens_pedidos_id(database_name, id_pedido)
            itens_detalhados = []
            for item in itens_pedido:
                itens_detalhados.append(item)
            dados_relatorio.append({
                "id": id_pedido,
                "data": pedido.date,
                "valor": pedido.valor_total,
                "itens": itens_detalhados
            })
            faturamento_total += pedido.valor_total
        # print(dados_relatorio)
        # print(faturamento_total)
        return {
            "pedidos": dados_relatorio,
            "faturamento_total": faturamento_total
        }