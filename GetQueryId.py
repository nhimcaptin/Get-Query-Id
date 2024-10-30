from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import concurrent.futures
from utils import (
    action_play_game,
    getUserDataDir,
    chrome_driver_path,
    sort_data_by_user_id,
)
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import json


urlQuery = input("Nhập url con cần lấy query: ")
countProject = int(input("Nhập số profile: "))
numberThreads = int(input("Nhập số luồng: "))
sort_choice = input("Bạn có muốn thực hiện sort không? (y/n): ")
proxy = []

with open("data.txt", "w", encoding="utf-8") as file:
    pass
with open("proxy.txt", "r", encoding="utf-8") as file:
    for line in file:
        proxy.append(line.strip())


def run_profile(i):
    user_data_dir = getUserDataDir(i)
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    if len(proxy) > 0:
        chrome_options.add_argument(f"--proxy-server=http://{proxy[i-1]}")
    chrome_options.add_argument("--window-size=250,600")
    # chrome_options.add_argument("--disable-web-security")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    time.sleep(1)
    driver.get(urlQuery)
    time.sleep(2)
    driver.refresh()
    time.sleep(5)

    action_play_game(driver)

    time.sleep(15)

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
        with open("data.txt", "r", encoding="utf-8") as file:
            for line in file:
                data_list.append(line.strip())

        with open("data.txt", "a", encoding="utf-8") as file:
            if len(data_list) > 0:
                file.write(f"\n{query_id}")
            else:
                file.write(f"{query_id}")
    except Exception as e:
        print(f"Error occurred: {e}")
    time.sleep(5)
    driver.quit()


with concurrent.futures.ThreadPoolExecutor(max_workers=numberThreads) as executor:
    executor.map(run_profile, range(1, countProject + 1))

if sort_choice.lower() == "y":
    sort_data_by_user_id()
