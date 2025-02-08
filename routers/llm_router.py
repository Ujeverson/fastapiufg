from fastapi import APIRouter
from utils import obter_logger_e_configuracao, executar_prompt


logger = obter_logger_e_configuracao()

router = APIRouter()


@router.post(
    "/gerar_historia", 
    summary="Gera uma história sobre o tema informado por parâmetro",
    description="Gera uma história em português brasileiro sobre um tema específico usando a API Groq.",
    )
def gerar_historia(tema: str):
    logger.info(f"Tema informado: {tema}")    
    
    historia = executar_prompt(tema)        
    logger.info(f"História gerada: {historia}")
    
    return {"historia": historia}