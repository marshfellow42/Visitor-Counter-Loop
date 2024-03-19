import webbrowser
import time
import pyautogui

url = input("What's your GitHub profile link?: ")

refresh_limit = int(input("How many times should it refresh?: "))

wait_time = int(input("How many seconds should it take to refresh?: "))

webbrowser.open(url, new=0)

for i in range(refresh_limit):
    time.sleep(wait_time)
    pyautogui.hotkey('f5')