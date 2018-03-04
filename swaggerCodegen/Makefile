SWAGGER_CODEGEN=java -jar ~/swagger/swagger-codegen-cli-2.3.1.jar

create_service:
	# Generate Server
	$(SWAGGER_CODEGEN) generate -i swagger.yaml -l python-flask -o server -D supportPython2=true
	# Copy files
	cp credentials.yaml server/swagger_server/controllers
	cp movies_controller.py server/swagger_server/controllers
	cp music_controller.py server/swagger_server/controllers
	cp tv_shows_controller.py server/swagger_server/controllers
	cp __main__.py server/swagger_server/
	# Install requirements and server side code
	cd server; pip install -r requirements.txt; python setup.py install;

run_service:
	# Run service
	cd server; python -m swagger_server

create_client:
	# Generate Client Code
	$(SWAGGER_CODEGEN) generate -i swagger.yaml -l python -o client -D supportPython2=true
	# Install requirements and client side code
	cd client; pip install -r requirements.txt; python setup.py install

test_service:
	# Invoke services
	python InvokeServices.py "The Good Place" "Taylor Swift" "Red Sparrow"

clean:
	rm -r server/
	rm -r client/
