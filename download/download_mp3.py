import time
from selenium import webdriver


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import pyperclip

#from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager






def copy_input(xpath, input):
    pyperclip.copy(input)
    #driver.find_element_by_xpath(xpath).click()
    driver.find_element(By.XPATH, value = xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


def enable_download(driver):
    print('백그라운드 다운로드 기능 활성화')
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': 'C:\\Users\\yoondain\\Downloads'}}
    driver.execute("send_command", params)


    
driver = webdriver.Chrome('chromedriver.exe')  
options = webdriver.ChromeOptions()
def download_music_mp3(link, download_path):
    global options
    global driver
    # options = webdriver.ChromeOptions()

    # options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\yoondain\Desktop\00학교\4-1'})
    options.add_experimental_option('prefs', {'download.default_directory': download_path})
    test_link = link#'https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver'
    

    driver = webdriver.Chrome('chromedriver.exe',options=options)

    # driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')




    # options = webdriver.ChromeOptions()
    # # options.add_argument("headless") # 창이 열리지 않은채로
    
    # # options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # options.add_experimental_option("prefs", {
    # "download.default_directory": 'C:\\Users\\yoondain\\Desktop\\00학교\\4-1',
    # "download.prompt_for_download": False,
    # "download.directory_upgrade": True,
    # "safebrowsing.enabled": True
    # })




    # driver = webdriver.Chrome('chromedriver.exe',options=options)  
    # enable_download(driver)
    # # driver = webdriver.Chrome('chromedriver.exe')  





















    download_link = 'https://soundcloudmp3.org/'
    driver.get(download_link)
    time.sleep(1)

    # 링크 입력
    input_xpath = '//*[@id="conversionForm"]/div/input[2]'
    copy_input(input_xpath, test_link)
    time.sleep(1)

    print('링크입력 끝')
    #다운로드 버튼 누르기 
    print('다운로드1')
    click_xpath = '//*[@id="conversionForm"]/div/span/button/span' #/html/body/div[2]/div[3]/div/div/div[1]/form/div/span/button/i
    #driver.find_element_by_xpath(click_xpath).click()
    print('클릭')
    driver.find_element(By.XPATH, value = click_xpath).click()
    driver.implicitly_wait(600)
    print('다운로드2')

    #다운로드 버튼 누르기
    
    click_xpath = '//*[@id="download-btn"]'
    #driver.find_element_by_xpath(click_xpath).click()
    driver.find_element_by_xpath(click_xpath).send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, value = click_xpath).click()
    print('다운로드2클릭')
    time.sleep(30)
    driver.close()
    
    
    



if __name__ == '__main__':

    
    # driver = webdriver.Chrome('chromedriver.exe')     
    # driver.implicitly_wait(3)

    options = webdriver.ChromeOptions()

    options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\yoondain\Desktop\00학교\4-1'})
    test_link = 'https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver'
    

    driver = webdriver.Chrome('chromedriver.exe',options=options)

    # driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')




    # options = webdriver.ChromeOptions()
    # # options.add_argument("headless") # 창이 열리지 않은채로
    
    # # options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # options.add_experimental_option("prefs", {
    # "download.default_directory": 'C:\\Users\\yoondain\\Desktop\\00학교\\4-1',
    # "download.prompt_for_download": False,
    # "download.directory_upgrade": True,
    # "safebrowsing.enabled": True
    # })




    # driver = webdriver.Chrome('chromedriver.exe',options=options)  
    # enable_download(driver)
    # # driver = webdriver.Chrome('chromedriver.exe')  





















    download_link = 'https://soundcloudmp3.org/'
    driver.get(download_link)
    time.sleep(1)

    # 링크 입력
    input_xpath = '//*[@id="conversionForm"]/div/input[2]'
    copy_input(input_xpath, test_link)
    time.sleep(1)

    print('링크입력 끝')
    #다운로드 버튼 누르기 
    print('다운로드1')
    click_xpath = '//*[@id="conversionForm"]/div/span/button/span' #/html/body/div[2]/div[3]/div/div/div[1]/form/div/span/button/i
    #driver.find_element_by_xpath(click_xpath).click()
    print('클릭')
    driver.find_element(By.XPATH, value = click_xpath).click()
    driver.implicitly_wait(600)
    print('다운로드2')

    #다운로드 버튼 누르기
    
    click_xpath = '//*[@id="download-btn"]'
    #driver.find_element_by_xpath(click_xpath).click()
    driver.find_element_by_xpath(click_xpath).send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, value = click_xpath).click()
    print('다운로드2클릭')
    time.sleep(30)
    driver.close()