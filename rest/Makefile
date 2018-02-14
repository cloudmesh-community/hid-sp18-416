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
