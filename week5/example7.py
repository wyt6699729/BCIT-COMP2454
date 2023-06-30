from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
DRIVER_PATH = "/Python/ChromeDriver/chromedriver"
browser = None
# This loads webdriver from the local machine if it exists.
try:
    browser = webdriver.Chrome(service=Service(DRIVER_PATH))
    print("The path to webdriver_manager was found.")
# If a webdriver not found error occurs it is then downloaded.
except:
    print("webdriver not found. Update 'DRIVER_PATH' with file path in the download.")
    browser = webdriver.Chrome(ChromeDriverManager().install())
