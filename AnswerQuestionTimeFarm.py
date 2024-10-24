from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import concurrent.futures
from utils import action_play_game, getUserDataDir, chrome_driver_path

countProject = int(input("Nhập số profile: "))
numberThreads = int(input("Nhập số luồng: "))


def run_profile(i):
    user_data_dir = getUserDataDir(i)
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    chrome_options.add_argument("--window-size=250,600")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    time.sleep(1)
    driver.get("https://web.telegram.org/k/#@TimeFarmCryptoBot")
    time.sleep(2)
    driver.refresh()
    time.sleep(5)
    action_play_game(driver)
    time.sleep(10)

    try:
        # Chuyển sang iframe chứa tab
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        earn_tab = driver.find_element(
            By.XPATH, '//div[@class="tab"]//div[@class="tab-title" and (text()="Earn" or text()="Kiếm")]'
        )
        earn_tab.click()
        time.sleep(1)
        oracle_card = driver.find_element(By.XPATH, '//div[@class="earn-card"]//div[@class="title" and (text()="Oracle of Time" or text()="Lời tiên tri của thời gian")]')
        oracle_card.click()
        time.sleep(1)
        date_input = driver.find_element(By.ID, "datepicker")
        date_value = "16-10-2017"  
        date_input.send_keys(date_value)
        time.sleep(1)
        check_date_button = driver.find_element(By.XPATH, '//div[@class="button-component common btn"]//div[text()="Check the date" or text()="Kiểm tra ngày"]')
        check_date_button.click()
        time.sleep(5)
        claim_button = driver.find_element(By.XPATH, '//div[@class="button-component common btn"]//div[contains(text(), "Claim") or contains(text(), "Yêu cầu")]')
        claim_button.click()
        print("Đã click vào tab 'Earn'")
    except Exception as e:
        print(f"Không thể click vào tab 'Earn': {e}")

    # try:
    #     button_play = driver.find_element(By.XPATH, '//div[@class="new-message-bot-commands is-view"]//div[@class="new-message-bot-commands-view"]')
    #     button_play.click()
    #     print("Đã nhấn nút 'Play'")
    #     time.sleep(5)
    # except Exception as e:
    #     print(f"Không thấy nút 'Play'")

    time.sleep(5)
    # input("")
    driver.quit()


with concurrent.futures.ThreadPoolExecutor(max_workers=numberThreads) as executor:
    executor.map(run_profile, range(6, countProject + 1))
