# Variables
PROJECT_NAME="fzflib"

ifeq ($(OS),Windows_NT)
	VENV_BIN = .\.venv\Scripts
else
	VENV_BIN = ./.venv/bin
endif

# Settings
.DEFAULT_GOAL = help


help:
	@echo "---------------HELP---------------------------"
	@echo "Manage $(PROJECT_NAME). Usage:"
	@echo "make test   - Test."
	@echo "make clean  - Clean build directories, temporary files, and caches."
	@echo "make deploy - Deploy to PyPi."
	@echo "----------------------------------------------"

test:
	@echo "Testing $(PROJECT_NAME)."
	${VENV_BIN}/python -m pip install --upgrade pip
	${VENV_BIN}/pip install tox tox-gh-actions
	${VENV_BIN}/tox

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
	${VENV_BIN}/python setup.py sdist bdist_wheel

release:
	@echo "Deploying $(PROJECT_NAME) to PyPi."
	# Build and Upload Release
	${VENV_BIN}/python setup.py sdist bdist_wheel upload
