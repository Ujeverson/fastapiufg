from enum import Enum
from pydantic import BaseModel


class NomeGrupo(str, Enum):
    """
    Enumeração que representa os nomes dos grupos.

    Atributos:
        operacoes (str): Retorna o nome do grupo de operações matemáticas simples.
        teste (str): Retorna o nome do grupo de teste.
    """
    operacoes = "Operações matemáticas simples"
    teste = "Teste"


class TipoOperacao(str, Enum):
    """
    Enumeração que representa os tipos de operações matemáticas.

    Atributos:
        soma (str): Representa a operação de soma.
        subtracao (str): Representa a operação de subtração.
        multiplicacao (str): Representa a operação de multiplicação.
        divisao (str): Representa a operação de divisão.
    """
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"


class Numero(BaseModel):
    """
    Classe Numero que herda de BaseModel.

    Atributos:
        numero1 (int): Primeiro número inteiro.
        numero2 (int): Segundo número inteiro.
    """
    numero1: int
    numero2: int


class Resultado(BaseModel):
    """
    Classe que representa o resultado de uma operação.

    Atributos:
        resultado (int): O valor do resultado.
    """
    resultado: int
