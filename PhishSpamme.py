#!/usr/bin/python3
# -*- coding: utf-8 -*-

import smtplib, time, os, sys
import unicodedata
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


###########################
a = "\033[1;32m" # Verde
b = "\033[1;31m" # Vermelho
c = "\033[1;33m" # Amarelo
d = "\033[1;37m" # Branco
D = "\033[0;37m" # Branco
###########################

def help():
    os.system("clear")
    print('''\033[0;37m
A ferramenta PhishSpammer foi desenvolvida por Mr. Cyber, em agosto de 2018. Especificamente 
criada para quem trabalha com Websites e precise de Spammear para diversas pessoas ao mesmo 
tempo. Lembrando se utilizada a ferramenta de forma ilegal você está assumindo automaticamente 
todos os crimes cometidos, tenha responsabilidade na hora de usar. 

Antes de iniciar verifique se seu login esta com permissao para usar aplicativos menos seguros,
caso nao esteja com a permissao ativada voce deve ativa para comecar utilizar essa ferramenta
proximo passo adcione a lista de emails, depois o titulo da mensagem, e por fim a mensagem que
sera enviada e como voce quer que o usario receba, existe duas maneiras, você pode mandar em
formato padrão de forma simples ou em formato HTML (o mais recomendado), se não sabe muito de
HTML daremos alguns exemplos."


\033[1;32m<h1>\033[0;37mTitulo   \033[1;32m</h1>
\033[1;32m<p> \033[0;37mParagrafo\033[1;32m</p>
\033[1;32m<b> \033[0;37mNegrito  \033[1;32m</b>
\033[1;32m<i> \033[0;37mItalico  \033[1;32m</i>
\033[1;32m<br>\033[0;37mQuebra de linha\033[1;32m<br>
\033[1;32m<a href="site">\033[0;37mNome\033[1;32m</a>
\033[1;32m<img src="\033[0;37mSua imagem\033[1;32m"/>


\033[1;34m════━ \033[1;37mAutenticacao
\033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m 1\033[1;31m =>\033[1;33m Entre com seu email
\033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m 2\033[1;31m =>\033[1;33m Entre com sua senha
\033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m 3\033[1;31m =>\033[1;33m Sua lista de E-mails

\033[1;34m════━ \033[1;37mCorpo da mensagem
\033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m 4\033[1;31m =>\033[1;33m Titulo (Assunto)
\033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m 5\033[1;31m =>\033[1;33m Sua mensagem
\033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m 6\033[1;31m =>\033[1;33m Aguarde.

\033[1;34m════━ \033[1;37mExemplo da mensagem
\033[0;37m<p>Ola poderia visitar meu site, link abaixo</p>
<a href="https://site.com.br/">Link do site</a>
<img src="Imagem do meu site aqui"/>
    ''')


if len(sys.argv) == 2 or len(sys.argv) == 6:
   help()
   input("\033[1;33m════━\033[1;32m Precione enter para continuar \033[0;37m")
else:
   time.sleep(1)

os.system("clear")
print("""\033[0;31m
8888888b.  888      d8b          888       .d8888b.                                  888b     d888 
888   Y88b 888      Y8P          888      d88P  Y88b                                 8888b   d8888 
888    888 888                   888      Y88b.                                      88888b.d88888 
888   d88P 88888b.  888 .d8888b  88888b.   "Y888b.   88888b.   8888b.  88888b.d88b.  888Y88888P888 
8888888P"  888 "88b 888 88K      888 "88b     "Y88b. 888 "88b     "88b 888 "888 "88b 888 Y888P 888 
888        888  888 888 "Y8888b. 888  888       "888 888  888 .d888888 888  888  888 888  Y8P  888 
888        888  888 888      X88 888  888 Y88b  d88P 888 d88P 888  888 888  888  888 888   "   888 
888        888  888 888  88888P' 888  888  "Y8888P"  88888P"  "Y888888 888  888  888 888       888 
                                                     888                                           
                                                     888                                           
                                                     888                                           
\033[0;33m                          ~~~~~~~~~~~
\033[0;33m          	          (         )
\033[0;33m                           (_     _)
\033[0;33m           	             } L {
\033[0;33m            	             } C {
\033[0;33m                     (,,,,,,,| N |,,,,,,,)
\033[0;33m                    {  	                  }
\033[0;33m                     (``````|/   \|``````)
\033[0;37m                             |/ \|
\033[0;34m==============================================================
\033[0;36m[ Author » Mister Cyber  \033[0;37m    |/ \|   \033[0;36m<b>Negrito</b>          ]
\033[0;36m[ Data   » 29-agosto-2018\033[0;37m    |/ \|   \033[0;36m<br>Nova linha<br>      ]
\033[0;36m[ Canal  » Legião anonyma\033[0;37m    |/ \|   \033[0;36m<p>Paragrafo</p>        ]
\033[0;36m[ Tool   » PhishSpamme   \033[0;37m    |/ \|   \033[0;36m<a href="site">Link</a> ]
\033[0;36m[ Ajuda  » [--help] [-h] \033[0;37m    |/ \|   \033[0;36m<img src="Imagem"/>     ]
\033[0;34m==============================================================\033[0;37m
                             |/ \|
                             \/ \/
                              \ /
                               '""")


