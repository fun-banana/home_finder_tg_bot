from datetime import datetime
from typing import List, Optional
import time


import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

from schemas import ListingDTO


class Yad2Parser:
    BASE_URL = "https://www.yad2.co.il/realestate/rent/center-and-sharon"

    HEADERS = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
        "origin": "https://www.yad2.co.il",
        "referer": "https://www.yad2.chttps://www.yad2.co.il/realestate/rent/center-and-sharon?minPrice=1000&minRooms=3&maxRooms=4&area=9&city=8300&bBox=31.831802%2C34.730162%2C32.119823%2C34.846166&zoom=11o.il/realestate/rent",
        "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }

    async def fetch_feed(self,
        city_code: Optional[int] = None,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        min_rooms: Optional[float] = None,
        max_rooms: Optional[float] = None,
        ) -> List[ListingDTO]:
            params = {
                    "page": 1,
                    "sort": "date",
                }
            if city_code:
                params["city"] = city_code
            if min_price:
                params["minPrice"] = min_price
            if max_price:
                params["maxPrice"] = max_price
            if min_rooms:
                params["minRooms"] = min_rooms
            if max_rooms:
                params["maxRooms"] = max_rooms
            
            results: List[ListingDTO] = []
            
            options = Options()
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome()
            stealth(driver, 
                    platform='Win32',
                    languages='he-IL')
            
            driver.get(self.BASE_URL)
            time.sleep(20)
            
            

            
            return results

if __name__ == "__main__":
    async def main():
        parser = Yad2Parser()
        print("Запрашиваем свежие квартиры с Yad2...")
        listings = await parser.fetch_feed(min_price=3000, max_price=6000, city_code=8300, min_rooms=3, max_rooms=4)

    asyncio.run(main())