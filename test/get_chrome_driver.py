from certifi import contents
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#실행이 매번 느린 경우에는
# driver_path = "C:\Users\108-0\.wdm\drivers\chromedriver\win64\137.0.7151.68\chromedriver-win32\chromedriver.exe"
# service = Service(driver_path)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.epeople.go.kr/nep/prpsl/opnPrpl/opnpblPrpslList.npaid")
print(driver.title)

import time
time.sleep(3)

row = driver.find_element(By.CSS_SELECTOR, "tbody tr")
cols = row.find_elements(By.TAG_NAME, "td")

doc_num = cols[0].text.strip()
title = cols[1].text.strip()
dept = cols[2].text.strip()
date = cols[3].text.strip()

print("번호 : ", doc_num)
print("제목 : ", title)
print("처리 기관 : ", dept)
print("날짜 : ", date)

title_link = cols[1].find_element(By.TAG_NAME,"a")
title_link.click()

time.sleep(2)
contents = driver.find_elements(By.CSS_SELECTOR, ".b_cont")
full_text = "\n\n".join([c.text.strip() for c in contents])

print("본문 : ", full_text)
driver.quit()
