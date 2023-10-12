from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Safari()

browser.get('https://ca.finance.yahoo.com/crypto/')

def extractdata(counter):
    crypto = browser.find_elements(By.XPATH, '//td[@class="Va(m) Ta(start) Px(10px) Fz(s)"]')
    crypto_price = browser.find_elements(By.XPATH, '//td[@class="Va(m) Ta(start) Px(10px) Fz(s)"]/following-sibling::td/fin-streamer[@data-field="regularMarketPrice"]')
    crypto_list = []
    crypto_price_list = []

    for element in range(len(crypto)):
        toAppend = str(counter) + ". " + crypto[element].text
        crypto_list.append(toAppend)
        crypto_price_list.append(crypto_price[element].text)
        counter += 1

    return crypto_list, crypto_price_list, counter

        
crypto_list, crypto_price_list, counter = extractdata(1)

button = browser.find_element(By.XPATH, '//button[@class="Va(m) H(20px) Bd(0) M(0) P(0) Fz(s) Pstart(10px) O(n):f Fw(500) C($linkColor)"]')
button.click()
time.sleep(1)

crypto_update, crypto_price_update, counter = extractdata(counter)

completelist_crypto = crypto_list + crypto_update
completelist_price = crypto_price_list + crypto_price_update


for element in completelist_crypto:
    print(element)

browser.close()
value = input("Please enter id number of crypto you want today's price of: ")

output = "The value of " + completelist_crypto[int(value)-1] + " today is: $" + completelist_price[int(value)-1] + "CAD"
print(output)