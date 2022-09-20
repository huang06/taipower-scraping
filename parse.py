from __future__ import annotations

import logging
import os

from bs4 import BeautifulSoup

with open("data/20220917/202209171750.html") as html_doc:
    soup = BeautifulSoup(html_doc, "html.parser")

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)

table = soup.find("table", {"id": "unitgentab"})

# parse headers
thead = table.find("thead")
headers = [thead.text.strip().lower() for thead in thead.find_all("th")]
logger.info(headers)
n_headers = len(headers)

# parse rows
data = []
rows = table.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    items = [index.text.strip() for index in cells]
    data.append(items)
    if len(items) != n_headers:
        logger.warning(items)
    logger.info(items)
