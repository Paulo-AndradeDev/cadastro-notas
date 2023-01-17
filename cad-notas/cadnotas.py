import pyautogui

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('cmd')
pyautogui.press('enter')
pyautogui.PAUSE = 1.5

pyautogui.write('cd cad-notas')
pyautogui.press('enter')


pyautogui.write('python manage.py runserver')
pyautogui.press('enter')
pyautogui.PAUSE = 1.5

pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.PAUSE = 1.5


pyautogui.write('http://127.0.0.1:8000/admin')
pyautogui.press('enter')
pyautogui.PAUSE = 1.5





