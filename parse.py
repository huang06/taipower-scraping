from __future__ import annotations

import datetime
import logging
import os
import re
from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


def extract_values_in_pagesource(html_path: Path) -> dict:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    datetime_ = datetime.datetime.strptime(
        soup.find("a", id="datetime").text, "%Y-%m-%d %H:%M"
    )  # 2023-02-07 21:20

    overview = soup.find_all("div", {"class": "col col-sm-6"})

    nuclear = None
    for div in overview:
        obj = div.find("strong", string="核能(Nuclear)")
        if obj is not None:
            nuclear = float(obj.findNext("span").string.strip())
            break
    if obj is None:
        logger.error("Failed to extract the Nuclear value")

    coal = None
    for div in overview:
        obj = div.find("strong", string="燃煤(Coal)")
        if obj is not None:
            coal = float(obj.findNext("span").text.strip())
            break
    if obj is None:
        logger.error("Failed to extract the Coal value")

    solar = None
    for div in overview:
        obj = div.find("strong", string="太陽能(Solar)")
        if obj is not None:
            solar = float(obj.findNext("span").text.strip())
            break
    if obj is None:
        logger.error("Failed to extract the Solar value")

    wind = None
    for div in overview:
        obj = div.find("strong", string="風力(Wind)")
        if obj is not None:
            wind = float(obj.findNext("span").text.strip())
            break
    if obj is None:
        logger.error("Failed to extract the Wind value")

    output = {
        "time": datetime_,
        "overview": {
            "nuclear": nuclear,
            "coal": coal,
            "solar": solar,
            "wind": wind,
        },
    }
    return output


html_path_list = []
for dir_ in Path("/home/tom/huang06/taipower-scraping/data").iterdir():
    if not dir_.is_dir() or dir_.stem < '20230205':
        continue
    for html_file in dir_.iterdir():
        if re.match(r".*/(\d+).html$", str(html_file)):
            html_path_list.append(html_file)
html_path_list.sort()
print(f"Length of html_path_list: {len(html_path_list)}")

row_list = []
for html_path in html_path_list:
    resp = extract_values_in_pagesource(html_path)
    row_list.append({"time": resp["time"], **resp["overview"]})
df = pd.DataFrame(row_list)
df.to_csv("aaa.csv", index=False)
