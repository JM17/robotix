import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException


def init_driver():
  binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
  driver = webdriver.Firefox(firefox_binary=binary)
  driver.wait = WebDriverWait(driver, 5)
  return driver

def lookup(driver, query):
  driver.get("http://www.google.pl")
  try:
    box = driver.wait.until(EC.presence_of_element_located((By.NAME, "q")))
    button = driver.wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
    box.send_keys(query)
    try:
      button.click()
    except ElementNotVisibleException:
      button = driver.wait.until(EC.visibility_of_element_located((By.NAME,"btnG")))
      button.click()
  except TimeoutException:
    print("Box or Button not found in google.pl")

if __name__ == "__main__":
  driver = init_driver()
  lookup(driver, "Selenium")
  time.sleep(5)
  driver.quit()
