# Taipower Scraper

Scraping real-time power information from Taipower website.

## Motivation

[Taipower](https://www.taipower.com.tw) updates electricity consumption and generation information every 10 minutes on its website. However, historical records are not available for download. To address this, I developed GitHub workflows that automatically collect the data at regular intervals and save it in this repository for future analytical purposes.

## Prerequisites

- Docker
- Python3 (tested with 3.10)

## Usage

Launch a Selenium worker.

```bash
docker compose up -d
```

Install Python packages.

```bash
python3 -m pip install pipenv
pipenv install
pipenv shell
```

Execute the following scripts to download website data.

```bash
python3 power_generation_of_each_generating_unit.py --remote

python3 power_supply_for_the_next_seven_days.py --remote
```
