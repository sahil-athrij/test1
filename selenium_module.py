# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests,bs4,time
from selenium import webdriver

    
def main():
    
    driver = webdriver.Chrome()
    driver.get("http://results.cusat.ac.in/regforms/regno1.php")
    regno = driver.find_element_by_name("rno")
    regno.clear()
    button = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/input")
    regno.send_keys('12180021')
    button.click()
    print(driver.page_source)
    driver.back()
    regno = driver.find_element_by_name("rno")
    regno.clear()
main()

input()
