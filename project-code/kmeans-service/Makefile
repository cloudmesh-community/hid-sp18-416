SWAGGER_CODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
PORT=9550

service:
	pip install -r kmeans-svc-requirements.txt
	# Generate Server
	$(SWAGGER_CODEGEN) generate -i kmeans-swagger-svc.yaml -l python-flask -o server -D supportPython2=true
	# Copy files
	cp *_controller.py server/swagger_server/controllers
	cp __main__.py server/swagger_server/
	# Install requirements and server side code
	cd server; pip install -r requirements.txt; python setup.py install;

start:
	# Run service
	cd server; python -m swagger_server

client:
	# Generate Client Code
	$(SWAGGER_CODEGEN) generate -i kmeans-swagger-svc.yaml -l python -o client -D supportPython2=true
	# Install requirements and client side code
	cd client; pip install -r requirements.txt; python setup.py install

stop:
	# Save pid of server in SVC_PID file
	ps aux | grep "[p]ython -m swagger_server" | awk '{print $$2}' > SVC_PID
	# If process exists kill service
	if [ -e SVC_PID ]; then \
		kill -TERM $$(cat SVC_PID) || true; \
	fi;
	
clean:
	if [ -d server ]; then \
		rm -r server/; \
	fi;
	if [ -d client ]; then \
		rm -r client/; \
	fi;
