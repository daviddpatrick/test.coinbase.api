ENV ?= venv
VENV ?= venv
PIP = $(VENV)/bin/pip3
PYTHON = $(VENV)/bin/python3
TESTENV ?= us

default: test

setup:
	python3 -m venv $(VENV)
	echo $(CURDIR)/$(VENV)

build: $(VENV)
	clear
	$(PIP) install -r requirements.txt

test: $(VENV)
	clear
	-$(PYTHON) -m pytest tests/test_coinbase.py --test_env=$(TESTENV) --alluredir=allure-results -W ignore::Warning;
	sleep 5;
	allure serve allure-results;