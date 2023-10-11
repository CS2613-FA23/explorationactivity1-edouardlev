# Overview of Selenium WebDriver
## By Edouard Levesque

### Selenium WebDriver
### The purpose
Selenium is an open source automated testing framework that can be used to do a plethora of testing. It works in C#, Java, JavaScript, Ruby, Python and PHP. [1](https://www.alphabold.com/selecting-a-programming-language-for-selenium-webdriver/)

 Selenium is a suite of software, each piece being able to do different testing for different needs of whoever uses it. Precisely, WebDriver is a library component of the Selenium suite used for browser automation.  Browser automation is testing software in a web browser with automated solutions. WebDriver can fill out forms, navigate through websites and extract data. This is important for testing and building higher quality software. Manual testing simply does not cut it anymore as there are many browsers that require many tests. Using a testing library like Selenium allows us to redo the tests on multiple browsers and reduce the risk of human errors. [2](https://www.browserstack.com/guide/what-is-browser-automation)
Selenium also works on a variety of browsers, including all the main ones.

### How to use it 
As mentioned in the readme file, you must install it first by running the command: 
```console
 pip3 install selenium
```
Then, in order to interact with a web browser, you must download a web driver. If you're using Safari, you do not need to install anything. For the purpose of this document, let's say you would like to use it with Chrome. You should then install the webdriver from the chromium.org website.

```console
driver = webdriver.Chrome('/Users/MyUsername/Downloads/chromedriver')
```
Like above this is how the driver should be defined in your program.

The browser is then ready to start receiving requests through it's driver. 

```python
driver.get(https://www.browserstack.com)
```
After this code runs, this will result in the launch of the Chrome broswer to the specified website. Now we can get specific elements within the webpage in order to get information. We're also able to fill out forms, click buttons, refresh the page, use the back and next buttons.

By creating a program to test your website or web app with WebDriver, you can then store the scraped data from your website and manipulate it as you would any data. Know that WebDriver does not give test results, so it will not tell you if your test file failed or not. It is up to you to determine wether the test worked or not by seeing if the data you wanted was successfully retrieved. [3](https://www.leapwork.com/blog/what-is-webdriver-in-selenium#what-is-selenium-webdriver)

### Various Functionalities

#### Extracting
The main feature of WebDriver (as mentioned above) is getting information from specific web elements. You can do this by locating an element by name, class name, id name, or XPath. HTML knowledge comes in handy here. You can do so by right clicking on an element in your browser>inspect and copying the highlighted element's XPath. The XPath is usually the more foolproof way of getting the element you want.
![getting xpath](https://ibb.co/nkDwnqR)

```python
crypto = browser.find_elements(By.XPATH, '//td[@class="Va(m) Ta(start) Px(10px) Fz(s)"]')
```

Here we're getting the list of crypto names after getting the xpath of the specific column of names from the website and assigning it to the crypto variable.

#### filling forms: 
send_Keys() enters values into a text box
```python
input_element = driver.find_element_by_name("username")
input_element.send_keys("example_username")
input_element.send_keys(Keys.ENTER)
```
Here we locate the text box "username" on the page and enter "example_username" into it, we then simulate hitting the enter key. 

We can also use .clear() on input_element to remove whatever text has been added into it.

#### Clicking: to simulate a button click on our opened website, we can use the .click feature.

```python
element_with_xpath = driver.find_element_by_xpath("//button[@id='example-button']")
element_with_xpath.click()
```
[4](https://www.digitalocean.com/community/tutorials/selenium-webdriver)

#### screenshot:

WebDriver is capable of taking a screenshot of the open webpage

for example: 

```python
TakesScreenshot scrShot =((TakesScreenshot)webdriver);
File SrcFile=scrShot.getScreenshotAs(OutputType.FILE);
```

The first line converts the web driver object to take a screenshot and the second one instructs it to create a file for it.
[5] https://www.browserstack.com/guide/take-screenshots-in-selenium






