PROJECT_NAME = fzflib
VENV_DIR = .venv

ifeq ($(OS),Windows_NT)
	PYTHON = py
	VENV_BIN = ./$(VENV_DIR)/Scripts
else
	PYTHON = python3
	VENV_BIN = ./$(VENV_DIR)/bin
endif
VENV_PYTHON = $(VENV_BIN)/python
VENV_PIP = $(VENV_BIN)/pip

# Settings
.DEFAULT_GOAL = help
.PHONY: help test build clean publish venv


help:
	@echo "---------------HELP---------------------------"
	@echo "Manage $(PROJECT_NAME). Usage:"
	@echo "make test    - Test."
	@echo "make clean   - Clean build directories, temporary files, and caches."
	@echo "make build   - Build with setup.py."
	@echo "make publish - Deploy to PyPi."
	@echo "----------------------------------------------"

venv:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install --upgrade virtualenv
	$(PYTHON) -m virtualenv $(VENV_DIR)
	-$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install --upgrade -r requirements.txt
	$(VENV_PIP) install --upgrade -r dev-requirements.txt

test:
	@echo "Testing $(PROJECT_NAME)."
	$(VENV_BIN)/tox

clean:
	@echo "Removing temporary files and caches."
	# Build Directories
	rm -rf build/
	rm -rf dist/
	# Temporary Files
	rm -rf **/__pycache__/
	rm -rf **/*.egg-info/

build:
	@echo "Building $(PROJECT_NAME)."
	# Build
	$(VENV_PYTHON) setup.py sdist bdist_wheel

publish: build
	@echo "Deploying $(PROJECT_NAME) to PyPi."
	$(VENV_PIP) install --upgrade twine
	$(VENV_PYTHON) -m twine upload dist/*
