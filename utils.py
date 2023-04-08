from __future__ import annotations

import logging
from typing import Any

from selenium import webdriver

logger = logging.getLogger(__name__)


def get_driver(browser: str = "firefox", remote_url: str | None = None) -> Any:
    driver_dict = {
        "firefox": webdriver.Firefox,
        "chrome": webdriver.Chrome,
    }
    option_dict = {
        "firefox": webdriver.FirefoxOptions,
        "chrome": webdriver.ChromeOptions,
    }
    options = option_dict[browser]()
    if remote_url is not None:
        logger.info("Using the remote hub: %s", remote_url)
        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options,
        )
        return driver
    else:
        logger.info("Using the local driver")
        options.add_argument("--headless")
        driver = driver_dict[browser](options=options)
        return driver
