import ollama

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    resposta = ollama.chat(
        model='llama3',
        messages=lista_mensagens,
    )
    # Adiciona a resposta no histórico, no formato certo!
    lista_mensagens.append(
        {"role": "assistant", "content": resposta['message']['content']}
    )
    return resposta['message']['content']

lista_mensagens = []

while True:
    texto = input("Escreva aqui sua mensagem: ")

    if texto.lower() == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        print("Chatbot:", resposta)

