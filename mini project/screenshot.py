# pip install pyautogui

#  if use linux (ubuntu , opensuse ,....) you have install this too :
# sudo apt install python3-tk python3-dev
# sudo apt install gnome-screenshot
import pyautogui as pag

sc=pag.screenshot()
sc.save("image.jpg")