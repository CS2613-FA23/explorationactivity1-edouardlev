[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# ExplorationActivity1
### Which library my sample program demonstrates

My sample program demonstrates the use of web scraping (computer getting information from websites by itself) using the [Selenium](https://www.browserstack.com/selenium) library. This is a library that is used for browser automation and testing websites. 

### How to run my sample program

My sample program must be run on MacOS as that is how my program is set up. Precisely, the WebDriver import of selenium requires one specific browser driver for a program. I used Safari for my program as that is the only browser that does not require downloads for use.

To install selenium on your (Python having) machine, open your command terminal and type in
```console
 pip3 install selenium
```


 To set up your Safari browser to run this program, click on 
 Safari>Settings...>Advanced>check 'Show Develop menu in menu bar'. Then from the menu bar click allow remote automation. 

 Now the program should be ready to be run just like any other Python program. Change directory to where the program is stored and type in

```console
python3 cryptoPriceCheck.py
```

### The purpose of my program

My program scrapes the Yahoo! Finance website for a list of the top 50 cryptocurrencies and then prompts the user for which current price they would like to see. I believe that this program would be useful for people who own the currency or are just interested and want to check the price of any top crypto. This program also adjusts with Yahoo's list of top crypto, so the program will not need to be adjusted if any particular currency goes under.

### Input and output examples

After running the programs, you should see the list of scraped currencies from the Yahoo website. 