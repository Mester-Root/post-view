# !/usr/bin/python3
# viewer rubika.ir
import time,sys,os,random
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
created = 'Mr. Root [Saleh]'
#---------------------------
try:
    from requests import post as pt
except:
    os.system("pip install requests")
    from requests import post as pt
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
    from colorama import Fore
try:
    import pyuseragents
except:
    os.system("pip install pyuseragents")
    import pyuseragents
try:
    import datetime
except:
    os.system("pip install datetime")
    import datetime
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
    import pyfiglet
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# $ clear
try:
    os.system("clear")
except:
    os.system("cls")
date = (datetime.datetime.today())
time.sleep(1)
timer = (Fore.YELLOW+F'\nStArT > {date} [#] <~> Mr. Root [saleh] <@THEserver> <~>\n')
print(timer)
time.sleep(1)
logo = ['Rubika','rubika . ir','ViewEr','view','viewing','views','ViEwEr','viewer','rubika']
banner = (random.choice(logo))
bnr = (pyfiglet.figlet_format(banner))
print(Fore.RED+'')
print(bnr)
time.sleep(1)
print(Fore.WHITE+"\nversion --> '1.0.0' \n\n")
time.sleep(2)
username = input(Fore.GREEN+'\nĚŇŤĚŘ channel for view'+Fore.YELLOW+' <--> '+Fore.BLUE+'[username] '+Fore.RED+'dont "@"'+Fore.WHITE+' _> ')
print('\n\n')
time.sleep(1)
number = input(Fore.GREEN+'ĚŇŤĚŘ number for view or sin (200) _> '+Fore.WHITE+'')
print('\n\n')
time.sleep(2)
number = int(number)
num = 0
num = int(num)
auth = ''
# ----- while ----
_NUMBER_ = int(number)
while number != num:
    # -------------- head ------------
    head = {'Host':'https://messengerg2c74.iranlms.ir/','User-Agent': pyuseragents.random(),'Content-Type':'application/json','Accept':'application/json, text/plain, */*','content-length':'2127','content-type':'application/json'}
    # --------- json ----------
    json = {"api_version":"5","auth": auth, "method":"GetFile.ashx","message_id": username, "data_enc":"O3uANv/X/dpDKAjFxc1gZqTmvJ0kcP1ke8RlTBw19mfAOBMva/JpF/yJskbNI/ZqxStLAoJY29pB2L0OXDnKdXEUUvcCdrZjAqJKLvehKbTsBh7FDiAViDZwJi24FBdE6E4Zo7/VC1r9lYFsFb10o4SBHL5UEw1MrRhoDJi5yaAlIhpSwChKukCt5Fy86yBL3mfeUZkWHBHRzir3eQCfHXo64cxkGQdUSASrSE6TKHkt9b2xGy1ToD0UFH2eX9yOnZKoNk3oSZcSHf5BYgOyKw=="}
    # --------- data ---------
    data = {'username': username,'user-caption': username,'user_modal_username': username,'touch-action': username,'user-last-message': username,"message_id": username, "data_enc":"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"}
    #------------------------------------------
    try:
        time.sleep(3)
        pt('https://messengerg2c74.iranlms.ir/',headers=head,json=json,data=data)
        pt(f'https://web.rubika.ir/#im?um={username}',headers=head,json=json,data=data)
        print(Fore.YELLOW+f'\n~>> [SENT NEW VIEW IN] < @{username} > <<~')
    except:
        time.sleep(2)
        print(Fore.RED+f'\n~>> NOT VIEW <<~')
    number = (number-1)
    # the end
time.sleep(3)
print(Fore.WHITE+F'\n\n\nO.K. MY FRIEND | >> [{_NUMBER_}] SENTED TO [@{username}] <<\n')
time.sleep(1)
sys.exit()
