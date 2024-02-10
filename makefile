help:
	@echo "Usage: make <target>"
	@echo "Available targets:"
	@echo "  run.local       - Run Django server locally after checking database health"
	@echo "  mysql.up        - Start MySQL container"
	@echo "  psql.up         - Start PostgreSQL container"
	@echo "  migrate.psql    - Run migrations for PostgreSQL"
	@echo "  migrate.mysql   - Run migrations for MySQL"

run.local:
	python3 manage.py check_db_health
	python3 manage.py runserver

mysql.up:
	docker run -d --name mysql_dj_multi_db \
		-p 3306:3306 \
		-e MYSQL_ROOT_PASSWORD=password \
		-e MYSQL_DATABASE=mysql_dj_multi_db \
		-e MYSQL_USER=mysql_dj_multi_db \
		-e MYSQL_PASSWORD=password \
		mysql:latest

psql.up:
	docker run -d --name psql_dj_multi_db \
		-p 5432:5432 \
		-e POSTGRES_PASSWORD=password \
		-e POSTGRES_USER=psql_dj_multi_db \
		-e POSTGRES_DB=psql_dj_multi_db \
		postgres:latest

migrate.psql:
	python3 manage.py migrate --database=psql dj_app_1

migrate.mysql:
	python3 manage.py migrate --database=mysql dj_app_2
