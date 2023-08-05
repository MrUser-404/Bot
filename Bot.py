import os,time,json,sys,hashlib,subprocess
from concurrent.futures import ThreadPoolExecutor as tpe
try:
	import requests
except ImportError:
	os.system("pip install requests")

B='\033[1;97m'
S='\033[0m'
R='\033[1;91m'
V='\033[1;92m'
C='\033[36m'
v='\033[7;92m'
r='\033[7;91m'
c='\033[7;96m'
J='\033[1;33m'
f_coms=[]
coments=[]
i=0
Ok=[]
No=[]
user=[]
tar_name=[]
thread_ok=0
thread_no=0
me=[]

limite=[]
logo=f'''
{B} ______     ______     ______  
/\  == \   /\  __ \   /\__  _\ 
\ \  __<   \ \ \/\ \  \/_/\ \/ 
 \ \_____\  \ \_____\    \ \_\ 
  \/_____/   \/_____/     \/_/ {J}By MrUser{B}
=======================================
Tool name: Bot
Tool-Info: Auto Comment Fb
Version: {V}V4.0{S}
{B}Github: github.com/MrUser-404
======================================={S}'''


def log():
	os.system("rm -rf tool/result.txt")
	os.system("clear")
	print(logo)
	print("\033[7;96mLogin option\033[0m")
	print(f"{B}[{R}1{B}]Login num/pwd{S}")
	print(f"{B}[{R}2{B}]Token")
	print()
	option=input(f"{B}[{R}?{B}]Input choice: ")
	if str(option)=="1":
		login()
	if str(option)=="2":
		os.system("clear")
		print(logo)
		print()
		token=input(f"{B}[{V}•{B}]Token: ")
		if "EAAAAU" in token:
			rq1=requests.get(f"https://graph.facebook.com/me?fields=name&access_token={token}")
			rp1=json.loads(rq1.text)
			if 'name' in rp1:
				name=rp1['name']
				s_tok=open("tool/Token.txt",'w')
				s_tok.write(token)
				s_tok.close()
				os.system("clear")
				print(logo)
				k=(f"{B}       Hello: {J}{name}{S}\n{B}======================================={S}")
				for lettre in k:
					print(lettre,end='',flush=True)
					time.sleep(0.1)
				t_user=input(f"\n{B}[{V}•{B}]Target ID: ")
				if '1000' in t_user:
					user.append(t_user)
					os.system("clear")
					print(logo)
					dump()
				else:
					os.system("clear")
					print(f"{r}Wrong ID, please try again\033[0m")
					time.sleep(2)
					os.system("clear")
					print(logo)
					for lettre in k:
						print(lettre,end='',flush=True)
						time.sleep(0.1)
						t_user=input(f"{B}[{V}•{B}]Target ID: ")
						if '1000' in t_user:
							user.append(t_user)
							os.system("clear")
							print(logo)
							dump()
						else:
							os.system("clear")
							print(f"{r}Wrong ID *2{S}")
							time.sleep(2)
							os.system("clear")
							print(f"{r}Good Bye{S}")
							exit()
		else:
			mot=(f"{r}Invalid Token{S}")
			os.system("clear")
			for lettre in mot:
				print(lettre,end='',flush=True)
				time.sleep(0.1)
			log()
			
			
