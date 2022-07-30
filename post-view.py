#!/bin/python# !/usr/bin/python3
# viewer rubika.ir
from os import system
import sys
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
created = 'Mr. Root [Saleh]'
#---------------------------
try:
    from requests import post, get
except:
    system("pip install requests")
    from requests import post, get
try:
    import datetime
except:
    system("pip install datetime")
    import datetime
try:
    import pyfiglet
except:
    system("pip install pyfiglet")
    import pyfiglet
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
try:
    system('cls')
except:
    system('clear')
from re import findall
from random import randint, choice
from json import loads, dumps, JSONDecodeError
import base64,urllib3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from time import sleep, time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class encryption:
    def __init__(self, auth):
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if e >= '0' and e <= '9':
                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode('UTF-8'), AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = aes.encrypt(raw)
        result = base64.b64encode(enc).decode('UTF-8')
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(base64.urlsafe_b64decode(text.encode('UTF-8')))
        result = unpad(dec, AES.block_size).decode('UTF-8')
        return result

class accesses:
	class admin:
		pin               = "PinMessages"
		newAdmin          = "SetAdmin"
		editInfo          = "ChangeInfo"
		banMember         = "BanMember"
		changeLink        = "SetJoinLink"
		editMembersAccess = "SetMemberAccess"
		deleteMessages    = "DeleteGlobalAllMessages"

	class user:
		viewMembers = "ViewMembers"
		viewAdmins  = "ViewAdmins"
		sendMessage = "SendMessages"
		addMember   = "AddMember"

class clients:
	web = {
		"app_name"    : "Main",
		"app_version" : "3.2.1",
		"platform"    : "Web",
		"package"     : "web.rubika.ir",
		"lang_code"   : "fa"
	}

	android = {
		"app_name"    : "Main",
		"app_version" : "2.8.1",
		"platform"    : "Android",
		"package"     : "ir.resaneh1.iptv",
		"lang_code"   : "fa"
	}

defaultDevice = {
	"app_version":"MA_2.9.8",
	"device_hash":"CEF34215E3E610825DC1C4BF9864D47A",
	"device_model":"rubika-library",
	"is_multi_account": False,
	"lang_code":"fa",
	"system_version":"SDK 22",
	"token":"cgpzI3mbTPKddhgKQV9lwS:APA91bE3ZrCdFosZAm5qUaG29xJhCjzw37wE4CdzAwZTawnHZM_hwZYbPPmBedllAHlm60v5N2ms-0OIqJuFd5dWRAqac2Ov-gBzyjMx5FEBJ_7nbBv5z6hl4_XiJ3wRMcVtxCVM9TA-",
	"token_type":"Firebase"
}

