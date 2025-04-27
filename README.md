# Chatbot 

Este é um simples projeto de **Chatbot** desenvolvido com **Python**, utilizando o framework **Flask** para a criação da interface web e a API do **Ollama** para o processamento das mensagens. O chatbot responde a perguntas e mantém o contexto da conversa.

## Tecnologias Utilizadas

- **Python** 3.x
- **Flask**: Framework web para desenvolvimento da interface
- **Ollama**: Modelo de linguagem utilizado para processamento de linguagem natural
- **HTML**: Para a estrutura da página web
- **CSS**: Para o estilo da página web

## Funcionalidades

- Interação simples de chatbot com o modelo Llama3.
- Respostas dinâmicas e manutenção do contexto da conversa.
- Interface web simples criada com o Flask.
- O modelo Llama3 é executado localmente com o Ollama.

## Como Rodar o Projeto

### 1. Instalação de Dependências

Certifique-se de ter o **Python** instalado. Em seguida, crie um ambiente virtual para o projeto e instale as dependências:

```bash
# Criação do ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate
# No Linux/macOS
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt
