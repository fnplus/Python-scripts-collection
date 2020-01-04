import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",r"C:\Users\Disha Sinha\Downloads")
fp.set_preference("plugin.disable_full_page_plugin_for_types","application/pdf")
fp.set_preference("pdfjs.disabled",True)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")       

driver=webdriver.Firefox(firefox_profile=fp)
driver.get("https://www.allitebooks.in/")

search_ch=1
while search_ch:
    title=driver.title
    search_icon=driver.find_element_by_id("td-header-search-button")
    search_icon.click()
    search_bar=driver.find_element_by_id("td-header-search")
    search_bar.clear()
    search=input("ENTER WHAT TO SEARCH:")
    search_bar.send_keys(search)
    search_bar.send_keys(Keys.RETURN)
    wait(driver, 15).until_not(EC.title_is(title))
    links = [x.get_attribute('href') for x in driver.find_elements_by_xpath("//*[contains(@class, 'td-module-title')]/a")]
    htmls = []
    for link in links:
        driver.get(link)
        htmls.append(driver.page_source)
        down_icon=driver.find_element_by_class_name("td_outlined_btn")
        time.sleep(5)
        download=int(input("Do you want to download this book? press 1 for Yes and 0 for No:"))
        if (download):
            
            down_icon.click()
            try:
                download_icon=driver.find_element_by_id('download')
                download_icon.click()
            except:
                print("PDF version of the book is being downloaded")
            choice=int(input("Do you want to see more books matching your search? Press 1 for YES and 0 for NO:"))
            if not choice:
                links=[]
                break
    search_ch=int(input("Do you want to search again? Press 1 for YES and 0 for NO:"))
    if not search_ch:
        driver.close()
        break
                
            




    





