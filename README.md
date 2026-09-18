# Sistema de Gerenciamento de Estacionamento

Um sistema simples e interativo de linha de comando (CLI) desenvolvido em Python para gerenciar vagas de um estacionamento. O sistema permite cadastrar veículos, controlar a ocupação das vagas e salva os dados automaticamente para que não sejam perdidos ao fechar o programa.

## 🚀 Funcionalidades

- **Cadastro de Veículos:** Associa a placa do carro ao nome do dono.
- **Controle de Vagas:** Permite ocupar e desocupar vagas com atualização visual em tempo real.
- **Listagem:** Exibe um painel com o status de todas as vagas (Livre/Ocupada) e uma lista completa de clientes cadastrados.
- **Persistência de Dados:** Salva todas as informações em um arquivo `JSON` ao encerrar o sistema e carrega automaticamente na próxima execução.

## 📂 Estrutura dos Arquivos

O projeto foi organizado para separar a interface (menus) da regra de negócio (lógica do estacionamento):

* **`main.py`**
  É o arquivo principal do programa. Ele gerencia a interface do usuário, imprime os menus na tela, captura as opções digitadas e chama as funções correspondentes.
  
* **`estacionamento.py`**
  Contém a classe `Estacionamento` e suas funções utilitárias. Aqui ficam todas as regras do sistema, como checar se uma vaga já está ocupada, se uma placa já existe, além dos métodos para ler e salvar o arquivo JSON.
  
* **`dados_estacionamento.json`** *(Gerado automaticamente)*
  Arquivo de banco de dados local. Ele é criado na primeira vez que você sai do sistema usando a opção "0" e armazena o estado atual das vagas e cadastros.

## 💻 Como executar o projeto

### Pré-requisitos
Tudo o que você precisa é ter o **Python 3** instalado em sua máquina. Nenhuma biblioteca externa é necessária, pois o código utiliza apenas bibliotecas nativas do Python (`os`, `json`, `time`).

### Passo a passo

1. Abra o terminal (no Ubuntu/Linux) ou Prompt de Comando (no Windows).
2. Navegue até a pasta onde os arquivos `main.py` e `estacionamento.py` estão salvos.
3. Execute o comando abaixo para iniciar o sistema:

```bash
python3 main.py
