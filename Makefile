.PHONY: up
up: down
	@docker compose up --build -d

.PHONY: down
down:
	@docker compose down
