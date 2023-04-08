from __future__ import annotations

import argparse
import datetime
import logging
import os
import pathlib

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import get_driver

parser = argparse.ArgumentParser()
parser.add_argument("--remote", action="store_true")
args = parser.parse_args()

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)

driver = (
    get_driver(browser="firefox", remote_url="http://127.0.0.1:4444/wd/hub")
    if args.remote
    else get_driver(browser="firefox", remote_url=None)
)
cht_url = "https://www.taipower.com.tw/d006/loadGraph/loadGraph/load_forecast_.html?mid=209&cid=357&cchk=2fd2f12d-f009-43c5-9a41-150e39c214b9"  # noqa: E501
logger.info("Connecting to the page: %s", cht_url)
driver.get(cht_url)
driver.implicitly_wait(5)

try:
    title = driver.title
    logger.info("Page title: %s", title)
    datetime_repr = (
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "datetime"))).text
    )  # '111/09/17'
    logger.info("datetime_repr=%s", datetime_repr)
    year, month, day = datetime_repr.split("/")
    datetime_ = datetime.datetime.strptime(f"{int(year)+1911}-{month}-{day}", "%Y-%m-%d")
    logger.info("Updated - %s", datetime_)

    html = driver.page_source

    data_dir = pathlib.Path(__file__).resolve().parent / "data" / f"{datetime_:%Y%m%d}"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "power_supply_for_the_next_seven_days.html").write_text(html)
except Exception:
    html = driver.page_source
    logger.error("%s", html)
    raise
finally:
    driver.quit()