def login():
		os.system("clear")
		print(logo)
		print(f"{c}Login with mail & pwd{S}")
		num=input(f"{B}[{R}•{B}]Email or ID: ")
		mdp=input(f"{B}[{R}•{B}]Password: ")
		API_SECRET=("62f8ce9f74b12f84c123cc23437a4a32")
		data={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":num,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":mdp,"return_ssl_resources":"0","v":"1.0"}
		sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+num+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+mdp+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
		x=hashlib.new('md5')
		x.update(sig)
		data.update({'sig':x.hexdigest()})
		try:
			rq=requests.get("https://graph.facebook.com/restserver.php",data)
			rp=json.loads(rq.text)
			if 'access_token' in rp:
				token=rp['access_token']
				s_tok=open("tool/Token.txt",'w')
				s_tok.write(token)
				s_tok.close()
				word=(f"{v}Login Success{S}")
				os.system("clear")
				for f in word:
					print(f,end='',flush=True)
					time.sleep(0.1)
				os.system("clear")
				print(logo)
				rq2=requests.get(f"https://graph.facebook.com/me?fields=name&access_token={token}")
				rp2=json.loads(rq2.text)
				if 'name' in rp2:
					name=rp2['name']
					s=(f"{B}       Hello: {J}{name}{S}\n{B}======================================={S}")
					for g in s:
						print(g,end='',flush=True)
						time.sleep(0.1)
				print()
				t_user=input(f"\n{B}[{V}•{B}]Target ID: ")
				if '1000' in t_user:
					user.append(t_user)
					os.system("clear")
					print(logo)
					dump()
				else:
					os.system("clear")
					print(f"{r}Wrong ID,please try again\033[0m")
					time.sleep(2)
					os.system("clear")
					print(logo)
					t_user=input(f"{B}[{V}•{B}]Target ID: ")
					if '1000' in t_user:
						user.append(t_user)
						os.system("clear")
						print(logo)
						dump()
					else:
						os.system("clear")
						print(f"{r}Wrong ID *2{S}")
						time.sleep(2)
						os.system("clear")
						p=(f"{r}Good Bye{S}")
						for lettre in p:
							print(lettre,end='',flush=True)
							time.sleep(0.1)
							exit()
			else:
					os.system("clear")
					if 'User must verify their account on www.facebook.com' in rp['error_msg']:
						print(f"{r}Account has been Checkpoint or Blocked\033[0m")
						time.sleep(2)
						os.system("clear")
						login()
					if 'Invalid username or password (401)' in rp['error_msg']:
						os.system("clear")
						print(f"{r}Invalid Username or Password{S}")
						time.sleep(2)
						login()
					
		except KeyError:
					os.system("clear")
					print(f"{r}Account has been blocked or checkpoint or Incorrect Number or Pwd{S}")
					time.sleep(3)
					log()
		except requests.exceptions.ConnectionError:
					os.system("clear")
					print(f"{r}No Internet Connection{S}")
					time.sleep(2)
					log()
					
		
		
def dump():
	try:
		token=open("tool/Token.txt",'r').read()
	except IOError:
		os.system("clear")
		print("\033[7;91mToken not Found\033[0m")
		log()
	id=user[0]
	url1=f"https://graph.facebook.com/{id}?fields=name&access_token={token}"
	rq2=requests.get(url1)
	rp2=json.loads(rq2.text)
	t_name=rp2['name']
	tar_name.append(t_name)
	t_id=rp2['id']
	os.system("clear")
	print(logo)
	u=(f"{r}Target Info{S}\n{B}Name: {V}{t_name}{S}\n{B}ID: {V}{t_id}{S}\n{B}======================================{S}")
	for lettre in u:
		print(lettre,end='',flush=True)
		time.sleep(0.1)
	print()
	print(f"{R}[1]{B}Post Link")
	print(f"{R}[2]{B}Dump all post ID(Best)")
	print(f"{R}[3]{B}Exit")
	select=int(input(f"{B}Your Choice: {S}"))
	if str(select)=="1":
		os.system("clear")
		print(logo)
		print()
		p_link=input(f"{B}[{C}•{B}]Post Link: {S}").split("/")
		id=p_link[3]
		pub=p_link[5]
		pub_id=f"{id}_{pub}"
		s_pub=open("id_pub.txt",'w')
		s_pub.write(pub_id)
		s_pub.close()
		x=len(pub)
		if str(x)=="15":
			os.system("clear")
			print("\033[7;92mPost Link Valid\033[0m")
			time.sleep(2)
			os.system("clear")
			print(logo)
			print()
			print(f"{B}[{V}✓{B}]Your Post Link:{V}",pub_id,f"{S}")
			coms()
		elif str(x)=="6":
			os.system("clear")
			print("\033[7;91mGroup Post Not Valid\033[0m")
			time.sleep(2)
			dump()
		else:
			os.system("clear")
			print("\033[7;91mInvalid Link\033[0m")
			time.sleep(2)
	if str(select)=="2":
			url2=f"https://graph.facebook.com/{id}?fields=feed.limit=(0)&access_token={token}"
			rq2=requests.get(url2)
			rp2=json.loads(rq2.text)
			for x in rp2['feed']['data']:
				all_pubs=x['id']
				pub_time=x['created_time']
				open("tool/result.txt",'a').write(f"{all_pubs}\n")
			post()
	if str(select)=="3":
					exit("\033[7;92mGoodbye\033[0m")
					
					
