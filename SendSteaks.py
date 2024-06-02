from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from quests import questions
os.system("gnome-terminal -- google-chrome-stable --remote-debugging-port=9988")
sleep(3)

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress","localhost:9988")
driver = webdriver.Chrome(service=Service(executable_path="/home/srihithreddy/Snapbot/chromedriver"),options=options)
driver.get('https://web.snapchat.com/')
sleep(10)
Capture_Open_button = driver.find_element('xpath', '/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/button[1]')
    # Click the send button
Capture_Open_button.click()

    
    # Sleep for a short duration to allow time for the message to be sent
sleep(10)    
Capture_button = driver.find_element('xpath', '/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/button[1]')
    # Click the send button
Capture_button.click()
sleep(3)
    # Sleep for a short duration to allow time for the message to be sent
sendTO_button = driver.find_element('xpath', '/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/button[2]')
    # Click the send button
sendTO_button.click()
sleep(3)

    # Sleep for a short duration to allow time for the message to be sent

Streak_button = driver.find_element('xpath', '/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/form/div/div[2]/button')
    # Click the send button
Streak_button.click()
sleep(3)
from selenium.common.exceptions import NoSuchElementException

i = 2  # Starting index
while True:
    try:
        xpath = f'/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/form/div/ul/li[{i}]/div/div[2]/div'
        select_ppl_button = driver.find_element('xpath', xpath)
        select_ppl_button.click()
        i += 1  # Increment the index
    except NoSuchElementException:
        # If no more elements are found, exit the loop
        break
sleep(3)
final_send=driver.find_element('xpath','/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/form/div[2]/button/div')
final_send.click()
