import pyautogui as pag
from time import sleep, ctime

sentence = ""
letter_list = list(sentence)

pag.hotkey("alt", "tab")

sleep(1)
delay = 0.2

i = 1
while True:
    
    pag.write(f"{i}) ")
    
    # for letter in ctime():
    #     pag.write(letter)
    #     sleep(delay)
    
    pag.write(" ")
    for letter in letter_list:
        pag.write(letter)
        sleep(delay)

    pag.press("enter") 

    i += 1
