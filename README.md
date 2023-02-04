# Taipower Scraper

Scraping real-time power information from Taipower website.

## Motivation

[Taipower](https://www.taipower.com.tw) updates Taiwan's electricity consumption information and power generation information every 10 minutes on its website. However, the official currently does not provide historical records for downloading.

Therefore, I set up GitHub actions to fetch the power data every 10 minutes and save to this repository for further analysis usage.

[Taipower](https://www.taipower.com.tw) regularly updates electricity consumption and generation information every 10 minutes on its website. However, there is no option to download historical records. To address this,, I developed GitHub workflows that periodically gather the data and save it in this repository for future analysis purposes.

## Development Guide

### Prerequisites

- Python3 (tested with 3.10)
- Docker

### Selenium Grid

Start a Selenium Grid container.

```bash
make selenium
```

For detailed usage of Selenium Grid, see <https://github.com/SeleniumHQ/docker-selenium>.

### Python

```bash
python3 -m pip install pipenv
pipenv sync --dev -v
```

### pre-commit

```bash
pre-commit install
pre-commit install -t commit-msg
```

### Cleanup

```bash
make clean
```
