from seleniumwire import webdriver #https://pypi.org/project/selenium-wire/#proxies  для проксей, пизже решения нет
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #чтобы парсить адреса
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from multiprocessing import Pool

import undetected_chromedriver as uc

mtmsku: list = open('empty_nft5z.txt', 'r', encoding='utf-8').read().splitlines()

addres = []


for i in range(len(mtmsku)):
    addr = mtmsku[i].split(':')
    addres.append(addr[0])
# addresa = addres[50:]
addresa = addres

pswrd = "SobakaAwAw"


def poshla_zhara(adrs):
    try:
        chop = webdriver.ChromeOptions()
        chop.add_extension("metamask-chrome-10.6.4.crx")
        chop.add_argument('--lang=en')
        #отключение режима WebDriver
        chop.add_argument("--disable-blink-features=AutomationControlled")
        chop.add_argument(r"user-data-dir=C:\Users\chillz\profiles\\"+adrs)
        global driver
        driver = webdriver.Chrome(chrome_options=chop)
        global wait
        wait = WebDriverWait(driver, 14)
        driver.implicitly_wait(10)
        global handle
        handle = driver.window_handles
        driver.switch_to.window(handle[0])
        unlock = driver.find_element_by_xpath("//*[contains(@class,'button')]").text
        if unlock == "Unlock":
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'password')]"))).send_keys("SobakaAwAw")
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'button')]"))).click()
        driver.get("https://scoville-nft.chiliz.com/")
        time.sleep(3)
        handle = driver.window_handles
        if len(handle) != 2:
            driver.switch_to.window(handle[2])
            try:
                approve = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]').text
            except:
                approve = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]').text
            if approve == "Next":
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Next')]"))).click()
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Connect')]"))).click()
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Approve')]"))).click()
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Switch')]"))).click()
            elif approve == "Switch network":
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Switch')]"))).click()
            else:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Approve')]"))).click()
                wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Switch')]"))).click()
            driver.switch_to.window(handle[0])
            
            try:
                asd = driver.find_element_by_xpath("//*[contains(@class,'MuiGrid-root MuiGrid-item css-1wxaqej')]").text
                if asd == 'Transaction signature has been denied by the user!':
                    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'MuiButton-contained MuiButton-containedError')]"))).click()
                    mint_NFT()
                else:
                    mint_NFT()
            except:
                mint_NFT()
            
           
        else:
            mint_NFT()
        # while len(handle) != 3: #потом создать функцию для ожидания popup metamask
        #     time.sleep(0.5)
        #     handle = driver.window_handles
        # driver.switch_to.window(handle[2])
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()[contains(.,'Connect With MetaMask')]]")))
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()[contains(.,'Next')]]"))).click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@data-testid,'page-container-footer-next')]"))).click()
        # driver.switch_to.window(handle[0])
        
        
        


    except Exception as ex:
        print(ex)  
        fileVar = open("nerobit.txt", "a")
        fileVar.write(adrs + '\n' + ex + '\n\n')
        fileVar.close()  
    finally:    
        driver.close()
        driver.quit()


def mint_NFT():
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'MuiButton-contained MuiButton-containedError')]"))).click() #1st NFT
    # Transaction signature has been denied<div class="MuiGrid-root MuiGrid-item css-1wxaqej">Transaction signature has been denied by the user!</div>
     # wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'MuiButton-contained MuiButton-containedError')]"))).click()
    buy_nft() ###1
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@aria-haspopup,'listbox')]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()[contains(.,'CHZ - A New Era 2/5')]]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'MuiButton-contained MuiButton-containedError')]"))).click() #2nd NFT
    buy_nft() ###2
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@aria-haspopup,'listbox')]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()[contains(.,'CHZ - A New Era 3/5')]]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'MuiButton-contained MuiButton-containedError')]"))).click() #3rd NFT
    buy_nft() ###3
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@aria-haspopup,'listbox')]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()[contains(.,'CHZ - A New Era 4/5')]]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'MuiButton-contained MuiButton-containedError')]"))).click() #4rd NFT
    buy_nft() ###4
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@aria-haspopup,'listbox')]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()[contains(.,'CHZ - A New Era 5/5')]]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'MuiButton-contained MuiButton-containedError')]"))).click() #5th NFT
    buy_nft() ###5
    time.sleep(5)

def buy_nft():
    handle = driver.window_handles
    while len(handle) != 3: #потом создать функцию для ожидания popup metamask
        time.sleep(0.5)
        handle = driver.window_handles
    driver.switch_to.window(handle[2])
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()[contains(.,'Confirm')]]"))).click()
    driver.switch_to.window(handle[0])
    

if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    p = Pool(processes=process_count)
    p.map(poshla_zhara, addresa)
    print("Успех!!! не плакай!")
