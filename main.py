from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

websites = ['https://cointelegraph.com', 'https://www.coindesk.com', 'https://bitcoinmagazine.com']


def getNewsFromList():
    for web in websites:
        print(web)

        driver = webdriver.Chrome('C:/WebDrivers/chromedriver.exe')
        driver.get(web)
        time.sleep(3)

        if web == 'https://cointelegraph.com':
            print('Cointelegraph')
        elif web == 'https://www.coindesk.com':
            print('Coindesk')
        else:
            print('BitcoinMagazine')

        driver.quit()


getNewsFromList()
