from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/teste")
def hello_world():
    return {
        "message": "Hello, World!"
        }

# Criando um endpoint para receber dois números e retornar a soma
@app.post("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {
        "resultado": total
    }

# Formato2 Passando o número 1 e 2 no corpo da requisição
@app.post("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}

# Formato3 Passando o número 1 e 2 no corpo da requisição
class Numeros(BaseModel):
    numero1: int
    numero2: int
    numero3: int = 2

@app.post("/soma_formato3")
def soma_formato3(numero: Numeros):
    total = numero.numero1 + numero.numero2 + numero.numero3
    return {"resultado": total}
