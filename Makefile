docker_build:
	docker build -t tiagotele/python_api .

docker_run:
	docker run -p 80:80 tiagotele/python_api

uvicorn_run:
	uvicorn app.api:app --reload

unit_tests:
	python3 -m pytest

compose_up:
	docker-compose up

call_home_10_times:
	for i in 1 2 3 4 5; curl localhost:8080; done
		