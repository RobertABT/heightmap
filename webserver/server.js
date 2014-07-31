var express = require('express'),
        app = express(),
       http = require('http'),
     server = require('http').createServer(app),
       exec = require('child_process').exec,
       path = require('path'),
       mime = require('mime'),
         fs = require('fs'),
parseString = require('xml2js').parseString,
	 io = require('socket.io').listen(server),
      child;

server.listen(80);

app.configure(function () {
  app.use(express.static(__dirname + '/public'));
  app.use(express.json());
  app.use(express.urlencoded());
  app.use(app.router);
});

app.post('/submit', function(req, res){

});

io.sockets.on('connection', function (socket) {
  console.log(socket.id + " connected.");


  socket.on('postCode', function(data) {
    var input = data.code;
    var api = "http://www.nearby.org.uk/api/convert.php?key=5103caf756c8b6&p=";
    var gridCode;
    var result;

    http.get(api + input, function(res){
      var body = '';

      res.on('data', function(chunk) {
	  body += chunk;
      });

      res.on('end', function() {
	parseString(body, function (err, result) {
	  gridCode = result.convert.output[0].gr10[0].$.gr10;
	  gridCode = gridCode.replace(/ /g,'');
	  fs.exists('generated/GENERATED_' + gridCode + '.stl', function(exists) {
	    if (!exists) {
	      child = exec('cd python; python2 webstlwrite.py ' + gridCode, function(error, stdout, stderr) {
	        socket.emit('generated',{'fileName' : gridCode});
                return;
	      });
	    } else {
	      socket.emit('generated',{'fileName' : gridCode});
            }
	  });
	});
      });
    }).on('error', function(e) {
      console.log("Got error: ", e);
    });

    });

    socket.on('disconnect', function() {
      console.log(socket.id + " disconnected.");
    });
});

app.get('/preview', function(req, res) {
  var file = 'generated/' + req.param('id') + '.stl';
  res.sendfile("public/preview.html");
});

app.get('/download', function(req, res) {
  // res.redirect('/get?id=GENERATED_' + gridCode); gridCode can't be accessed
  var file = 'generated/' + req.param('id') + '.stl';

  var filename = path.basename(file);
  var mimetype = mime.lookup(file);

  res.setHeader('Content-disposition', 'attachment; filename=' + filename);
  res.setHeader('Content-type', mimetype);

  var filestream = fs.createReadStream(file);
  filestream.pipe(res);
});

