#библиотеки
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #чтобы парсить адреса
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
#для прокрутки
from selenium.webdriver.common.action_chains import ActionChains
import time
from multiprocessing import Pool

import undetected_chromedriver as uc

from web3 import Web3
from json import loads

from random import randint


#кошельки, где меньше 2 чиллизов
mtmsku: list = open('./deleg/0bole1.txt', 'r', encoding='utf-8').read().splitlines()
addres = []

for wallet in mtmsku:
    addres.append(wallet)#.split(':')[0])

pswrd = "##"


#выбираем кошельки и запускаем кликер
def main1():
    #poshla_zhara(addres[22])
    for adrs in addres:
        poshla_zhara(adrs)



def poshla_zhara(adrs):
    #выводим номер и сам кошелёк 
    print(addres.index(adrs))
    print(adrs)
    #подключаем вебдрайвер со всеми опциями и нужным профилем
    chop = webdriver.ChromeOptions()
    chop.add_argument('--lang=en')
    chop.add_argument(r"user-data-dir=C:\Users\chillz\profiles\\"+adrs)
    chop.add_argument("--disable-blink-features=AutomationControlled")
    chop.add_extension("metamask-chrome-10.6.4.crx")

    global driver
    driver = webdriver.Chrome(chrome_options=chop)
    #ожидание
    global wait
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    #переключение вкладок
    global handle
    handle = driver.window_handles
    driver.switch_to.window(handle[0])
    #проверка на наличие кошелька в метамаске
    unlock = driver.find_element_by_xpath("//*[contains(@class,'button')]").text
    if unlock == "Unlock":
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'password')]"))).send_keys("SobakaAwAw")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'button')]"))).click()

    #запуск тестнета
    driver.get("https://scoville-governance.chiliz.com/staking")
    #подключение кошелька к сайту, режект транзакций(хз работает или нет)
    ChckCnnctWllt()
    #отправка на стейкинг 1)клик на чела 2)ввод кол-ва токенов  3)отправка
    DBVT1()
    driver.close()
    driver.quit()


def ChckCnnctWllt():
    try:
        #переход на страницу кошелька
        driver.switch_to.window(driver.window_handles[1])
        driver.get("chrome-extension://dkhpanfopmlnehhnibfobghhkpebfbni/popup.html")
        try:
            #прожим кнопок next, connect
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Next')]"))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Connect')]"))).click()
            #пытаюсь найти кнопку reject и прожать
            try:
                reject = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[1]').text
                if reject == 'Reject':
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[1]'))).click()
            except:
                pass
        except:
            #если кнопки next нет, то попытка найти кнопку reject
            print("Probuyu reject")
            try:                                
                if driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[1]').text == "Reject":
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[1]'))).click()
                else:
                    pass
            except:
                print("PZDC NHY BLT Connect kshka ne proshel IlI da")
                pass
        driver.switch_to.window(driver.window_handles[0])
        print('jdeme dal dbvt')
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mouse-parallax-container"]/section/section/section/div/article/div[1]/button'))).click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/aside/section/ul/li/button/span'))).click()
    except:
        print('jdeme dal popal v except')
        pass


def DBVT1(): 
    #prokrutka vniz
    try:
        #прокрутка на 8 валидатора
        target = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/section/main/div[3]/div/div/div/div/div/table/tbody/tr[7]/td[8]/div/button')))
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()
    except:
        time.sleep(5)
        target = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/section/main/div[3]/div/div/div/div/div/table/tbody/tr[7]/td[8]/div/button')))
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()
    
    #выбор валидатора 1                                    //*[@id="root"]/section/section/main/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[8]/div/button/span         
    try:
        print('try')
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/section/main/div[3]/div/div/div/div/div/table/tbody/tr[7]/td[8]/div/button'))).click()
        #ввод количества токенов                                /html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/div/div/input
        print('jdem 5sec pered vvodom')                         #/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/div/div/input
        time.sleep(5)
        actions.move_to_element(wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/div/div/input'))))
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/div/div/input'))).send_keys("1")
        #submit                                                 /html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]
        actions.move_to_element(wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]'))))
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]'))).click()
        print('go to gaslim')
        gaslim()
    except:
        print('except')
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/section/main/div[3]/div/div/div/div/div/table/tbody/tr[6]/td[8]/div/button/span'))).click()
        #ввод количества токенов                                /html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/div/div/input
        print('jdem 5sec pered vvodom')                         
        time.sleep(3)
        # actions.move_to_element(wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/div/div/input'))))
        # actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/div/div/input'))).send_keys('1')#(str(randint(1,3)))
        #submit                                                 /html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]
        actions.move_to_element(wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]'))))
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]'))).click()
        print('go to gaslim')
        gaslim()

def gaslim():
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.refresh()
    #ждем пока прогрузится
    time.sleep(7)
    try:
        print(1.1)                                                     #/html/body/div/section/section/main/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[8]/div/button/span
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[2]/div/div/div/div[1]/button'))).click()
        print(1.2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popover-content"]/div/div/section/div/div/div[2]/div[1]/button'))).click()
        try:
            print(1.3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popover-content"]/div/div/section/div/div/div[2]/div[1]/div[2]/div[2]/label/div[2]/input'))).send_keys(Keys.CONTROL + "a")
            print(1.4)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popover-content"]/div/div/section/div/div/div[2]/div[1]/div[2]/div[2]/label/div[2]/input'))).send_keys(Keys.DELETE)
        except:
            print(1.13)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popover-content"]/div/div/section/div/div/div[2]/div[1]/div[3]/div[2]/label/div[2]/input'))).send_keys(Keys.CONTROL + "a")
            print(1.14)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popover-content"]/div/div/section/div/div/div[2]/div[1]/div[3]/div[2]/label/div[2]/input'))).send_keys(Keys.DELETE)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popover-content"]/div/div/section/div/div/div[2]/div[1]/div[2]/div[2]/label/div[2]/input'))).send_keys("10")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Save')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[2]'))).click()
        #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popover-content"]/div/div/section/footer/button'))).click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()[contains(.,'Transaction executed')]]")))
        except:
            pass
    except:
        print("reject all transactions")
        #reject all
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[4]/div/a'))).click()
        #podtverjdeniye
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-content"]/div/span/div[1]/div/div/div[3]/button[2]'))).click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[4]/div/a'))).click()
        # print(2)
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-content"]/div/span/div[1]/div/div/div[3]/button[2]'))).click()
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        DBVT1()
        
        



#начало 
if __name__ == "__main__":
    main1()
