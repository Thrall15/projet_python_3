import pyautogui
import time

texte = "Salut toi ! tu vas bien ? 💕 "

time.sleep(30)
for t in range(0,3) :
    for i in range(0,len(texte)) :
        pyautogui.press(texte[i])
    time.sleep(10)