try:
   print(D+"[+] Suas Credenciais\n")
   Email = input(c+"╔═══━"+a+" Entre com seu E-mail » "+d)
   Senha = input(c+"╚═══━"+a+" Entre com sua senha  » "+d)
   print(D+"\n[+] Enviar Mensagem\n")
   Destino = input(c+"════━"+a+" Sua lista de E-mails » "+d)
   Assunto = input(c+"╔═══━"+a+" Assunto da mensagem  » "+d)
   mensage = input(c+"╚═══━"+a+" Escreva uma mensagem » "+d)
   login = unicodedata.normalize('NFKD', Destino).encode('ASCII', 'ignore')
   email_list = open(login, "r").readlines()
   print(c+"════━ "+a+"Iniciando...\n\n")
except KeyboardInterrupt:
   print(d+"\n[\033[1;37;41mVoce precionou Ctrl+C para cancelar!\033[m]")
   time.sleep(0.10)
   quit()

except FileNotFoundError:
    print(d+"\n[\033[1;37;41mNão existe tal arquivo ou diretório!\033[m]")
    time.sleep(0.10)
    quit()

msg = MIMEMultipart()
msg['From'] = Email
msg['To'] = Destino
msg['Subject'] = Assunto

body = MIMEText(mensage,'html')
msg.attach(body)

text = msg.as_string()
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
x = 1

try:
   server.login(Email, Senha)
   for para in email_list:
       login = unicodedata.normalize('NFKD', para).encode('ASCII', 'ignore').decode('ascii')
       s = server.sendmail(Email, login, text)
       print(b+"["+d+str(x)+'/'+str(len(email_list))+b+"]"+a+" Mensagem enviada com sucesso"+b+" : "+d + login)
       x += 1

except KeyboardInterrupt:
    print(d+"\n[\033[1;37;41mVoce precionou Ctrl+C para cancelar!\033[m]")
    time.sleep(0.10)
    quit()

except smtplib.SMTPNotSupportedError:
    print(d+"\n[\033[1;37;41mAutenticacao nao suportada pelo servidor!\033[m]")
    time.sleep(0.10)
    quit()

except smtplib.SMTPServerDisconnected:
    print(d+"\n[\033[1;37;41mConexão fechada inesperadamente!\033[m]")
    time.sleep(0.10)
    quit()

except smtplib.SMTPAuthenticationError:
    print(d+"\n[\033[1;37;41mUsername ou senha incorreto ou a permissao de apps menos seguro esta desativada\033[m]")
    print(D+"Verifique no site: https://myaccount.google.com/security\n")
    time.sleep(0.10)
    quit()

except smtplib.SMTPSenderRefused:
    print(d+"\n[\033[1;37;41mEndereço do remetente recusado!\033[m]")
    time.sleep(0.10)
    quit()

except smtplib.SMTPRecipientsRefused:
    print(d+"[\033[1;31;42mTodos os endereços de destinatários recusados!\033[m]")
    time.sleep(0.10)
    quit()

except OSError:
    print(d+"[\033[1;31;42mPermitir aplicativos menos seguros usarem sua conta!\033[m]")
    print(D+"https://myaccount.google.com/security")
    time.sleep(0.10)
    quit()

except  smtplib.SMTPConnectError:
    print(d+"\n[\033[1;37;41mOcorreu um erro durante a conexao com o servidor!\033[m]")
    time.sleep(0.10)
    quit()

except UnicodeEncodeError as erro:
    print(d+"\n[\033[1;37;41mErro de Codificação, os e-mails nao devem conter acentuacao grafica!\033[m]")
    time.sleep(0.10)
    quit()

except smtplib.SMTPDataError:
   print(d+"\n[\033[1;37;41mO servidor SMTP recusou-se a aceitar os dados da mensagem.\033[m]")
   time.sleep(0.10)
   quit()

print(d+"\n["+a+"ENVIOS FINALIZADO! "+d+"]")
time.sleep(0.10)
quit()

