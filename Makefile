PROJECT_NAME=sellout
PYTHON_INSTALL := $(shell python3 -c 'import sys;print(sys.executable)')
BIN ?= $(shell [ -e venv/bin ] && echo 'venv/bin' || dirname $(PYTHON_INSTALL))/
args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

# colors
GREEN = $(shell tput -Txterm setaf 2)
YELLOW = $(shell tput -Txterm setaf 3)
WHITE = $(shell tput -Txterm setaf 7)
RESET = $(shell tput -Txterm sgr0)
GRAY = $(shell tput -Txterm setaf 6)
TARGET_MAX_CHAR_NUM = 20

# Common

all: run

init_dev:
	poetry install --no-root

pretty:
	$(BIN)black -l 120 -t py310 .


## Runs application. Builds, creates, starts, and attaches to containers for a service. | Common
up:
	@docker compose up $(PROJECT_NAME)_app

## Rebuild domain_api_app container
build:
	@docker compose build $(PROJECT_NAME)_app

## Stops application. Stops running container without removing them.
stop:
	@docker compose stop

## Removes stopped service containers.
clean:
	@docker compose down

## Runs command `bash` commands in docker container.
bash:
	@docker exec -it $(PROJECT_NAME) bash

# Help

## Shows help.
help:
	@echo ''
	@echo 'Usage:'
	@echo ''
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
		    if (index(lastLine, "|") != 0) { \
				stage = substr(lastLine, index(lastLine, "|") + 1); \
				printf "\n ${GRAY}%s: \n\n", stage;  \
			} \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			if (index(lastLine, "|") != 0) { \
				helpMessage = substr(helpMessage, 0, index(helpMessage, "|")-1); \
			} \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''

# Linters & tests

## Formats code with `flake8`.
lint:
	$(BIN)flake8 --jobs 4 --statistics --show-source application
	$(BIN)black -l 120 -t py310 --check .


test:
	cp config-simple.json config.json -n
	@pytest -n 4 -vvv --trace-config -p no:warnings --cov=application --junitxml=junit.xml --cov-report xml:coverage.xml --cov-report term
	@python3 -c "exec(\"from xml.etree import ElementTree\ntree = ElementTree.parse('./coverage.xml')\nsources = tree.find('sources')\nfor source in sources:source.text ='./'+ source.text.split('/')[-1]\ntree.write('./coverage.xml')\")"


## Runs application with development config.
dev:
	poetry run python -m application.manage runserver


migration:
	poetry run python -m application.manage migrate

create_revision:
	poetry run python -m application.manage makemigrations

run:
	poetry run python -m application

