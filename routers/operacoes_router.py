
from fastapi import HTTPException, status, APIRouter
from models import NomeGrupo, Resultado, Numero, TipoOperacao
from utils import obter_logger_e_configuracao


logger = obter_logger_e_configuracao()

router = APIRouter()


@router.get(
    "/teste",
    summary="Retorna mensagem de teste",
    description="Retorna uma mensagem de exemplo para testar e verificar se deu certo",
    tags=[NomeGrupo.teste],
)
def hello_world():
    return {"mensagem": "Deu certo"}


# Criando um endpoint para receber dois números e retornar a soma
@router.post(
    "/soma/{numero1}/{numero2}",
    tags=[NomeGrupo.operacoes],
    summary="Recebe dois números na url e retorna a soma",)
def soma(numero1: int, numero2: int):
    logger.info(f"Requisição recebida, parâmetros numero1={numero1}, numero2={numero2}")

    if numero1 < 0 or numero2 < 0:
        logger.error("Não é permitido números negativos")
        raise HTTPException(status_code=400, detail="Não é permitido números negativos")

    total = numero1 + numero2

    if total < 0:
        logger.error("Resultado negativo")
        raise HTTPException(status_code=400, detail="Resultado negativo")

    logger.info(f"Requisição processada com sucesso. Resultado: {total}")

    return {"resultado": total, "warning": "Esta versão será descontinuada em 30 dias"}


# Formato 2: recebendo os números no corpor da requisição
@router.post(
    "/soma/v2", 
    tags=[NomeGrupo.operacoes],
    summary="Recebe dois números no corpo da requisição e retorna a soma",
    response_model=Resultado,
    )
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    logger.info(f"Resultado da operação: {total}")
    return Resultado(resultado=total)


@router.post(
    "/soma/v3",
    response_model=Resultado,
    tags=[NomeGrupo.operacoes],
    status_code=status.HTTP_200_OK,
    summary="Recebe dois números no corpo da requisição e retorna a soma",
)
def soma_formato3(numero: Numero):
    total = numero.numero1 + numero.numero2
    logger.info(f"Resultado da operação: {total}")
    return {"resultado": total}


@router.post(
    "/divisao/{numero1}/{numero2}", 
    tags=[NomeGrupo.operacoes],
    summary="Recebe dois números na url e retorna a divisão",
    )
def divisao(numero1: int, numero2: int):
    if numero2 == 0:
        raise HTTPException(status_code=400, detail="Não é permitido divisão por zero")

    total = numero1 / numero2

    logger.info(f"Resultado da operação: {total}")
    return {"resultado": total}


@router.post(
    "/operacao", 
    tags=[NomeGrupo.operacoes],
    summary="Recebe dois números e o tipo de operação e retorna o resultado",
    )
def operacao(numero: Numero, tipo: TipoOperacao):
    if tipo == TipoOperacao.soma:
        total = numero.numero1 + numero.numero2

    elif tipo == TipoOperacao.subtracao:
        total = numero.numero1 - numero.numero2

    elif tipo == TipoOperacao.multiplicacao:
        total = numero.numero1 * numero.numero2

    elif tipo == TipoOperacao.divisao:
        total = numero.numero1 / numero.numero2
    
    logger.info(f"Resultado da operação: {total}")
    return {"resultado": total}