import openai
import time

# Definindo a chave da API
api_key = "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"
openai.api_key = api_key

# Função para enviar a conversa e receber a resposta
def enviar_conversa(mensagem, lista_mensagens=[]):
    lista_mensagens.append({"role": "user", "content": mensagem})

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=lista_mensagens,
        )
        return resposta.choices[0].message['content']
    
    except openai.error.RateLimitError:
        print("Erro: Você excedeu o limite de uso da API. Por favor, verifique sua cota e tente novamente mais tarde.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

# Inicializando a lista de mensagens e o loop de interação
lista_mensagens = []
while True:
    texto = input("Digite sua mensagem: ")

    if texto.lower() == "sair":
        break
    else:
        resposta = enviar_conversa(texto, lista_mensagens)
        if resposta:
            lista_mensagens.append({"role": "assistant", "content": resposta})
            print("Chatbot:", resposta)

from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="Gerador de Prompts.xlsx", 
  model="gpt-4o-mini-2024-07-18"
)