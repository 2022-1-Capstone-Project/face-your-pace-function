import time
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

import os, sys

def copy_input(xpath, input):
  pyperclip.copy(input)
  driver.find_element_by_xpath(xpath).click()
  ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
  time.sleep(1)


if __name__ == '__main__':
  test_link = sys.argv[1] # get this from terminal
  #test_link = 'https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver'

  driver = webdriver.Chrome('chromedriver.exe')     
  driver.implicitly_wait(3)

  download_link = 'https://soundcloudmp3.org/'
  driver.get(download_link)
  time.sleep(1)

  # 링크 입력
  input_xpath = '//*[@id="conversionForm"]/div/input[2]'
  copy_input(input_xpath, test_link)
  time.sleep(1)

  #다운로드 버튼 누르기
  click_xpath = '//*[@id="conversionForm"]/div/span/button/span'
  driver.find_element_by_xpath(click_xpath).click()
  #driver.find_element(By.XPATH,click_xpath)
  driver.implicitly_wait(600)

  #다운로드 버튼 누르기
  click_xpath = '//*[@id="download-btn"]'
  #driver.find_element_by_xpath(click_xpath).click() #click error
  driver.find_element_by_xpath(click_xpath).send_keys(Keys.ENTER) 
  #time.sleep(1)

  driver.quit()
