import logging
from fastapi import FastAPI, status, HTTPException
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


API_TOKEN = int(os.getenv("API_TOKEN"))


def obter_logger_e_configuracao():
    """
    Configura o logger padrão para o nível de informação e formato especificado.

    Retorna:
        logging.Logger: Um objeto de logger com as configurações padrões.
    """
    logging.basicConfig(
        level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s"
    )
    logger = logging.getLogger("fastapi")
    return logger


def commom_verificacao_api_token(api_token: int):
    """
    Verifica se o token da API fornecido é válido.

    Args:
        api_token (int): O token da API a ser verificado.

    Raises:
        HTTPException: Se o token da API for inválido, uma exceção HTTP 401 é levantada com a mensagem "Token inválido".
    """
    if api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")


def executar_prompt(tema: str):
    """
    Gera uma história em português brasileiro sobre um tema específico usando a API Groq.
    Args:
        tema (str): O tema sobre o qual a história será escrita.
    Returns:
        str: O conteúdo da história gerada pela API Groq.
    """
    prompt = f"Escreva uma história em pt-br sobre o {tema}"

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content
