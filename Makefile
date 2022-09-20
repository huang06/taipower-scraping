SHELL=/bin/bash

.PHONY: all
all:

.PHONY: python-venv
python-venv:
	rm -rf .venv
	python3 -m pip install pipenv
	PIPENV_VENV_IN_PROJECT=1 pipenv sync

.PHONY: python-ci
python-ci:
	python3 -m pip install pipenv
	pipenv sync --system

.PHONY: selenium
selenium:
	docker run -d -p 4444:4444 --shm-size="2g" --name selenium docker.io/selenium/standalone-firefox:4.4.0

.PHONY: pre-commit
pre-commit:
	PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev
	.venv/bin/pre-commit run -a

.PHONY: clean
clean:
	rm -rf .venv
	docker rm -f selenium