def post():
			try:
				pub=open("tool/result.txt",'r').readlines()
			except IOError:
				os.system("clear")
				print("\033[7;91mUnknow Error\033[0m")
			x=len(pub)
			stable=pub.insert(0,"stable")
			os.system("clear")
			print(logo)
			print()
			print(f"{B}[{V}✓{B}]Total post:{V}",x,f"{S}")
			n=int(input(f"{B}[{R}•{B}]Choose Your Post:{S} "))
			select_pub=pub[n].strip()
			s_post=open("tool/id_pub.txt",'w')
			s_post.write(select_pub)
			s_post.close()
			os.system("clear")
			print(logo)
			print(f"{B}[{V}•{B}]Your Post ID: {V}",select_pub,f"{S}")
			coms()			
			
def coms():
			mess=input(f"{B}[{R}•{B}]Comment: ")
			f_coms.append(mess)
			limit=input(f"{B}[{R}•{B}]Limit: ")
			if limit.isnumeric():
				limite.append(limit)
				main()
			else:
				print("\033[7;91mNumber only\033[0m")
				time.sleep(2)
				os.system("clear")
				print(logo)
				print()
				limit=input(f"{B}[{R}•{B}]Limit: ")
				if limit.isnumeric():
					limite.append(limit)
					main()
				else:
					os.system("clear")
					print("\033[7;91mGoodbye\033[0m")
					time.sleep(2)
					exit()
					
def start(commentaire):
			global i,Ok,user,thread_ok,thread_no
			try:
				token=open("tool/Token.txt",'r').read()
				pub_id=open("tool/id_pub.txt",'r').read()
				id=user[0]
			except IOError:
				os.system("clear")
				print("\033[7;91mAn error was occured\033[0m")
				time.sleep(2)
				os.system("clear")
				dump()
			t_ok=len(Ok)
			t_no=len(No)
			sys.stdout.write(f"\r{B}Sending comment [{B}{i}{B}/{B}{limite[0]}{B}]  {V}OK:{B} {t_ok} {R}NO:{B} {t_no}{S}\r")
			sys.stdout.flush()
			url=f"https://graph.facebook.com/{pub_id}/comments?message={commentaire}&access_token={token}"
			rq1=requests.post(url)
			rp1=json.loads(rq1.text)
			i+=1
			if 'id' in rp1:
				Ok.append("Ok")
				thread_ok+=1
				time.sleep(2)
			else:
				No.append("No")
				thread_no+=1
				print(rp1)
				time.sleep(1)
			
def main():
			os.system("clear")
			print(logo)
			global f_coms,limite,coments
			barrière=limite[0]
			comms=f_coms[0]
			name=tar_name[0]
			coments.append(comms)
			coments*=int(barrière)
			commentaire=coments
			mot=(f"{B}[{V}+{B}]Target Name: {V}{name}{S}\n{B}[{V}+{B}]Total Comms: {V}{limite[0]}{S}\n{B}[{R}•{B}]Wait Tool processing{S}\n{B}[{V}✓{B}]Tool Starting...{S}\n{B}======================================={S}\n")
			for lettre in mot:
				print(lettre,end='',flush=True)
				time.sleep(0.1)
			with tpe(max_workers=3) as speed:
				speed.map(start, commentaire)
			mots=(f"{B}[{V}✓{B}]Tool process finished successfuly{S}\n{B}[{V}+{B}]Total sent: {V}{thread_ok}{S}\n{B}[{R}x{B}]Total not sent: {R}{thread_no}{S}\n{B}======================================={S}\n")
			os.system("clear")
			print(logo)
			for lettres in mots:
				print(lettres,end='',flush=True)
				time.sleep(0.1)
			exit()
