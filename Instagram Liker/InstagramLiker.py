from selenium import webdriver
from time import sleep
import sys
import os
import getpass

path = os.path.join(sys.path[0], 'chromedriver.exe')

choice = int(input("Enter 1 for facebook log in 2 for email login : "))
email = input("Enter the email : ")
password = getpass.getpass('Password:')
tags = input("Enter the tag you want to search for : (saperate the tags by a ',')").split(",")
limit = int(input("Enter how many pictures you want to like?"))
time = (len(tags) * limit * 5) + 6
print("It will take approximately ",time,"seconds to run!")
sleep(2)
driver = webdriver.Chrome(path)
url1 = "https://www.instagram.com"
driver.set_page_load_timeout(50)
driver.get(url1)
if (choice == 1):
    # statements for facebook login
    driver.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[1]/button").click()
    sleep(2)
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_name("login").click()
elif(choice == 2):
    # statements for email login
    driver.find_element_by_xpath("//section/main/article/div[2]/div[2]/p/a").click()
    sleep(5)
    driver.find_element_by_name("username").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[3]/button").click()   


ListofElements = []
sleep(3)
for tag in tags:

    url = "https://www.instagram.com/explore/tags/"+tag+"/"

    driver.get(url)
    #write code for the like part here!
    driver.find_element_by_xpath("//section/main/article/div[1]/div/div/div[1]/div[1]").click()
    sleep(1)
    #clicking the first like 
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]').click()
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/a").click()
    sleep(2)
    i = 0
    while(i < limit-1):
        btn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
        print(btn)
        label = btn.get_attribute("aria-label")
        print(label)
        if(label == "Like"):
            print("Here")
            i = i+1
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
            sleep(3)
        else:
            print("over here")
            i = i - 1
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/a[2]").click()
            sleep(2)
            continue
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/a[2]").click()
        sleep(2)
driver.quit()
