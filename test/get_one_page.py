import json

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

table = driver.find_element(By.CSS_SELECTOR, "table.tbl.default.brd1")
rows = table.find_elements111(By.CSS_SELECTOR, "tr")

data_list = []
for idx, row in enumerate(rows):
    try:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) < 4:
            print(f"[{idx}] 컬럼이 부족하여 건너뜀")
            continue

        doc_num = cols[0].text.strip()
        title = cols[1].text.strip()
        dept = cols[2].text.strip()
        date = cols[3].text.strip()

        print(f"[{idx}] 번호 {doc_num}, 상세 페이지 이동 중")

        title_link = cols[1].find_element(By.TAG_NAME,"a")
        title_link.click()
        time.sleep(2)

        contents = driver.find_elements(By.CSS_SELECTOR, ".b_cont")
        full_text = "\n\n".join([c.text.strip() for c in contents])

        item = {
            "num" : doc_num, "title" : title, "dept" : dept, "date" : date, "contect" : full_text
        }
        data_list.append(item)

        print(f"[{idx}] 저장 완료 -> 목록 복귀")
        driver.back()
        time.sleep(2)

        table = driver.find_element(By.CSS_SELECTOR, "table.tb1.default.drd1")
        rows = table.find_elements((By.TAG_NAME), "tr")
    except Exception as e:
        print(f"[{idx}] 에러 발생 {e}")

with open("epeople_articles.json", "w", encoding="utf-8") as f:
    json.dump(data_list, f, ensure_ascii=False, indent=2)


driver.quit()
print(f"\n총 {len(data_list)}건 저장 완료")

