import pyautogui
import time

time.sleep(3)
pyautogui.moveTo(455,1067)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(151,56)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.3)
pyautogui.write("clickspeedtest.com")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.moveTo(744,673)

for i in range(1,52):
    pyautogui.tripleClick()
    