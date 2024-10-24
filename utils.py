import time
from selenium.webdriver.common.by import By

chrome_driver_path = r"E:\Airdrop\Resources\chromedriver-win64\chromedriver.exe"

def getUserDataDir(index):
    return rf"C:\Users\doanh.tran\AppData\Local\Google\Chrome\User Data\Profile {index}"
    
def action_play_game(driver):
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