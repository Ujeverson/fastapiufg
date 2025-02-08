# fastapiufg
Repositório para a disciplina de Construção de APIs para Inteligência Artificial da especialização em agentes inteligentes UFG

### ORIENTAÇÕES PARA A EXECUÇÃO DO PROJETO
- Crie um ambiente virtual: `python -m venv venv`
- Ative o ambiente virtual (no Windows): `venv\Scripts\activate`
- Ative o ambiente virtual (no Linux): `source venv/bin/activate`
- Instale as bibliotecas: `pip install -r requirements.txt`
- Copie o arquivo `.env.sample` para `.env` e preencha as variáveis de ambiente
- Executar a API em ambiente de desenvolvimento: `fastapi dev main.py`
- Executar a API em ambiente de produção: `fastapi run main.py`


## Desenvolva um endpoint que deverá:
     - Receber por parâmetro um “tema” de uma história
     - Montar um prompt para que seja gerada uma história com base no tema informado pelo usuário
     - Execute o prompt na OpenAI ou Groq
     - Retorne a resposta para o usuário
### Postman
### Github

