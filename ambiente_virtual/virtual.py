from fastapi import FastAPI

# 1. Instanciamos a aplicação
app = FastAPI()

# 2. Criamos uma "Rota" (o endereço que a pessoa vai acessar)
@app.get("/")
def home():
    return {"mensagem": "Minha primeira API está online!"}

# 3. Uma rota com parâmetro (ex: /usuario/kaua)
@app.get("/saudar/{nome}")
def saudar_usuario(nome: str):
    return {"saudacao": f"Olá, {nome}! Você já é um dev de APIs."}
