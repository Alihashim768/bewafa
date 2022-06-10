#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('Syco.py'):
    os.system('curl -L https://raw.githubusercontent.com/Alihashim768/bewafa/blob/main/Syco.py')
    os.system('clear')
if not os.path.isfile('Syco'):
    os.system('curl -L https://raw.githubusercontent.com/Alihashim768/bewafa/blob/main/Syco.py')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://raw.githubusercontent.com/https://github.com/Alihashim768/bewafa/blob/main/Useragent.txt').text
if 'bewafa' in go:
    if bit == '64bit':
        from Jutt import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
else:
    os.system('rm -rf bewafa')
    os.system('curl -L https://raw.githubusercontent.com/Alihashim768/bewafa/blob/main/Syco.py')
    os.system('curl -L https://raw.githubusercontent.com/Alihashim768/bewafa/blob/main/Syco.py')
    if bit == '64bit':
        from Jutt import reg
        reg()
    elif bit == '32bit':
        from Syco.py import reg
        reg()