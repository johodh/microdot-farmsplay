import re
import random
import urllib
import ConfigParser
import os

cp = ConfigParser.RawConfigParser()
config = os.getcwd() + '/config'
cp.read(config)

wallets = {}

# read config file

for a in cp.sections(): 
    if cp.get(a,'enabled') == '1': 
        wallets[a] = []
    for (k,v) in cp.items(a):
        if cp.get(a,'enabled') == '1' and k != 'enabled' : 
            wallets[a].append(v)

balances = {}

# get wallet balances from alltheblocks.net 

def getPostBalances(): 
    for currency in wallets:
        data = urllib.urlopen('https://alltheblocks.net/' + currency + '/address/' + wallets[currency][1])
        html = data.read()
        search_regex = wallets[currency][0] + ' [0-9]+.[0-9]+'
        balance = re.findall(search_regex,html)[0].split()
        balances[currency] = balance
    return balances

# generate a fake response to not overuse the source while debugging, not used in general

def fakePostBalances(): 
    balances = {'spare': ['SPARE', str(1+random.randint(1,10)*0.1)], 'flora': ['XFL', '5.000000000000'], 'chia': ['XCH', '3.342645227353'], 'flax': ['XFX', '0.500000000000'], 'silicoin': ['TSIT', '2.250000000000']}
    return balances 
