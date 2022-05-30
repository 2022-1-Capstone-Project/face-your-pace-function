import time
from selenium import webdriver


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import pyperclip

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager



def copy_input(xpath, input):
    pyperclip.copy(input)
    #driver.find_element_by_xpath(xpath).click()
    driver.find_element(By.XPATH, value = xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

driver = webdriver.Chrome('chromedriver.exe')  
options = webdriver.ChromeOptions()
def download_music_wav(link, download_path):
    global options
    global driver
    # options = webdriver.ChromeOptions()

    # options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\yoondain\Desktop\00학교\4-1'})
    options.add_experimental_option('prefs', {'download.default_directory': download_path})
    test_link = link#'https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver'
    

    driver = webdriver.Chrome('chromedriver.exe',options=options)

    driver.implicitly_wait(3)
    #browser = webdriver.Chrome(options=options)

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
    time.sleep(2)
    #driver.find_element_by_xpath(click_xpath).send_keys(Keys.ENTER)
    #driver.implicitly_wait(600)
    # print('time sleep start')
    # time.sleep(15)
    # print('time sleep end')
    # print('download 1 end')


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



    print('download2')
 
    click_xpath = '/html/body/div[1]/div[5]/div/a[2]'


    driver.find_element(By.XPATH, value = click_xpath).click()

    print('download 2 end')
    time.sleep(360)
    driver.close()
    # time.sleep(10)
    # driver.implicitly_wait(10)
    # while(True):
    # 	pass




if __name__ == '__main__':
    test_link = 'https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver' # 이 링크는 사용자가 입력한 링크

    

    options = webdriver.ChromeOptions()
    # options.add_argument("headless") # 창이 열리지 않은채로
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome('chromedriver.exe',options=options)  

    driver = webdriver.Chrome('chromedriver.exe',options=options)   
       
    driver.implicitly_wait(3)
    #browser = webdriver.Chrome(options=options)

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
    time.sleep(2)
    #driver.find_element_by_xpath(click_xpath).send_keys(Keys.ENTER)
    #driver.implicitly_wait(600)
    # print('time sleep start')
    # time.sleep(15)
    # print('time sleep end')
    # print('download 1 end')


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



    print('download2')
 
    click_xpath = '/html/body/div[1]/div[5]/div/a[2]'


    driver.find_element(By.XPATH, value = click_xpath).click()

    print('download 2 end')
    time.sleep(360)
    # time.sleep(10)
    # driver.implicitly_wait(10)
    # while(True):
    # 	pass