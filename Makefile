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
	 for i in $$(seq 1 10); do \
        curl localhost:8080 ; \
    done

call_about_10_times:
	 for i in $$(seq 1 10); do \
        curl localhost:8080/about ; \
    done

		