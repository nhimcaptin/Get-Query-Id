from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import concurrent.futures
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import json

# https://web.telegram.org/k/#@TimeFarmCryptoBot
chrome_driver_path = r"E:\Airdrop\Resources\chromedriver-win64\chromedriver.exe"
urlQuery = input("Nhập url con cần lấy query: ")
count = int(input("Nhập số profile: "))
with open('data.txt', 'w', encoding='utf-8') as file:
    pass 
def run_profile(i):
    user_data_dir = rf"C:\Users\doanh.tran\AppData\Local\Google\Chrome\User Data\Profile {i}"
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    # chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--window-size=250,600")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")  

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(urlQuery)

    time.sleep(2)
    driver.refresh()
    time.sleep(5)

    try:
        try:
            button_play = driver.find_element(By.XPATH, '//div[@class="new-message-bot-commands is-view"]//div[@class="new-message-bot-commands-view"]')
            button_play.click()
            print("Đã nhấn nút 'Play'")
            time.sleep(5)
        except Exception as e:
            print(f"Không thấy nút 'Play'")
            
        try:
            button_open_app = driver.find_elements(By.XPATH, '//button[.//span[text()="Open App" or text()="Mở chương trình"]]')
            button_open_app[len(button_open_app) - 1].click()
            print("Đã nhấn nút 'Open App'")
            time.sleep(1)
        except Exception as e:
            print(f"Không thấy nút 'Open App'")
        
        try:
            button_confirm = driver.find_element(By.XPATH, '//button[span[text()="Confirm"]]')
            if button_confirm: 
                button_confirm.click()
                print("Đã nhấn nút 'Confirm'")
                time.sleep(1)
        except Exception as e:
            print(f"Không thấy nút Confirm")
            
        try:
            launch_button = driver.find_element(By.XPATH, "//button[span[text()='Launch']]")
            if launch_button: 
                launch_button.click()
                print("Đã nhấn nút 'Launch'")
                time.sleep(1)
        except Exception as e:
            print(f"Không thấy nút Launch")
        
    except Exception as e:
        print(f"Không thấy nút")

    time.sleep(5)


    try:
        script = """
        const resquest = window.performance.getEntries().find(entry => entry.initiatorType === 'iframe');
        const urlString = resquest.name;
        const decodedQueryId = decodeURIComponent(urlString.split('tgWebAppData=')[1]);
        const urlSplit = decodedQueryId.split('&tgWebAppVersion')[0];
        return urlSplit
        """

        query_id = driver.execute_script(script)
        data_list = []
        with open('data.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data_list.append(line.strip())
                
        with open('data.txt', 'a', encoding='utf-8') as file:
            if len(data_list) > 0:
                file.write(f'\n{query_id}')
            else:
                file.write(f'{query_id}')
    except Exception as e:
        print(f"Error occurred: {e}")
    time.sleep(5)
    driver.quit()

with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:
    executor.map(run_profile, range(1, count + 1))

