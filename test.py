import time
from seleniumbase import SB

BASE_URL = "https://www.yad2.co.il/realestate/rent/center-and-sharon"

with SB(uc=True, test=False, locale_code='he') as sb:
    sb.driver.execute_cdp_cmd("Network.setUserAgentOverride", {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    })
    

    print("Подключение к Yad2...")
    # 2. Обход TLS-защиты при открытии страницы
    sb.driver.uc_open_with_reconnect(BASE_URL, reconnect_time=6)
    
    # Даем странице полностью загрузиться (загрузка скриптов Kasada)
    time.sleep(5)
    
    
 