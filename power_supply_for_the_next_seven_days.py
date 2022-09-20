import datetime
import logging
import os
import pathlib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

try:
    logger.info("Connecting to the page")
    cht_url = "https://www.taipower.com.tw/d006/loadGraph/loadGraph/load_forecast_.html?mid=209&cid=357&cchk=2fd2f12d-f009-43c5-9a41-150e39c214b9"  # noqa: E501
    driver.get(cht_url)
    driver.implicitly_wait(5)

    datetime_repr = (
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "datetime"))).text
    )  # '111/09/17'
    logger.info(f"{datetime_repr=}")
    year, month, day = datetime_repr.split("/")
    datetime_ = datetime.datetime.strptime(f"{int(year)+1911}-{month}-{day}", "%Y-%m-%d")
    logger.info("Updated - %s", datetime_)

    html = driver.page_source

    data_dir = pathlib.Path.cwd() / "data" / f"{datetime_:%Y%m%d}"
    data_dir.mkdir(parents=True, exist_ok=True)
    with open(data_dir / "power_supply_for_the_next_seven_days.html", "w") as file:
        file.write(html)
finally:
    driver.quit()
