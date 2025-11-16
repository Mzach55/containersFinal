build:
	docker build -t resilient-app .
run:
	docker run --rm -p 8080:8080 resilient-app
test:
	curl -f http://localhost:8080
