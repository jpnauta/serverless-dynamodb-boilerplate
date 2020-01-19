start:
	docker-compose build
	docker-compose up
run:
	docker-compose exec web python run.py