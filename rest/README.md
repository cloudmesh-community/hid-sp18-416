# Instructions to Setup and Execute REST service

## Getting Started

### Steps

1. Setup MongoDB (in cloudmesh/data/db)
2. Install Eve in a Pyenv Virtual Environment
3. Execute run.py (in cloudmesh/eve)
```
python run.py
```
4. Execute EnterComputerInfo.py
```
python EnterComputerInfo.py
```
This would cause your computer information to be persisted in mongodb.

## Get persisted computer information

### Invoke the curl command

* GET Request

```
curl -H 'Content-Type: application/json' -X GET 'http://127.0.0.1:5000/computer_info'
```

* Response
```
{
	"_items": [
		{
			"_id": "5a77379ee555c056f46d9cb3",
			"username": "sabra",
			"system_info": {
				"system": "Linux",
				"node": "vaio",
				"release": "4.13.0-32-generic",
				"processor": "x86_64",
				"bit_architecture": "64bit",
				"current_cpu_freq": "861.9636249999999"
			},
			"memory": {
				"total": 4115476480,
				"available": 255721472,
				"used": 3558371328,
				"free": 116252672
			},
			"disk": {
				"total": 146247778304,
				"used": 110261878784,
				"free": 28533252096,
				"partition": {
					"device": "/dev/sda5",
					"mount point": "/",
					"file system type": "ext4",
					"opts": "rw,relatime,errors=remount-ro,data=ordered"
				}
			},
			"_updated": "Sun, 04 Feb 2018 16:41:02 GMT",
			"_created": "Sun, 04 Feb 2018 16:41:02 GMT",
			"_etag": "f549d97c9027cb3fc0e7b556e2f74206d4e7cd85",
			"_links": {
				"self": {
					"title": "Computer_info",
					"href": "computer_info/5a77379ee555c056f46d9cb3"
				}
			}
		}
	],
	"_links": {
		"parent": {
			"title": "home",
			"href": "/"
		},
		"self": {
			"title": "computer_info",
			"href": "computer_info"
		}
	},
	"_meta": {
		"page": 1,
		"max_results": 25,
		"total": 1
	}
}
```

## Clean Database

1. Run the following command
```
make mongodb_rm DB_NAME=system_db
```
