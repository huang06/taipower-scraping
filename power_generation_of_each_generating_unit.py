from __future__ import annotations

import argparse
import datetime
import logging
import os
import pathlib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

parser = argparse.ArgumentParser()
parser.add_argument("--remote", action="store_true")
args = parser.parse_args()

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)

if args.remote:
    remote_url = "http://127.0.0.1:4444/wd/hub"
    logger.info("Connecting to the Selenium hub: %s", remote_url)
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=remote_url,
        options=options,
    )
else:
    logger.info("Using the local driver")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

try:
    cht_url = "https://www.taipower.com.tw/d006/loadGraph/loadGraph/genshx_.html?mid=206&cid=406&cchk=b6134cc6-838c-4bb9-b77a-0b0094afd49d"  # noqa: E501
    logger.info("Connecting to the page: %s", cht_url)
    driver.get(cht_url)
    driver.implicitly_wait(5)

    title = driver.title
    logger.info("Page title: %s", title)

    page_head = (
        WebDriverWait(driver, 10)
        .until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div")))
        .get_attribute('innerHTML')
    )
    logger.info("page_head: %s", page_head)

    datetime_repr = (
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "datetime"))).text
    )  # '2022-09-17 16:40'
    logger.info("datetime_repr=%s", datetime_repr)
    datetime_ = datetime.datetime.strptime(datetime_repr, "%Y-%m-%d %H:%M")
    logger.info("Updated - %s", datetime_)

    html = driver.page_source

    data_dir = pathlib.Path(__file__).resolve().parent / "data" / f"{datetime_:%Y%m%d}"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / f"{datetime_:%Y%m%d%H%M}.html").write_text(html)
finally:
    driver.quit()
