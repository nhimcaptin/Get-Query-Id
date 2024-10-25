import time
from selenium.webdriver.common.by import By
import urllib.parse
import re

chrome_driver_path = r"E:\Airdrop\Resources\chromedriver-win64\chromedriver.exe"


def getUserDataDir(index):
    return rf"C:\Users\doanh.tran\AppData\Local\Google\Chrome\User Data\Profile {index}"


def action_play_game(driver):
    try:
        try:
            button_play = driver.find_element(
                By.XPATH,
                '//div[@class="new-message-bot-commands is-view"]//div[@class="new-message-bot-commands-view"]',
            )
            button_play.click()
            print("Đã nhấn nút 'Play'")
            time.sleep(5)
        except Exception as e:
            print(f"Không thấy nút 'Play'")

        try:
            button_open_app = driver.find_elements(
                By.XPATH,
                '//button[.//span[text()="Open App" or text()="Mở chương trình"]]',
            )
            button_open_app[len(button_open_app) - 1].click()
            print("Đã nhấn nút 'Open App'")
            time.sleep(1)
        except Exception as e:
            print(f"Không thấy nút 'Open App'")

        try:
            button_confirm = driver.find_element(
                By.XPATH, '//button[span[text()="Confirm"]]'
            )
            if button_confirm:
                button_confirm.click()
                print("Đã nhấn nút 'Confirm'")
                time.sleep(1)
        except Exception as e:
            print(f"Không thấy nút Confirm")

        try:
            launch_button = driver.find_element(
                By.XPATH, "//button[span[text()='Launch']]"
            )
            if launch_button:
                launch_button.click()
                print("Đã nhấn nút 'Launch'")
                time.sleep(1)
        except Exception as e:
            print(f"Không thấy nút Launch")

    except Exception as e:
        print(f"Không thấy nút")


def sort_data_by_user_id():
    with open("file_user_ids.txt", "r", encoding="utf-8") as f:
        user_ids = f.read().splitlines()

    with open("data.txt", "r", encoding="utf-8") as f:
        query_data = f.read().splitlines()

    decoded_queries = [urllib.parse.unquote(query) for query in query_data]

    query_dict = {}
    for index, query in enumerate(decoded_queries):
        user_id_match = re.search(r'"id":(\d+)', query)
        if user_id_match:
            user_id = int(user_id_match.group(1))
            query_dict[user_id] = query_data[index]

    sorted_queries = [
        query_dict[int(user_id)] for user_id in user_ids if int(user_id) in query_dict
    ]

    sorted_data_queries = "\n".join(sorted_queries)

    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(sorted_data_queries)
