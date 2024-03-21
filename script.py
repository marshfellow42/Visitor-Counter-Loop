import webbrowser
import time
import pyautogui

url = input("What's your GitHub profile link?: ")

refresh_limit = int(input("How many times should it refresh?: "))

website_load_time = float(input("How long should it take for the website to fully load?: "))

wait_time = float(input("How many seconds should it take to refresh?: "))

webbrowser.open(url, new=0)

time.sleep(website_load_time)

for i in range(refresh_limit):
    time.sleep(wait_time)
    pyautogui.hotkey('f5')