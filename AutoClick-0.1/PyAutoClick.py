# -*- coding: utf-8 -*#

'''
PyAutoClick 0.1
'''
import pyautogui
import time

def click():
    pyautogui.alert(text = "Gravar posição 1 do cursor", title = 'Auto click')
    time.sleep(5)
    pos1 = pyautogui.position()
    pyautogui.alert(text = "Posição 1 gravada", title = 'Auto click')

    pyautogui.alert(text = "Gravar posição 2 do cursor", title = 'Auto click')
    time.sleep(5)
    pos2 = pyautogui.position()
    pyautogui.alert(text = "Posição 2 gravada", title = 'Auto click')

    pyautogui.alert(text = "Iniciando...",title = "Auto click")
    try:
        while(True):
            pyautogui.click(pos1,button='left')
            #print("Clicando")
            pyautogui.click(pos2, button = 'left')
            #print("Clicando")

    except KeyboardInterrupt:
        pyautogui.alert(text = "Saindo...", title = 'Auto click')
