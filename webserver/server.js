     server = require('http').createServer(app),
       exec = require('child_process').exec,
       path = require('path'),
       mime = require('mime'),
         fs = require('fs'),
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

  http.get(api + input, function(res){
    var body = '';

    res.on('data', function(chunk) {
	body += chunk;
    });

    res.on('end', function() {
      // parseXML here
      console.log(body);


    });
  }).on('error', function(e) {
    console.log("Got error: ", e);
  });

  return


  fs.exists('generated/GENERATED_' + input + '.stl', function(exists) {
    if (exists) {
      res.redirect('/get?id=GENERATED_' + req.body.text.area);
    } else {
      child = exec('cd python; python2 webstlwrite.py ' + input, function(error, stdout, stderr) {
	if (error !== null) {
	  console.log('exec error: ' + error);
	}
	res.redirect('/get?id=GENERATED_' + req.body.text.area);
      });
    }
  });
  
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
