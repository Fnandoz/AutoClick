# -*- coding: utf-8 -*#
'''
PyAutoClick 0.1
'''

import pyautogui
from AutoClick import click
while(True):
    botao = pyautogui.confirm(text='Auto Click', title='Auto Click', buttons=['Iniciar','Sair'])

    if(botao == 'Iniciar'):
        click()
    else:
        break



