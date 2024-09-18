print("Hello World")

api_key = "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"
openai.api_key = api_key

import openai
import os
from dotenv import load_dotenv

# Carregar a API Key do arquivo .env
load_dotenv()
openai.api_key = os.getenv("openai.api_key")

# Função para gerar resposta aleatória
def gerar_resposta():
    prompt = "Diga uma frase aleatória para o usuário"
    resposta = openai.Completion.create(
        engine="text-davinci-003",  # Motor da OpenAI
        prompt=prompt,
        max_tokens=50  # Quantidade máxima de tokens na resposta
    )
    return resposta.choices[0].text.strip()

if __name__ == "__main__":
    print("Bem-vindo ao MVP da IA!")
    while True:
        input("Aperte Enter para receber uma frase aleatória:")
        print(gerar_resposta())

