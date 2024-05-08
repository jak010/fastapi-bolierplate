

app.docker:
	docker-compose -f ./.docker/docker-compose.yml up --remove-orphans

app.local:
	uvicorn application:application --port 8000 --reload

app.dev:
	uvicorn application:application --port 8000 --workers 4