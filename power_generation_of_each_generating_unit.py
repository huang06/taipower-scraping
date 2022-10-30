from __future__ import annotations

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
    cht_url = "https://www.taipower.com.tw/d006/loadGraph/loadGraph/genshx_.html?mid=206&cid=406&cchk=b6134cc6-838c-4bb9-b77a-0b0094afd49d"  # noqa: E501
    eng_url = "https://www.taipower.com.tw/d006/loadGraph/loadGraph/genshx_e.html?mid=4484&cid=2834&cchk=20432baa-1f39-4018-aed8-7b33b02f942e"  # noqa: E501
    driver.get(cht_url)
    driver.implicitly_wait(5)

    datetime_repr = (
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "datetime"))).text
    )  # '2022-09-17 16:40'
    logger.info("datetime_repr=%s", datetime_repr)
    datetime_ = datetime.datetime.strptime(datetime_repr, "%Y-%m-%d %H:%M")
    logger.info("Updated - %s", datetime_)

    html = driver.page_source

    data_dir = pathlib.Path(__file__).parent / "data" / f"{datetime_:%Y%m%d}"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / f"{datetime_:%Y%m%d%H%M}.html").write_text(html)
finally:
    driver.quit()
