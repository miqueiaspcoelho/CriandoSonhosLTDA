
# CriandoSonhosLTDA - Pizza Mais "Seus sonhos têm formato e borda" - (Versão com Manutenções Aplicadas)

Este repositório é uma versão derivada (fork) do sistema original Pizza Mais, desenvolvido pela CriandoSonhosLTDA.

Tem como objetivo aplicar manutenções corretivas e evolutivas com base em interações reais de clientes, documentadas na tarefa do processo seletivo.


## Funcionalidades

- criação de pedidos
- gerenciamento de pedidos
- controle de faturamento

## Novas Funcionalidades e Correções Aplicadas

Nº	Tipo de Manutenção	Descrição
1	    Corretiva	        Corrigido o problema de confirmação de pedido que não funcionava corretamente mesmo com entrada válida (Sim).
2	    Corretiva	        Ajustado o fluxo de adição de novos itens ao pedido (evitava duplicidade de ações sem resposta).
3	    Corretiva	        Corrigida falha na atualização de status de pedidos (sistema ignorava o comando).
4	    Evolutiva	        Adicionada mensagem de erro para entradas inválidas durante a confirmação do pedido.
5	    Evolutiva	        Criada nova tela para cadastro de itens no cardápio diretamente pelo sistema.
6	    Evolutiva	        Melhorado o layout do menu principal de cadastro de pedido, deixando-o mais intuitivo.


## Instalação

Após instalação do interpretador python em conjunto com o gerenciador de pacotes pip: [Download Python.](https://www.python.org/downloads/release/python-3105/) Execute o comando abaixo via terminal.
```bash
  pip install reportlab
```
Biblioteca responsável por gerar pdfs

## Executando
Para executar o software, vá até sua IDE padrão (vs code por exemplo), navegue até a pasta do projeto e em seguida execute o seguinte comando
```bash
  cd src
  python app.py
```
Pressione enter e irá aparecer o terminal dentro da IDE rodando o software
## Stack utilizada

**Back-end:** Python, SQLite

**Front-end** Python (terminal)


## Tarefa

Este projeto é parte do processo avaliativo da CriandoSonhosLTDA com prazo de entrega até 15/07/2025.

Este repositório foi modificado para fins de análise técnica e demonstração de capacidade de manutenção e evolução de software.


## Créditos
Baseado no repositório oficial da CriandoSonhosLTDA.
Desenvolvido e mantido por Rafael Freitas, Jonathas Oliveira, Gabriel Silva e Isabel Araújo para fins de avaliação técnica.

## Links importantes:

[Acesse o documento detalhado aqui.](https://docs.google.com/document/d/1ko1jYclh1JraTPVI6uLXApfpHNh2PedjnyXawAxyvYQ/edit?usp=sharing)

[Acesse o caderno virtual Notion com teoria.](https://sleepy-bolt-bee.notion.site/Manuten-o-de-Software-Uma-abordagem-te-rica-e-pr-tica-151674186cac8073bcecff137ef65151)


