.PHONY: app db backend frontend down logs db-shell migrate test-db

# start everything
app:
	@$(MAKE) db
	@$(MAKE) -j2 backend frontend

# start FastAPI
backend: db
	cd backend && uv run uvicorn main:app --reload --port 8000

# start Next.js
frontend:
	cd frontend && pnpm run dev

# start Postgres
db:
	cd backend && docker compose up -d postgres

# stop Docker services
down:
	cd backend && docker compose down

# view Postgres logs
logs:
	cd backend && docker compose logs -f postgres

# open Postgres shell
db-shell:
	cd backend && docker compose exec postgres psql -U foretell -d foretell

# run database migrations
migrate:
	cd backend && uv run alembic upgrade head

# test database
test-db:
	cd backend && docker compose exec postgres psql -U foretell -d foretell -c "SELECT 1;"
