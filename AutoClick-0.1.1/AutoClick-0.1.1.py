# -*- coding: utf-8 -*-
import pyautogui
import time
import thread

posicoes = []

def grava():
    pos = input("Quantas posiçoes deseja salvar?")
    sec = input("Delay")

    for i in range(pos):
        print("Gravando %dª posiçao" % (i))
        posicoes.append(pyautogui.position())
        time.sleep(sec)

    # for posic in posicoes:
    #   print posicoes[i]


def click():
    while True:
        for i in range(len(posicoes)):
            pyautogui.click(posicoes[i], button='left')




grava()
click()


