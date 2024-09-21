.PHONY: build-and-push
build-and-push:
	@docker build -t $(FULL_IMAGE_NAME) . && docker push $(FULL_IMAGE_NAME)

.PHONY: build
build:
	@docker compose build

.PHONY: up
up: down build
	@docker compose up -d

.PHONY: down
down:
	@docker compose down

# Lint the code using flake8
.PHONY: lint
lint:
	@flake8 .

# Format the code using black and isort
.PHONY: format
format:
	@black .
	@isort .

# Check if code needs formatting (without applying)
.PHONY: check-format
check-format:
	@black --check .
	@isort --check .

# A complete check that includes both linting and formatting checks
.PHONY: check
check: lint check-format
