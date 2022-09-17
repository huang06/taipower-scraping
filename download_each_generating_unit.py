import datetime
import logging
import os
import pathlib

# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)

logger.info("Connecting to selenium hub")
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    options=webdriver.FirefoxOptions(),
)

logger.info("Connecting to the page")
cht_url = "https://www.taipower.com.tw/d006/loadGraph/loadGraph/genshx_.html?mid=206&cid=406&cchk=b6134cc6-838c-4bb9-b77a-0b0094afd49d"  # noqa: E501
eng_url = "https://www.taipower.com.tw/d006/loadGraph/loadGraph/genshx_e.html?mid=4484&cid=2834&cchk=20432baa-1f39-4018-aed8-7b33b02f942e"  # noqa: E501
driver.get(cht_url)

datetime_ = datetime.datetime.strptime(
    driver.find_element(By.ID, "datetime").text, "%Y-%m-%d %H:%M"
)  # '2022-09-17 16:40'
print(f"Updated - {datetime_}")

html = driver.page_source

data_dir = pathlib.Path.cwd() / "data" / f"{datetime_:%Y%m%d}"
data_dir.mkdir(parents=True, exist_ok=True)
with open(data_dir / f"{datetime_:%Y%m%d%H%M}.html", "w") as file:
    file.write(html)

# soup = BeautifulSoup(html, "html.parser")
