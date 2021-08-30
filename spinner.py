from numpy import arange
from microdotphat import clear, write_string, scroll_vertical, show
import sys
import time

def numberSpinner(startValue, endValue):
    for i in arange(startValue, endValue, 0.01): 
        print(str(round(i,2)))
        clear()
        write_string(str(round(i,2)), kerning=False)
        show()
        time.sleep(0.0002)
    
    write_string(str(round(endValue,2)), kerning=False)
    show()



