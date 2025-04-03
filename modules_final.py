import time
import random
import pyautogui
import keyboard

# Saisie d'un texte : 
def saisir_un_texte() :
    texte_1 = "Salut toi ! Tu vas bien ?"
    texte_2 = "Hey babe ! Tu es là ?"
    texte_3 = "Je vais bien merci ! tu fais quoi ?"
    texte = [texte_1,texte_2,texte_3]
    texte_choisi = texte[random.randint(0,2)]
    for texte_choisi_i in range(0,len(texte_choisi)) :
        pyautogui.press(texte_choisi[texte_choisi_i])

def voir_stat() :
    # Déplacement vers onlymonster menu :
    pyautogui.moveTo(34,68)
    pyautogui.click()
    time.sleep(random.randint(10,15))

    # Chatter metrics 
    pyautogui.moveTo(155,119,duration=random.random())
    pyautogui.click()
    time.sleep(random.randint(10,15))
    
    # Choix date liste 
    pyautogui.moveTo(758,198,duration=random.random())
    pyautogui.click()
    time.sleep(random.randint(0,1))

    # This month :
    pyautogui.moveTo(285,284,duration=random.random())
    pyautogui.click()
    time.sleep(random.randint(10,11))

    # Saisie nom chatter : 
    pyautogui.moveTo(1591,246)
    pyautogui.click()
    nom = ["olivier","claude","lucas"]
    for i in range(0,len(nom)) : 
        for c in range(0,len(nom[i])):
            pyautogui.press(nom[i][c])
            time.sleep(random.random())
        pyautogui.press("enter")
    pyautogui.press("esc")
    time.sleep(random.randint(10,15))

    # clear chatter list
    pyautogui.moveTo(1868,227,duration=random.random())
    pyautogui.click()
    time.sleep(random.randint(1,3))

    # creator list : 
    pyautogui.moveTo(129,151,duration=random.random())
    time.sleep(random.randint(1,3))

# Move to gindy :
def move_to_gindy() :
    pyautogui.moveTo(27,177)
    pyautogui.click()
    time.sleep(random.randint(1,2))
    pyautogui.moveTo(98,179)
    time.sleep(random.randint(1,2))
    pyautogui.click()
    pyautogui.moveTo(290,247)
    for scrol_count in range(0,5) :
        pyautogui.scroll(random.randint(-1000,-250))
        time.sleep(random.randint(1,5))
    pyautogui.scroll(5000)
    time.sleep(random.randint(10,20))

# Move to Vanessa :
def move_to_vanessa() :
    pyautogui.moveTo(26,231)
    pyautogui.click()
    time.sleep(random.randint(1,2))
    pyautogui.moveTo(98,179)
    time.sleep(random.randint(1,2))
    pyautogui.click()
    time.sleep(random.randint(10,20))
    pyautogui.moveTo(290,247)
    for scrol_count in range(0,5) :
        pyautogui.scroll(random.randint(-1000,-250))
        time.sleep(random.randint(1,5))
    pyautogui.scroll(5000)
    time.sleep(random.randint(10,20))
    
time.sleep(10)
fonctions = [saisir_un_texte,move_to_gindy,move_to_vanessa,voir_stat]

for fonction_compteur in range(0,10) :
    fonction_choisie = random.choice(fonctions)
    fonction_choisie()
    time.sleep(30)