class Seen:
    def __init__(self, auth=None, device=defaultDevice):
        if auth != None:
            self.auth = auth
        self.enc = encryption(self.auth)
    @staticmethod
    def _getURL():
        return "https://messengerg2c64.iranlms.ir/"
    @staticmethod
    def registerDevice(auth, device=defaultDevice):
        while True:
            try:
                enc = encryption(auth)
                response = loads(enc.decrypt(post(json={
                    "api_version":"4",
                    "auth":auth,
                    "client": clients.android,
                    "data_enc":enc.encrypt(dumps(device)),
                    "method":"registerDevice",
                },url=Seen._getURL()).json()["data_enc"]))
                return response
            except JSONDecodeError: break

    @staticmethod
    def _parse(mode:str, text:str):
        results = []
        if mode.upper() == "HTML":
            realText = text.replace("<b>","").replace("</b>","").replace("<i>","").replace("</i>","").replace("<pre>","").replace("</pre>","")
            bolds = findall("<b>(.*?)</b>",text)
            italics = findall("<i>(.*?)</i>",text)
            monos = findall("<pre>(.*?)</pre>",text)

            bResult = [realText.index(i) for i in bolds]
            iResult = [realText.index(i) for i in italics]
            mResult = [realText.index(i) for i in monos]

            for bIndex,bWord in zip(bResult,bolds):
                results.append({
                    "from_index": bIndex,
                    "length": len(bWord),
                    "type": "Bold"
                })
            for iIndex,iWord in zip(iResult,italics):
                results.append({
                    "from_index": iIndex,
                    "length": len(iWord),
                    "type": "Italic"
                })
            for mIndex,mWord in zip(mResult,monos):
                results.append({
                    "from_index": mIndex,
                    "length": len(mWord),
                    "type": "Mono"
                })

        elif mode.lower() == "markdown":
            realText = text.replace("**","").replace("__","").replace("`","")
            bolds = findall(r"\*\*(.*?)\*\*",text)
            italics = findall(r"\_\_(.*?)\_\_",text)
            monos = findall("`(.*?)`",text)

            bResult = [realText.index(i) for i in bolds]
            iResult = [realText.index(i) for i in italics]
            mResult = [realText.index(i) for i in monos]

            for bIndex,bWord in zip(bResult,bolds):
                results.append({
                    "from_index": bIndex,
                    "length": len(bWord),
                    "type": "Bold"
                })
            for iIndex,iWord in zip(iResult,italics):
                results.append({
                    "from_index": iIndex,
                    "length": len(iWord),
                    "type": "Italic"
                })
            for mIndex,mWord in zip(mResult,monos):
                results.append({
                    "from_index": mIndex,
                    "length": len(mWord),
                    "type": "Mono"
                })

        return results

    def sendMessage(self, chat_id, text, metadata=[], parse_mode=None, message_id=None):
        inData = {
            "method":"sendMessage",
            "input":{
                "object_guid":chat_id,
                "rnd":f"{randint(100000,999999999)}",
                "text":text,
                "reply_to_message_id":message_id
            },
            "client": clients.web
        }
        if metadata != [] : inData["input"]["metadata"] = {"meta_data_parts":metadata}
        if parse_mode != None :
            inData["input"]["metadata"] = {"meta_data_parts": Seen._parse(parse_mode, text)}
            inData["input"]["text"] = text.replace("<b>","").replace("</b>","").replace("<i>","").replace("</i>","").replace("<pre>","").replace("</pre>","") if parse_mode.upper() == "HTML" else text.replace("**","").replace("__","").replace("`","")

        return loads(self.enc.decrypt(post(json={"api_version":"5","auth":self.auth,"data_enc":self.enc.encrypt(dumps(inData))},url=Seen._getURL()).json()["data_enc"]))

    def forwardMessages(self, From, message_ids, to):
        return loads(self.enc.decrypt(post(json={"api_version":"5","auth": self.auth,"data_enc":self.enc.encrypt(dumps({
            "method":"forwardMessages",
            "input":{
                "from_object_guid": From,
                "message_ids": message_ids,
                "rnd": f"{randint(100000,999999999)}",
                "to_object_guid": to
            },
            "client": clients.web
        }))},url=Seen._getURL()).json()["data_enc"]))

    def seenChats(self, seenList):
        # seenList must be a dict , keys are object guids and values are last message’s id, {"guid":"msg_id"}
        return loads(self.enc.decrypt(post(json={"api_version":"5","auth": self.auth,"data_enc":self.enc.encrypt(dumps({
            "method":"seenChats",
            "input":{
                "seen_list": seenList
            },
            "client": clients.web
        }))},url=Seen._getURL()).json()["data_enc"]))

    def joinGroup(self, link):
        hashLink = link.split("/")[-1]
        return loads(self.enc.decrypt(post(json={"api_version":"5","auth": self.auth,"data_enc":self.enc.encrypt(dumps({
            "method":"joinGroup",
            "input":{
                "hash_link": hashLink
            },
            "client": clients.web
        }))},url=Seen._getURL()).json()["data_enc"]))

    def leaveGroup(self, chat_id):
        return loads(self.enc.decrypt(post(json={"api_version":"5","auth": self.auth,"data_enc":self.enc.encrypt(dumps({
            "method":"leaveGroup",
            "input":{
                "group_guid": chat_id
            },
            "client": clients.web
        }))},url=Seen._getURL()).json()["data_enc"]))

    def auths():
        auths = ""
        choices = [*"abcdefghijklmnopqrstuvwxyz"]
        for i in range(32): auths += choice(choices)
        return auths

class run:
    def run():
        date = (datetime.datetime.today())
        sleep(1)
        timer = (F'\033[93m\nStArT > {date} [#] <~> Mr. Root [saleh] <@THEserver> <~>\n')
        print(timer)
        sleep(1)
        logo = ['Rubika','rubika . ir','ViewEr','view','viewing','views','ViEwEr','viewer','rubika']
        banner = (choice(logo))
        bnr = (pyfiglet.figlet_format(banner))
        print('\033[91m')
        print(bnr)
        sleep(1)
        print("\n\033[93mversion \033[31m--> \033[36m'1.0.0' \n\n")
        sleep(2)
        methods : str = input('\n\033[31m[?] \033[36mmethos :\n\n\033[31m[*] \033[36mrandom AUTH \033[93m[0]\n\n\033[31m[*] \033[36myour AUTH \033[93m[1]\n\n\033[35m[#] \033[92mplease enter method number \033[31m_> \033[0m')
        _from_ = input('\n\033[31m[?] \033[36mplease enter guid channel for seen \033[31m_> \033[0m')
        msg = input('\n\033[31m[?] \033[36mplease enter message_id post \033[31m_> \033[0m')
        if methods == '1':
            auth : str = input('\n\033[31m\033[36mplease enter your AUTH \033[31m_> \033[0m')
            bot = Seen(auth=auth)
        linker : str = input('\n\033[31m[?] \033[36mplease enter directory file links \033[31m_> \033[0m')
        links : list = open(linker, 'r').read().split('\n')
        for link in links:
            sleep(1.7)
            auths : str = Seen.auths()
            if methods == '0':
                try:
                    bot.Seen(auth=auths)
                except:
                    pass
            try:
                _to_ = bot.joinGroup(link)
            except:
                pass
            try:
                _to_ : str = _to_.get('data').get('group').get('group_guid')
                pass
            except:
                pass
            try:
                bot.forwardMessages(_from_, msg, _to_)
                print('\n\033[31m[+] \033[92msenting-! AUTH True')
            except:
                print('\n\033[31m[!] \033[35mnot senting-! or AUTH False')
            try:
                bot.seenChats({_from_:msg})
            except:
                pass
            try:
                bot.leaveGroup(_to_)
            except:
                pass
run.run()
