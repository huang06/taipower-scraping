# Taipower Scraper

Scraping real-time power information from Taipower website.

## Motivation

[Taipower](https://www.taipower.com.tw) updates electricity consumption and generation information every 10 minutes on its website. However, historical records are not available for download. To address this, I developed GitHub workflows that automatically collect the data at regular intervals and save it in this repository for future analytical purposes.

## Schedule table

| workflow | schedule |
|---|---|
| Power Supply for the Next Seven Days | `0 0,12 * * *` |
| Power Generation of Each Generating Unit | `10 * * * *` |

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
