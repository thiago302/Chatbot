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

O arquivo requirements.txt deve conter:

ini
Copiar
Editar
Flask==2.1.2
ollama==1.0.0
2. Configuração do Ollama
Para usar a API do Ollama, é necessário ter o Ollama instalado em sua máquina e o modelo Llama3 executando. Para isso, siga os passos:

Baixe e instale o Ollama: Ollama Website.

Execute o modelo Llama3 com o comando:

bash
Copiar
Editar
ollama run llama3
Este comando inicia o modelo Llama3 localmente. O servidor do Ollama precisa estar em execução enquanto o chatbot estiver ativo.

3. Executando o Servidor Flask
Após configurar o Ollama, execute o servidor Flask com o seguinte comando:

bash
Copiar
Editar
python app.py
O servidor estará disponível em http://127.0.0.1:5000.

4. Acessando o Chatbot
Abra o navegador e acesse http://127.0.0.1:5000 para interagir com o chatbot.

5. Finalizando
Para finalizar o servidor, pressione Ctrl + C no terminal.

Estrutura do Projeto
kotlin
Copiar
Editar
chatbot/
│
├── app.py             # Código principal do servidor Flask
├── chatboot2.py       # Lógica do chatbot com Ollama
├── templates/
│   └── index.html     # Página HTML da interface web
└── requirements.txt   # Dependências do projeto
Descrição dos Arquivos:
app.py: Código principal para rodar o servidor Flask e servir a página da web.

chatboot2.py: Contém a lógica de interação com o modelo de linguagem Ollama.

templates/index.html: Página HTML simples com um campo para enviar mensagens para o chatbot.

requirements.txt: Arquivo contendo as dependências do projeto.
