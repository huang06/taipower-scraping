SHELL=/bin/bash
PYTHON="$(shell pwd)/.venv/bin/python3"

.PHONY: all
all:

.PHONY: python
python:
	rm -rf .venv
	python3 -m venv .venv
	$(PYTHON) -V
	$(PYTHON) -m pip install -U pip setuptools wheel
	$(PYTHON) -m pip install -r requirements.txt

.PYTHON: nb
nb:
	$(PYTHON) -m jupyterlab --ip 0.0.0.0 --no-browser

.PYTHON: pre-commit
pre-commit:
	$(PYTHON) -m pip install -r requirements-dev.txt
	.venv/bin/pre-commit run -a
