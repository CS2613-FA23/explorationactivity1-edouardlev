from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Safari()

browser.get('https://ca.finance.yahoo.com/crypto/')

crypto = browser.find_elements(By.XPATH, '//td[@class="Va(m) Ta(start) Px(10px) Fz(s)"]')
crypto_list = []
counter = 1
for element in range(len(crypto)):
    toAppend = str(counter) + ". " + crypto[element].text
    crypto_list.append(toAppend)
    counter += 1

crypto_price = browser.find_elements(By.XPATH, '//td[@class="Va(m) Ta(start) Px(10px) Fz(s)"]/following-sibling::td/fin-streamer[@data-field="regularMarketPrice"]')

crypto_price_list = []
counter = 1
for element in range(len(crypto_price)):
    crypto_price_list.append(crypto_price[element].text)
    counter += 1

button = browser.find_element(By.ID, "Va(m) H(20px) Bd(0) M(0) P(0) Fz(s) Pstart(10px) O(n):f Fw(500) C($linkColor)")
button.click()



for element in crypto_list:
    print(element)

browser.close()
value = input("Please enter id number of crypto you want today's price of: ")

output = "The value of " + crypto_list[int(value)-1] + " today is: $" + crypto_price_list[int(value)-1] + "CAD"
print(output)