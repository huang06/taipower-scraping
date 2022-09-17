SHELL=/bin/bash
PYTHON="$(shell pwd)/.venv/bin/python3"

.PHONY: all
all:

.PHONY: python-venv
python-venv:
	rm -rf .venv
	python3 -m venv .venv
	$(PYTHON) -V
	$(PYTHON) -m pip install -U pip setuptools wheel
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: selenium
selenium:
	docker run -d -p 4444:4444 --shm-size="2g" docker.io/selenium/standalone-firefox:4.4.0

.PHONY: pre-commit
pre-commit:
	$(PYTHON) -m pip install -r requirements-dev.txt
	.venv/bin/pre-commit run -a
