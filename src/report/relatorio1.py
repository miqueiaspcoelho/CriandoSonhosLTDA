from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class PDF:
    """
    Classe responsável pela geração de relatórios em PDF com visual aprimorado.
    """

    @staticmethod
    def gerar_pdf(nome_arquivo: str, pedidos: list, faturamento_total: float) -> bool:
        """
        Gera um arquivo PDF com os pedidos e o faturamento total.

        :param nome_arquivo: Caminho e nome do arquivo PDF.
        :param pedidos: Lista de dicionários com pedidos e seus itens.
        :param faturamento_total: Soma de todos os valores dos pedidos.
        :return: True se o PDF for salvo com sucesso, False caso contrário.
        """
        canva = canvas.Canvas(nome_arquivo, pagesize=A4)
        largura, altura = A4

        x = 30
        y = altura - 50

        # Título
        canva.setFont("Helvetica-Bold", 16)
        canva.drawCentredString(largura/2, y, "Pizza Mais - Relatório Geral")

        # Linha horizontal abaixo do título
        y -= 10
        canva.setLineWidth(1)
        canva.line(x, y, largura - 30, y)

        y -= 30
        canva.setFont("Helvetica", 11)

        for pedido in pedidos:
            y -= 15 #espaçamento superior 
            margem_direita = largura - 40 
            # Calcular altura da caixa de pedido dinamicamente
            # Cada pedido tem:
            #   20 para linha do título do pedido
            #   15 para "Itens:" cabeçalho
            #   27 para cada item (12 para o nome, 15 para a descrição)
            #   10 para espaçamento extra após os itens
            itens_validos = [item for item in pedido["itens"] if item[0] is not None]
            altura_caixa = 20 + 15 + (len(itens_validos) * 27) + 20

            # Quebra de página se necessário
            if y - altura_caixa < 50:
                canva.showPage()
                y = altura - 50

            # Caixa visual para pedido
            canva.setStrokeColor(colors.grey)
            canva.setLineWidth(0.3)
            canva.rect(x - 5, y + 15, largura - 60, -altura_caixa, stroke=1, fill=0)

            # Conteúdo do pedido
            # canva.setFont("Helvetica-Bold", 12)
            # canva.drawString(x, y, f"Pedido #{pedido['id']} - Data: {pedido['data']} - Total: R$ {pedido['valor']:.2f}")
            # y -= 20
            # Cabeçalho do pedido: nome do pedido à esquerda, data à direita
            canva.setFont("Helvetica-Bold", 12)
            canva.drawString(x, y, f"Pedido #{pedido['id']}")
            canva.drawRightString(margem_direita, y, f"Data: {pedido['data']}")

            y -= 15
            canva.setFont("Helvetica-Bold", 10)
            canva.drawString(x + 10, y, "Itens:")
            y -= 15
            
            canva.setFont("Helvetica", 10)
            for nome, preco, tipo, descricao in itens_validos:
                canva.drawString(x + 20, y, f"- {nome} ({tipo}) - R$ {preco:.2f}")
                y -= 12
                canva.setFillColor(colors.grey)
                canva.drawString(x + 30, y, f"{descricao}")
                canva.setFillColor(colors.black)
                y -= 15
            # Valor total abaixo dos itens, alinhado à direita
            canva.setFont("Helvetica-Bold", 11)
            canva.drawRightString(margem_direita, y, f"Total: R$ {pedido['valor']:.2f}")


            y -= 20 # espaço entre pedidos

        # Linha separadora final
        if y <= 60:
            canva.showPage()
            y = altura - 60

        canva.setLineWidth(1)
        canva.setStrokeColor(colors.black)
        canva.line(x, y, largura - 30, y)
        y -= 25

        # Faturamento final
        canva.setFont("Helvetica-Bold", 12)
        canva.drawCentredString(largura / 2, y, f"Faturamento Total: R$ {faturamento_total:.2f}")

        try:
            canva.save()
            return True
        except OSError as e:
            print(e)
            return False
