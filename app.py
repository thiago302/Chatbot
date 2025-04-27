from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

# Função que envia a mensagem para o modelo
def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append({"role": "user", "content": mensagem})
    resposta = ollama.chat(
        model='llama3',
        messages=lista_mensagens,
    )
    lista_mensagens.append({"role": "assistant", "content": resposta['message']['content']})
    return resposta['message']['content'], lista_mensagens

lista_mensagens = []

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        mensagem = request.form["mensagem"]
        resposta, _ = enviar_mensagem(mensagem, lista_mensagens)
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)
