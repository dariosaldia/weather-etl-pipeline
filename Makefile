.PHONY: up
up: down
	@docker compose up -d

.PHONY: down
down:
	@docker compose down
