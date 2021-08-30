import time

from microdotphat import clear, show, set_decimal, set_pixel, write_string, WIDTH, HEIGHT

def displayFlash(flashText, t=0.2, T=2):
    now = time.time()
    while True:
        clear()
        show()
        time.sleep(t)
        write_string(flashText, kerning=False)
        show()
        elapsed = time.time() - now
        if elapsed > T: 
            clear()
            show()
            break
