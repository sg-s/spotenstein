start: stop certificate
	docker-compose up --build -d

stop:
	docker-compose down

certificate: mydomain.key mydomain.crt

mydomain.key mydomain.crt:
	openssl req -x509 -newkey rsa:4096 -keyout mydomain.key -out mydomain.crt -days 365 -nodes -subj "/CN=mydomain"