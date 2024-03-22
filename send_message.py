import pyautogui as pag
from time import sleep

sentence = ""
letter_list = list(sentence)

pag.hotkey("alt", "tab")

i = 1057
while True:
    
    pag.write(f"{i}) ")
    

    pag.press("enter") 

    i += 1
