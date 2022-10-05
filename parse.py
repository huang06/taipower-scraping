from __future__ import annotations

import logging
import os

import pandas as pd
from bs4 import BeautifulSoup

with open("data/20220917/202209171750.html", encoding="utf-8") as html_doc:
    soup = BeautifulSoup(html_doc, "html.parser")

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

table = soup.find("table", {"id": "unitgentab"})

# parse headers
thead = table.find("thead")
headers = [thead.text.strip().lower() for thead in thead.find_all("th")]
logger.info("headers: %s", headers)
n_headers = len(headers)

# parse rows
data_list: list[list] = []
tr_list = table.find("tbody").find_all("tr")
for tr in tr_list:
    # find group name
    if set(tr["class"]) == {'dtrg-group', 'dtrg-start', 'dtrg-level-0'}:
        group_name = tr.text
        logger.info("group_name: %s", group_name)
    # find rows of the group
    cells = tr.find_all("td")
    row = [index.text.strip() for index in cells]

    if len(row) != n_headers:
        logger.warning(row)
        continue

    row = [group_name] + row
    data_list.append(row)

columns = ["group_name"] + headers
data = pd.DataFrame(data_list, columns=columns)
