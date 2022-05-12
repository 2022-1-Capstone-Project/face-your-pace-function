import time
from selenium import webdriver


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import pyperclip

def copy_input(xpath, input):
    pyperclip.copy(input)
    #driver.find_element_by_xpath(xpath).click()
    driver.find_element(By.XPATH, value = xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()






if __name__ == '__main__':
    test_link = 'https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver' # 이 링크는 사용자가 입력한 링크

    driver = webdriver.Chrome('chromedriver.exe')     
    driver.implicitly_wait(3)

    download_link = 'https://downcloud.cc/'
    driver.get(download_link)
    time.sleep(1)

    # 링크 입력
    input_xpath = '//*[@id="main-url-input"]' #/html/body/div[1]/div[2]/div/div[1]/div/input #full Spath
    copy_input(input_xpath, test_link)
    time.sleep(1)

    #  wav 선택 창
    click_xpath = '/html/body/div[1]/div[2]/div/div[1]/select/option[7]'#'//*[@id="main-format-select-vanilla"]n'
    #driver.find_element_by_xpath(click_xpath).click()
    driver.find_element(By.XPATH, value = click_xpath).click()
    # driver.implicitly_wait(600)
    time.sleep(1)

    # print('download 1')
    # download 클릭 (loading 있음)
    click_xpath = '//*[@id="main-download-button"]'#'/html/body/div[1]/div[2]/div/div[2]/button'
    #driver.find_element_by_xpath(click_xpath).click()
    driver.find_element(By.XPATH, value = click_xpath).click()
    #driver.find_element_by_xpath(click_xpath).send_keys(Keys.ENTER)
    #driver.implicitly_wait(600)
    # print('time sleep start')
    time.sleep(15)
    # print('time sleep end')
    # print('download 1 end')



 
    click_xpath = '/html/body/div[1]/div[5]/div/a[2]'


    element=driver.find_element(By.XPATH, value = click_xpath).click()

    print('download 2 end')