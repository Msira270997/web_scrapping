import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# Opciones para la navegacion
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.binary_location = "/opt/brave.com/brave/brave-browser"

driver_path = "/home/moises/Escritorio/Proyectos/Chrome_driver/chromedriver"
driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.get("https://criptodolar.net")
time.sleep(3)
# dolar_today = driver.find_element(By.XPATH, "//tbody/tr[1]")
# print(dolar_today)
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]"))
).click()
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
