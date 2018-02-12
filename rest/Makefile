mongodb_rm:
	mongo $$DB_NAME --eval "printjson(db.dropDatabase())"

mongod_start:
	mongod --dbpath "data/db" &     

mongod_svc_id:
	ps aux | grep "mongod --dbpath data/db"

eve_start:
	python eve/run.py &

eve_svc_id:
	ps aux | grep "python eve/run.py"

clean:
	mongo --eval "db.getMongo().getDBNames().forEach(function(i){db.getSiblingDB(i).dropDatabase()})"
	rm -r data
	sleep 1
	mkdir -p data/db
	mongod --dbpath "data/db" &
