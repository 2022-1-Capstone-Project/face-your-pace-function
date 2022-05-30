import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pyperclip




def copy_input(xpath, input, driver):
    pyperclip.copy(input)
    #driver.find_element_by_xpath(xpath).click()
    driver.find_element(By.XPATH, value = xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() # WINDOWS
    # ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform() # MAC


def download_music_wav(link, download_path):
    test_link = link 

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'download.default_directory': download_path})
    
    driver = webdriver.Chrome('chromedriver.exe',options=options)

    driver.implicitly_wait(3)

    download_link = 'https://downcloud.cc/'
    driver.get(download_link)
    time.sleep(1)

    # 링크 입력
    input_xpath = '//*[@id="main-url-input"]' #/html/body/div[1]/div[2]/div/div[1]/div/input #full Spath
    copy_input(input_xpath, test_link, driver)
    time.sleep(1)

    #  wav 선택 창
    click_xpath = '/html/body/div[1]/div[2]/div/div[1]/select/option[7]'#'//*[@id="main-format-select-vanilla"]n'
    #driver.find_element_by_xpath(click_xpath).click()
    driver.find_element(By.XPATH, value = click_xpath).click()
    # driver.implicitly_wait(600)
    time.sleep(1)

    click_xpath = '//*[@id="main-download-button"]'#'/html/body/div[1]/div[2]/div/div[2]/button'
    #driver.find_element_by_xpath(click_xpath).click()
    driver.find_element(By.XPATH, value = click_xpath).click()
    time.sleep(2)

    st = time.time()

    path = '/html/body/div[1]/div[5]/div/div/div[1]/p[2]'#'//*[@id="1652370417155"]/div/div[1]/p[2]'

    while(True):
        
        #print(1)
        temperature_xpath=driver.find_element(By.XPATH, value = path)
        #print(2)
        #print(type(temperature_xpath))
        temperature = temperature_xpath.text 
        #print(3)
        #print(temperature, end = '  ')
        if temperature == '100%': break



    end = time.time()
    print(end-st)

    time.sleep(7)



    # print('download2')
 
    click_xpath = '/html/body/div[1]/div[5]/div/a[2]'


    driver.find_element(By.XPATH, value = click_xpath).click()

    # print('download 2 end')
    time.sleep(360) # 다운받는 시간
    driver.close()


def download_music_mp3(link, download_path):
    test_link = link 
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'download.default_directory': download_path})
    driver = webdriver.Chrome('chromedriver.exe',options=options)

    # 링크열기
    download_link = 'https://soundcloudmp3.org/'
    driver.get(download_link)
    time.sleep(1)

    # 링크 입력
    input_xpath = '//*[@id="conversionForm"]/div/input[2]'
    copy_input(input_xpath, test_link,driver)
    time.sleep(1)

    #다운로드 버튼 누르기 
    click_xpath = '//*[@id="conversionForm"]/div/span/button/span' #/html/body/div[2]/div[3]/div/div/div[1]/form/div/span/button/i
    #driver.find_element_by_xpath(click_xpath).click()
    driver.find_element(By.XPATH, value = click_xpath).click()
    driver.implicitly_wait(600)

    #다운로드(하는) 버튼 누르기
    click_xpath = '//*[@id="download-btn"]'
    #driver.find_element_by_xpath(click_xpath).click()
    driver.find_element_by_xpath(click_xpath).send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, value = click_xpath).click()
    time.sleep(30)
    driver.close()
