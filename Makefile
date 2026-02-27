SHELL := /bin/bash

DURATION ?= 60
CONCURRENCY ?= 10
SLEEP ?= 0.2

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f --tail=200 app

load:
	DURATION=$(DURATION) CONCURRENCY=$(CONCURRENCY) SLEEP=$(SLEEP) bash scripts/load_test.sh