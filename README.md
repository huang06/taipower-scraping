# Taipower Scraper

Scraping real-time power information from Taipower website.

## Motivation

[Taipower](https://www.taipower.com.tw) updates Taiwan's electricity consumption information and power generation information every 10 minutes on its website. However, the official currently does not provide historical records for downloading.

Therefore, I set up GitHub actions to fetch the power data every 10 minutes and save to this repository for further analysis usage.

## TODO

- [GitHub Action] wait for N seconds until the Selenium service is ready.

## Development Guide

### Prerequisites

- Python3 (tested with 3.10)
- Docker

### Selenium Grid

Start a Docker container with Firefox.

```bash
docker run -d -p 4444:4444 --shm-size="2g" docker.io/selenium/standalone-firefox:4.4.0
```

For detailed usage of Selenium Grid, see <https://github.com/SeleniumHQ/docker-selenium>.

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -U pip setuptools wheel
python3 -m pip install -r requirements.txt
python3 -m pip install -r requirements-dev.txt
```

### Git

```bash
pre-commit install
pre-commit install -t commit-msg
```
