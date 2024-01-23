# Taipower Scraper

Scraping real-time power information from Taipower website.

## Motivation

[Taipower](https://www.taipower.com.tw) updates the power generation data of various power plants every 15 minutes on its website, but does not offer the option to download historical data. This repository addresses this issue by using Selenium to collect data every 15 minutes for subsequent data analysis needs.

## Prerequisites

- Docker
- Python3 (tested with 3.10)

## Usage

Launch a Selenium worker.

```bash
docker compose up -d
```

Install Python packages and activate the virtualenv.

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
