# Web Scraping with Python
This project was created for introduce you to Web Scraping.
The code show how to do web scraping content pages using Selenium
 **Project created just for educational proposes.**
 ## Getting Started
 First choose a browser of your choice. In this example I chose Chrome.
 After that choose a website to do web scraping.
 
 My choice was: [Investing](https://br.investing.com/crypto/)
 ## Prerequisites
  - Python 3.x
  - Some Python libraries
  - Chrome or Mozilla
  - ChromeDriver 
  - GeckoDriver (Mozilla only)
## Installing

### Python libraries:
- **selenium** - An API to write functional/acceptance tests using Selenium WebDriver;
-  **lxml** - Library for processing XML and HTML;
- **pandas** - A great Python Data Analysis Library;
- **requests2** - Requests is the only Non-GMO HTTP library for Python, safe for human consumption;
- **beautfulsoup** - Library for pulling data out of HTML and XML files.

With:
`pip install ..`

### ChromeDriver
[You can find instructions here.](https://chromedriver.chromium.org/getting-started)

### GeckoDriver
[You can find instructions here](https://github.com/mozilla/geckodriver/releases)

##  Tips
- Use `time.sleep ()` for the site to load before the script starts.
- You can use other parameters to find the content on the site:
	- `find_element_by_id`
	- `find_element_by_name`
- You can also search for multiple elements:
    - `find_elements_by_name`
    - `find_elements_by_xpath`
   
  [Documentation here.](https://selenium-python.readthedocs.io/locating-elements.html)
## Author
- **Murilo Carlos** - Inspired by Código Fonte TV