def key():
	path=("tool")
	if os.path.exists(path):
		pass
	else:
		os.mkdir(path)
	os.system("clear")
	mot=(f"{v}Correct Password😁 {S}")
	keys=input(f"{B}Tool Password: {S}")
	if keys=="MrBot":
					os.system("clear")
					for lettre in mot:
						print(lettre,end='',flush=True)
						time.sleep(0.1)
					relogin()
	else:
					mot1=(f"{r}Incorrect Password{S}")
					os.system("clear")
					for lettres in mot1:
						print(lettres,end='',flush=True)
						time.sleep(0.1)
					os.system("xdg-open https://www.facebook.com/MrUser.505")
					key()
					
def relogin():
					os.system("clear")
					dire=("tool/Token.txt")
					if os.path.exists(dire):
						token=open("tool/Token.txt",'r').read()
						print(f"{B}[{V}+{B}]Wait tool loading{S}")
						try:
							rq4=requests.get(f"https://graph.facebook.com/me?fields=name&access_token={token}")
							rp4=json.loads(rq4.text)
						except requests.exceptions.ConnectionError:
							os.system("clear")
							print(f"{r}No Internet Connection{R}")
							time.sleep(2)
							log()
						if 'name' in rp4:
							name=rp4['name']
							me.append(name)
							os.system("clear")
							o=(f"{v}Login Success{S}")
							for ox in o:
								print(ox,end='',flush=True)
								time.sleep(0.1)
							os.system("clear")
							print(logo)
							k=(f"{B}  Connected to: {V}{name}{S}\n{B}======================================={S}\n")
							for lettre in k:
								print(lettre,end='',flush=True)
								time.sleep(0.1)
							print(f"{B}[1]Start the tool")
							print(f"{B}[2]Log out{S}")
							print(f"{B}[0]Exit{S}")
							print()
							choice=input(f"{B}Choose option: ")
							if choice in ['1','a','A']:
								user_id()
							elif choice in ['2','b','B']:
								os.system("clear")
								u=(f"{v}Disconnected Successfuly{S}")
								for ux in u:
									print(ux,end='',flush=True)
									time.sleep(0.1)
								log()
									
							elif choice in ['0','00']:
									os.system("clear")
									exit()
							else:
								print("Wrong input")
						else:
							os.system("clear")
							ui=(f"{r}Invalid Token{S}")
							for uix in ui:
								print(uix,end='',flush=True)
								time.sleep(0.1)
							log()
					else:
						log()
						
						
def user_id():
					name=me[0]
					os.system("clear")
					print(logo)
					s=(f"{B}       Hello: {J}{name}{S}\n{B}======================================={S}\n")
					for lettre in s:
						print(lettre,end='',flush=True)
						time.sleep(0.1)
					t_user=input(f"{B}[{V}•{B}]Target ID: ")
					if '1000' in t_user:
						user.append(t_user)
						os.system("clear")
						print(logo)
						dump()
					else:
						os.system("clear")
						print(f"{r}Wrong ID{S}")
						time.sleep(2)
						os.system("clear")
						print(logo)
						print(s)
						t_user=input(f"{B}[{V}•{B}]Target ID: ")
						if '1000' in t_user:
							user.append(t_user)
							os.system("clear")
							print(logo)
							dump()
						else:
							os.system("clear")
							print(f"{r}Wrong ID *2{S}")
							time.sleep(2)
							os.system("clear")
							print(f"{r}Good Bye{S}")
							exit()
					

def maj():
			os.system("clear")
			fa=(f"{B}[{V}+{B}]If you don't have internet connections,please disable and enable your mobile data for run the tool{S}")
			for fax in fa:
				print(fax,end='',flush=True)
				time.sleep(0.1)
			try:
				subprocess.check_call(['git','pull','-q'])
				os.system("clear")
				fab=(f"{v}Update Success{S}")
				for fabx in fab:
								print(fabx,end='',flush=True)
								time.sleep(0.08)
				key()
			except subprocess.CalledProcessError:
								os.system("clear")
								print(f"{r}An error was occured when updating the tool{S}")
								time.sleep(2)
								key()
								
			
maj()	

						
			
		