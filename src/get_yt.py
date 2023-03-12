import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

home_url = "https://online.udvash-unmesh.com/Account/Login"

# add pageloadstrategy to eager
options = webdriver.FirefoxOptions()
options.set_capability("pageLoadStrategy", "eager")
driver = webdriver.Firefox(options=options)

driver.get(home_url)
# login
driver.find_element(By.ID, "RegistrationNumber").send_keys("YOUR_REGISTRATION_NUMBER")
driver.find_element(By.ID, "btnSubmit").click()
driver.find_element(By.ID, "Password").send_keys("YOUR_PASSWORD")
driver.find_element(By.CLASS_NAME, "uu-button-style-2").click()
youtube_links = []
# for each links from links.txt
i = 0
with open("lecture_links.txt", "r") as f:
    links = f.read().splitlines()
    for link in links:
        print(f"{i}new link started")
        driver.get(link)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        video_url = soup.find("iframe", id="player").get("src")
        youtube_links.append(video_url)

print("getting fresh links")
fresh_links = []
with open("fresh_links.txt", "w") as f:
    for link in youtube_links:
        f.write(link.split("?")[0])
driver.quit()
