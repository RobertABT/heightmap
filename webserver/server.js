var express = require('express'),
        app = express(),
       http = require('http'),
     server = require('http').createServer(app),
       exec = require('child_process').exec,
       path = require('path'),
       mime = require('mime'),
         fs = require('fs'),
parseString = require('xml2js').parseString,
      child;

server.listen(80);

app.configure(function () {
  app.use(express.static(__dirname + '/public'));
  app.use(express.json());
  app.use(express.urlencoded());
  app.use(app.router);
});

app.post('/submit', function(req, res){
  var input = req.body.text.area;
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
	      if (error !== null) {
		console.log('exec error: ' + error);
	      }
	    });
	  }
	});
      });
    });
  }).on('error', function(e) {
    console.log("Got error: ", e);
  });

  // res.redirect('/get?id=GENERATED_' + gridCode); gridCode can't be accessed

});

app.get('/get', function(req, res) {
  var file = 'generated/' + req.param('id') + '.stl';

  var filename = path.basename(file);
  var mimetype = mime.lookup(file);

  res.setHeader('Content-disposition', 'attachment; filename=' + filename);
  res.setHeader('Content-type', mimetype);

  var filestream = fs.createReadStream(file);
  filestream.pipe(res);
});
