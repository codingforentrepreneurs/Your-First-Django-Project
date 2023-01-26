build:
	docker build -t your-first-django-project -f Dockerfile . 

run:
	docker run -p 8200:80 --name your-first-django-project --rm  your-first-django-project

stop:
	docker stop your-first-django-project

push:
	docker build --platform=linux/amd64 -t codingforentrepreneurs/your-first-django-project:latest -f Dockerfile . 
	docker push codingforentrepreneurs/your-first-django-project