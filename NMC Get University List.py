import os
import pandas as  pd
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
import time #Was using time.sleep(n), but am now using driver.implicitly_wait(n)
# import urllib.request
# import webbrowser
from selenium.webdriver.chrome.options import Options
import re

from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import math

import pickle

url = "https://www.nmc.org.in/information-desk/for-students-to-study-in-india/list-of-college-teaching-mbbs/"

options = webdriver.ChromeOptions()
options.headless = True #Dont put headless on for some time. Once code is sorted, then do headless. 
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

df_to_append = pd.DataFrame()

driver.get(url)
num_pages = 2
for i in range(0, num_pages):
    df = pd.read_html(driver.page_source)[2]
    df_to_append = pd.concat([df_to_append, df], axis = 0) 
    driver.find_element(By.XPATH, '//*[(@id = "mbbsColleges_next")]').click()
    
os.chdir("C:/Users/savas/Documents/Ashoka/Economics/IGIDR/National Medical Registry/NMC_Yearwise_Scrapped_Data")
df_to_append.to_csv("MBBS College List.csv")
