#####create by 'REDOY KHAN'####


import os,requests



os.system('clear')

#-------------logo-----------------#
logo ="""
 ######  ##     ##  ######  
##    ## ###   ### ##    ## 
##       #### #### ##       
 ######  ## ### ##  ######  
      ## ##     ##       ## 
##    ## ##     ## ##    ## 
 ######  ##     ##  ######  

══════════════════════════════════════
FACEBOOK  : REDOY KHAN
══════════════════════════════════════"""
os.system("clear")

def lone():
	print('══════════════════════════════════════')
        
def clear():
	os.system('clear')
	print(logo)
	
	
def main():
	clear()
	print(f'(1) ➪ CUSTOM SMS SENDER ')
	print(f'(2) ➪ CONTACT ADMIN ')
	lone()
	sex=input(' CHOICE >> ')
	if sex in ['A','1']:sms()
	if sex in ['B','2']: os.system("xdg-open https://facebook.com/spamar.xudi.na")
	main()
	
	
def sms():
	clear()
	NUM=input('➪ Enter Number:- ')	
	MSG=input('➪ Enter Massage:-')    
	Api = requests.get(f"https://sobgoru.000webhostapp.com/App/test.php/?number={NUM}&msg="+MSG)
	print(Api.text)
	time.sleep(2)
	input(f' PRESS ENTER TO SEND MORE SMS  ')
	os.system('clear')
	sms()
	os.system('clear')
	main()
	
	
main()



#####@#no credit= api off #######
