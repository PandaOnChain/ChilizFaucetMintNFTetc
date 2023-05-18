from re import A
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #чтобы парсить адреса
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Pool

import time

import undetected_chromedriver as uc
import os


mtmsku: list = open('eth_atom.txt', 'r', encoding='utf-8').read().splitlines()
addresa = []

for i in mtmsku:
    addr = i.split(':')
    addresa.append(addr[0])



def nachalo(adrsy):


    # a = len(addresa)/process_count
    # b = a * adrsy
    # c = b - a
    # d = addresa[c:b]
    indexy = adrsy.split(':')
    global d
    d = addresa[int(indexy[0]):int(indexy[1])]

    opts = uc.ChromeOptions()
    opts.add_argument(f"--load-extension={os.getcwd()}/iproyal")
    global driver
    driver = uc.Chrome(options=opts)
    wait = WebDriverWait(driver, 14)
    driver.get("chrome-extension://kjpmahkhpjoekmlgifomlfeiidebfhbn/pages/options.html")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Get Started')]"))).click()

    driver.find_element_by_xpath("//a[contains(text(), 'Next')]").click()
    driver.find_element_by_xpath("//input[contains(@name, 'profile_name')]").send_keys('TimeToRazYob')
    driver.find_element_by_xpath("//input[contains(@name, 'singleProxy.host')]").send_keys('geo.iproyal.com')
    driver.find_element_by_xpath("//input[contains(@name, 'singleProxy.port')]").send_keys('12323')
    driver.find_element_by_xpath("//input[contains(@name, 'singleProxy.username')]").send_keys('ddbvt')
    driver.find_element_by_xpath("//input[contains(@name, 'singleProxy.password')]").send_keys('9379992_region-asiapacific')
    driver.find_element_by_xpath("//button[contains(text(), 'Save')]").click()
    time.sleep(2)
    driver.get("chrome-extension://kjpmahkhpjoekmlgifomlfeiidebfhbn/pages/options.html")
    time.sleep(5)
    driver.get("https://antcpt.com/score_detector/")
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Refresh')]"))).click()


    time.sleep(5)
    driver.get("https://scoville-faucet.chiliz.com/")

    for i in range(len(d)):
        try:
            get_tokens_chiliz(i)

        except Exception as ex:
            print(ex)
            fileVar = open("Kran_nerobit.txt", "a")
            fileVar.write(d[i] + '\n')
            fileVar.close()

    driver.quit()



def get_tokens_chiliz(i):
    driver.find_element_by_xpath("//input[contains(@class, 'form-control')]").clear()
    driver.find_element_by_xpath("//input[contains(@class, 'form-control')]").send_keys(d[i])

    driver.find_element_by_xpath("//button[contains(text(), 'Fan Tokens')]").click()
    driver.find_element_by_xpath("//*[text()[contains(.,'Paris')]]").click()


    # driver.find_element_by_xpath("//button[contains(text(), 'Give me CHZ')]").click()
    # driver.find_element_by_xpath("//*[text()[contains(.,'6.25')]]").click()#/html/body/div[1]/div[4]/div/div[1]/span[1]/ul/li[3]/a
    wait = WebDriverWait(driver, 14)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()[contains(.,'Funding request accepted')]]")))

    time.sleep(5.5)


if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    p = Pool(processes=process_count)

    prcnt = []
    a = len(addresa)/process_count

    for i in range(process_count):
        b = int(a * (i+1))
        c = int(b - a)
        g = str(c) + ":" + str(b)
        prcnt.append(str(g))
    print(prcnt)

    p.map(nachalo, prcnt)
