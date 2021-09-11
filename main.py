#!/usr/bin/env python

import time
import sys
from microdotphat import HEIGHT, write_string, scroll_vertical, show, clear
from flash import displayFlash
from spinner import numberSpinner
from getbalance import getPostBalances

yeOldBalances=getPostBalances()
# time.sleep(10) 

def winRoutine(currency,oldBalance,newBalance):
    numberSpinner(float(oldBalance),float(newBalance))
    displayFlash(newBalance,0.001,2)
    displayFlash(currency,0.001,1)
    clear()

def printBalances(balances): 
    clear()
    for line, currency in enumerate(balances): 
        write_string(balances[currency][0], offset_y=line*14, kerning=False)
        write_string(balances[currency][1], offset_y=7+line*14, kerning=False)
        print('debug: balances[currency][0] och [1]: ' + balances[currency][0] + '   offset: ' + str(line*14) + ' ' + balances[currency][1] + '   offset: ' + str(7+line*14))
        print line
    show()
    
    i = 0
    while i < len(balances)*2-1: 
        time.sleep(4)
        for x in range(7): 
            scroll_vertical()
            show()
            time.sleep(0.002)
        i = i+1
        print i

    # not sure why this last scroll run is needed, but if not done the starting/end point will move one step each time printBalances() run which leaves the buffer being scrolled in the wrong order after the first run. i think clear() should take care of that, but it doesn't.
    for x in range(7): 
        scroll_vertical()
    time.sleep(4)
#    clear()
#    show()

while True: 
    try:
        freshBalances=getPostBalances()
    
    except: 
        print('getPostBalances() failed')

    else:    
        for currency in freshBalances: 
            if float(freshBalances[currency][1]) > float(yeOldBalances[currency][1]): 
                winRoutine(freshBalances[currency][0],yeOldBalances[currency][1],freshBalances[currency][1])
                print 'debug: running win routine'
        printBalances(freshBalances) 

    # debug
    print freshBalances
    print yeOldBalances

    time.sleep(180)

