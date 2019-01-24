.DEFAULT_GOAL := all
SHELL := /bin/bash

COMPONENTS ?= 

P2P_DIST_DIR := dist/
P2P_BUILDER_IMAGE := pandastoproduction-builder:latest
P2P_WHL := $(P2P_DIST_DIR)/pandastoproduction-0.1.0-py3-none-any.whl

.PHONY: help
help: ## Display makefile target descriptions.
	@printf -- "\nPandas to Production.\n\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: compose-up
compose-up: ## Start the docker-compose stack.
	@COMPONENTS=$(subst ',',' ',$(COMPONENTS))
	docker-compose build $(COMPONENTS)
	docker-compose up -d $(COMPONENTS)


.PHONY: compose-down
compose-down: ## Stop the docker-compose stack.
	docker-compose down --remove-orphans --volumes


.PHONY: build-whl
build-whl: ## Build the p2p library.
	@printf -- "Building wheel: $(P2P_WHL)\n"
	docker build -f components/p2p/Dockerfile -t $(P2P_BUILDER_IMAGE) components/p2p
	docker run --rm -v $(PWD)/dist:/dist $(P2P_BUILDER_IMAGE)


.PHONY: clean
clean: ## Remove temporary directories.
	-rm -rf dist data


.PHONY: all
all: ## Runs all steps to have a working demo.
	make clean
	make compose-down
	make build-whl
	make compose-up
