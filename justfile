format:
    uv run ruff check --fix src tests
    uv run ruff format src tests

format-check:
    uv run ruff format --check src tests

lint:
    uv run ruff check src tests

test:
    PYTHONPATH=src uv run pytest

build:
    PYTHONPATH=src uv run python -m portfolio.build

check: format-check lint test build