import pyautogui as pg
import time

#pip install -i https://pypi.rd.corpintra.net/root/pypi <package-name> --trusted-host pypi.rd.corpintra.net

while(True):
	
	pg.click(x=100, y=200)
	#pyautogui.move(0, 50)
	time.sleep(10)
	pg.click(x=200, y=400)
	time.sleep(10)
	#pyautogui.move(0, -50)
	