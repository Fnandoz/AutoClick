import pyautogui

while(True):
    botao = pyautogui.confirm(text='Auto Click', title='Auto Click', buttons=['Iniciar','Sair'])

    if(botao == 'Iniciar'):
        import AUTOCLICK01.py
    else:
        break

