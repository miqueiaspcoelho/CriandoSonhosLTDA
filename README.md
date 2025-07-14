
# CriandoSonhosLTDA - Pizza Mais "Seus sonhos têm formato e borda" - (Versão com Manutenções Aplicadas)

Este repositório é uma versão derivada (fork) do sistema original Pizza Mais, desenvolvido pela CriandoSonhosLTDA.

Tem como objetivo aplicar manutenções corretivas e evolutivas com base em interações reais de clientes, documentadas na tarefa do processo seletivo.


## Funcionalidades

- criação de pedidos
- gerenciamento de pedidos
- controle de faturamento

## 📋 Tabela de Manutenções – Sistema "Pizza Mais"  
### Necessário preencher a tabela

| Nº | Descrição do Problema ou Solicitação                                                                 | Manutenção | Ação Esperada                                                                                                   |
|----|-------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------|
| 1  |                                                                                                       |            | Melhorar o layout do menu principal para torná-lo mais claro, organizado e visualmente acessível.               |
| 2  | Entrada para confirmar o cadastro de novo pedido não funciona em alguns casos.                       |            |                                                                                                                  |
| 3  | Ao adicionar novo item ao pedido, a confirmação falha ocasionalmente.                                | Corretiva  | Revisar a lógica de confirmação de novo item e corrigir falhas de reconhecimento ou fluxo.                      |
| 4  |                                                                                                       |            |                                                                                                                  |
| 5  | O sistema não apresenta nenhuma resposta na opção inicial: Cadastrar pedido (y-Sim, n-Nao).           |            | Adicionar validação e exibir mensagens informando o erro ao usuário.                                            |
| 6  | Ao tentar atualizar o status de um pedido, nenhuma ação ocorre (sistema ignora o comando).           | Corretiva  |                                                                                                                  |
| 7  | Cliente solicita a criação de uma nova tela para cadastrar novos itens no menu do restaurante.       |            | Implementar uma view de cadastro de itens, integrando com os controllers e models já existentes.               |




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


