.PHONY: help up down logs ps test load

help:
	@echo "make up      - start full stack (app + mlflow + prometheus + grafana)"
	@echo "make down    - stop all services"
	@echo "make logs    - tail logs"
	@echo "make ps      - show running containers"
	@echo "make test    - run tests"
	@echo "make load    - generate traffic for monitoring"

up:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f --tail=200

ps:
	docker compose ps

test:
	pytest -q

load:
	bash scripts/load_test.sh