.DEFAULT_GOAL := compose-up
SHELL := /bin/bash

COMPONENTS ?= 

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
