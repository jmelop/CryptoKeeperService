from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule

websites = ['https://cointelegraph.com', 'https://www.investing.com/news/cryptocurrency-news', 'https://www.forbes.com/crypto-blockchain/']

cointelegraph = []
investing = []
forbes = []

def getNewsFromList():
    for web in websites:
        print(web)

        driver = webdriver.Chrome('C:/WebDrivers/chromedriver.exe')
        driver.get(web)
        time.sleep(3)

        if web == 'https://cointelegraph.com':

            titles = driver.find_elements_by_class_name('main-news-controls__link')

            for new in titles:
                print(new.text)

                if len(cointelegraph) < 5:
                    cointelegraph.append(new.text)

            print('--------------------')
            print(cointelegraph)

        elif web == 'https://www.investing.com/news/cryptocurrency-news':

            n = 3

            titles = driver.find_elements_by_class_name('title')

            newTitles = titles[n:]

            for new in newTitles:
                print(new.text)

                if len(investing) < 5:
                    investing.append(new.text)

            print('--------------------')
            print(investing)

        else:

            titles = driver.find_elements_by_class_name('section-pick__title')

            for new in titles:
                print(new.text)

                if len(forbes) < 5:
                    forbes.append(new.text)

            print(forbes)

        driver.quit()


schedule.every(1).second.do(getNewsFromList)

while True:
    schedule.run_pending()
    time.sleep(5)
