import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Navigate to website content
url = "https://br.investing.com/crypto/"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

driver.find_element_by_xpath("//div//table[@class='genTbl js-top-crypto-table mostActiveStockTbl crossRatesTbl allCryptoTlb wideTbl elpTbl elp15 ']//thead//tr//th[@class='left elp name first pointer']//span[@class='headerSortDefault']").click()

target = driver.find_element_by_xpath("//div//table[@class='genTbl js-top-crypto-table mostActiveStockTbl crossRatesTbl allCryptoTlb wideTbl elpTbl elp15 ']")
html_content = target.get_attribute('outerHTML')

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# Structure the data
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Nome', 'Código', 'Preço (USD)', 'Var (24h)']]
df.columns = ['Nome', 'Sigla', 'Dólares', '24h']

print(df)

time.sleep(5)
driver.quit()