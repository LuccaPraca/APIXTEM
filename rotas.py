from fastapi import FastAPI, File, UploadFile, Request
from typing import Optional
import requests
import os
import uvicorn
from smtp import enviar_emails_arquivo
from comandos import enviarlogAPIglobal
app = FastAPI()
def salvar_arquivo(upload_file: UploadFile) -> str:
    diretorio = "./"
    with open(os.path.join(diretorio, upload_file.filename), "wb") as arquivo_salvo:
        arquivo_salvo.write(upload_file.file.read())
    return diretorio + upload_file.filename
@app.post("/{user}/apismtp/upload/{nomedoarquivo}")
async def upload(request: Request,nomedoarquivo: str, user: str, url: str, file: UploadFile = File(...)):
    client_host = request.client.host
    enviarlogAPIglobal("/apismtp/upload", client_host, user)
    if user == "dc":
        response = requests.get(url)
        if response.status_code == 200:
            conteudo_arquivo = response.content
            nome_arquivo = f"{nomedoarquivo}.txt"
            with open(nome_arquivo, "wb") as arquivo_salvo:
                arquivo_salvo.write(conteudo_arquivo)
            diretorio_arquivo = nome_arquivo
        else:
            diretorio_arquivo = "Falha ao baixar o arquivo"
        return {"diretorio_arquivo": diretorio_arquivo}
    elif user == "elpanda":
        response = requests.get(url)
        if response.status_code == 200:
            conteudo_arquivo = response.content
            nome_arquivo = f"{nomedoarquivo}.txt"
            with open(nome_arquivo, "wb") as arquivo_salvo:
                arquivo_salvo.write(conteudo_arquivo)
            diretorio_arquivo = nome_arquivo
        else:
            diretorio_arquivo = "Falha ao baixar o arquivo"
        return {"diretorio_arquivo": diretorio_arquivo}
    else:
        return {"USUARIO NAO IDENTIFICADO"}
@app.post("/{user}/apismtp/iniciarchk/{nome}/{assunto}/{mensagem}")
async def iniciarteste(nome: str,assunto: str,mensagem: str,request: Request,user: str):
    client_host = request.client.host
    enviarlogAPIglobal("/apismtp/upload", client_host, user)
    if user == "dc":
        client_host = request.client.host
        resultado = enviar_emails_arquivo(nome, assunto, mensagem)
        return resultado
    elif user == "elpanda":
        client_host = request.client.host
        resultado = enviar_emails_arquivo(nome, assunto, mensagem,client_host,user)
        return resultado
    else:
        return {"USUARIO NAO IDENTIFICADO"}


