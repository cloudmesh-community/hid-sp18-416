docker_compose_build:
	if [ ! -d data ]; then \
		mkdir data; \
	fi;
	sh download-data.sh
	wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -P kmeans-service/
	sudo docker-compose up --build

docker_compose_start:
	sudo docker-compose up

docker_compose_stop:
	sudo docker-compose stop

docker_compose_clean:
	sudo docker-compose rm -f

upload_input_file:
	curl -X POST http://localhost:3333/uploadInputFile \
	-H 'cache-control: no-cache' \
	-H 'content-type: multipart/form-data' \
	-F 'filetoupload=@iris_data.csv' \
	-F 'username=sabra' \
	-F 'jobnum=7'

execute_kmeans:
	curl -X POST \
	'http://localhost:3333/executeKMeans?k=3&input_file_name=iris_data.csv&model_file_name=model.txt&prediction_file_name=prediction.txt&username=sabra&jobnum=7&features_col=w&features_col=x&features_col=y&features_col=z' \
	-H 'cache-control: no-cache' 

get_kmeans_model:
	curl -X GET \
	'http://localhost:3333/getKMeansModel?username=sabra&jobnum=7&file=model.txt' \
	-H 'cache-control: no-cache'

get_predictions:
	curl -X GET \
	'http://localhost:3333/getPredictions?username=sabra&jobnum=7&file=prediction.txt' \
	-H 'cache-control: no-cache'