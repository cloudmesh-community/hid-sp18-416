var http = require('http'),
    url = require('url'),
    fs = require('fs'),
    formidable = require('formidable'),
    express = require('express'),
    mv = require('mv');

var app = express();
var Client = require('node-rest-client').Client;
var client = new Client();
var kmeans_svc_ip = "kmeans-swagger-svc";
var kmeans_svc_port = "9550";
var kmeans_svc_protocol = "http";
var kmeans_svc_path = "kmeans";
var kmeans_svc_url = kmeans_svc_protocol + "://" + kmeans_svc_ip + ":" + kmeans_svc_port + "/" + kmeans_svc_path + "/";


function saveInputFileinHDFS(username, jobnum, filename) {
    // Invoke Swagger REST service to upload input fiel to hdfs
    var args = {
        path: {
            username: username,
            jobNum: jobnum,
            fileName: filename
        },
        headers: {
            "Content-Type": "application/json"
        }
    };

    client.post(kmeans_svc_url + "saveInputFile?username=${username}&jobNum=${jobNum}&fileName=${fileName}", args, function(data, response) {
        console.log(data);
    });
}

function executeKMeans(username, jobnum, input_file_name, model_file_name, prediction_file_name, k, features_col) {
    // Invoke Swagger REST service to upload input fiel to hdfs
    var args = {
        path: {
            username: username,
            jobNum: jobnum,
            input_file_name: input_file_name,
            prediction_file_name: prediction_file_name,
            model_file_name: model_file_name,
            k: k,
            features_col: features_col
        },
        headers: {
            "Content-Type": "application/json"
        }
    };

    client.post(kmeans_svc_url + "executeKMeans?username=${username}&jobNum=${jobNum}&input_file_name=${input_file_name}&prediction_file_name=${prediction_file_name}&model_file_name=${model_file_name}&k=${k}&features_col=${features_col}", args, function(data, response) {
        console.log(data);
    });
}

app.post('/uploadInputFile', function(req, res) {

    var form = new formidable.IncomingForm();
    form.parse(req, function(err, fields, files) {
        if (files.filetoupload == undefined) {
            res.writeHead(400, {
                'Content-type': 'text/html'
            })
            res.end("No file uploaded");
        } else {
            // Save Uploaded File in local file system
            var oldpath = files.filetoupload.path;
            var filepath = '../data/' + fields.username + '/' + fields.jobnum + '/';
            var newpath = filepath + files.filetoupload.name;
            if (!fs.existsSync('../data/' + fields.username)) {
                fs.mkdirSync('../data/' + fields.username);
            }

            if (!fs.existsSync(filepath)) {
                fs.mkdirSync(filepath);
            }

            // Move from /tmp directory to inside the mounted fs
            mv(oldpath, newpath, function(err) {
                if (err) {
                    console.log(err);
                    res.write(err);
                } else {
                    // Invoke Swagger REST service to upload input fiel to hdfs
                    saveInputFileinHDFS(fields.username, fields.jobnum, files.filetoupload.name)
                    res.write('File uploaded and moved!');
                    res.end();
                }
            });
        }
    });
})

app.post('/executeKMeans', function(req, res) {
    var query = url.parse(req.url, true).query;
    var input_file_name = query.input_file_name;
    var model_file_name = query.model_file_name;
    var prediction_file_name = query.prediction_file_name;
    var username = query.username;
    var jobnum = query.jobnum;
    var k = query.k;
    var features_col = query.features_col;

    executeKMeans(username, jobnum, input_file_name, model_file_name, prediction_file_name, k, features_col)
    res.write('Executed KMeans');
    res.end();

})

app.get('/getKMeansModel', function(req, res) {
    var query = url.parse(req.url, true).query;
    var filename = query.file;
    var username = query.username;
    var jobnum = query.jobnum;
    var func = req.url.match('^[^?]*')[0].split('/').slice(1);

    // Invoke Swagger REST service to upload input fiel to hdfs
    var args = {
        path: {
            func: func,
            username: username,
            jobNum: jobnum,
            fileName: filename
        },
        headers: {
            "Content-Type": "application/json"
        }
    };

    client.get(kmeans_svc_url + "${func}?username=${username}&jobNum=${jobNum}&fileName=${fileName}", args, function(data, response) {
        // parsed response body as js object 
        console.log(data);
        setTimeout(function() {
            fs.readFile('../data/' + username + '/' + jobnum + '/' + filename, function(err, content) {
                if (err) {
                    res.writeHead(400, {
                        'Content-type': 'text/html'
                    })
                    console.log(err);
                    res.end("No such Model file");
                } else {
                    res.setHeader('Content-disposition', 'attachment; filename=' + query.file);
                    res.end(content);
                }
            });
        }, 2500);
    });
})

app.get('/getPredictions', function(req, res) {
    var query = url.parse(req.url, true).query;
    var filename = query.file;
    var username = query.username;
    var jobnum = query.jobnum;
    var func = req.url.match('^[^?]*')[0].split('/').slice(1);

    // Invoke Swagger REST service to upload input fiel to hdfs
    var args = {
        path: {
            func: func,
            username: username,
            jobNum: jobnum,
            fileName: filename
        },
        headers: {
            "Content-Type": "application/json"
        }
    };

    client.get(kmeans_svc_url + "${func}?username=${username}&jobNum=${jobNum}&fileName=${fileName}", args, function(data, response) {
        // parsed response body as js object 
        console.log(data);
        setTimeout(function() {
            fs.readFile('../data/' + username + '/' + jobnum + '/' + filename, function(err, content) {
                if (err) {
                    res.writeHead(400, {
                        'Content-type': 'text/html'
                    })
                    console.log(err);
                    res.end("No such Predictions file");
                } else {
                    res.setHeader('Content-disposition', 'attachment; filename=' + query.file);
                    res.end(content);
                }
            });
        }, 2500);
    });

})

var server = app.listen(3333, function() {

    var host = server.address().address
    var port = server.address().port

    console.log("Server running at http://localhost:3333")
})