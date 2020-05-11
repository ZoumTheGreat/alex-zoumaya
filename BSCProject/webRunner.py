import sys

import selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\17738\Desktop\chromedriver_win32\chromedriver.exe")
site = input("Enter the URL of the source invoice: ")
driver.get(site)
loginBox = driver.find_element_by_name('ctl00$ctl00$CphFormBody$cphFormBody$txtUserName')
passwordBox = driver.find_element_by_name('ctl00$ctl00$CphFormBody$cphFormBody$txtPassword')
username = input("username: ")
loginBox.send_keys(username)
password = input("password: ")
passwordBox.send_keys(password)
login = driver.find_element_by_name('ctl00$ctl00$CphFormBody$cphFormBody$btn_Login')
login.click()

rows = len(driver.find_elements_by_xpath('//*[@id="ctl00_ctl00_CphFormBody_cphFormBody_bigBilledItems_gvBilledItems"]/tbody/tr'))
# print(rows)
inv = input("input the target invoice number: ")
for x in range(0, rows):
    try:
        edit = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_CphFormBody_cphFormBody_bigBilledItems_gvBilledItems_ctl02_btnEdit"]')
        edit.click()
        changeButton = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_CphFormBody_cphFormBody_jqdBilledItemEditor_ctl01_aInvoiceNumberEdit"]')
        changeButton.click()
        invoiceBox = driver.find_element_by_name('ctl00$ctl00$CphFormBody$cphFormBody$jqdBilledItemEditor$ctl01$ctl05$txtInvoiceNumber')
        invoiceBox.clear()
        invoiceBox.send_keys(inv)
        saveBox = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_CphFormBody_cphFormBody_jqdBilledItemEditor_ctl01_ctl05_ctl01"]/ul/li[1]/a')
        saveBox.click()
    except:
        print("whoops")

