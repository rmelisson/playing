var formidable = require('formidable'),
    http = require('http'),

    sys = require('sys');

serv = http.createServer(function(req, res) {
  if (req.url == '/upload' && req.method.toLowerCase() == 'post') {
    // parse a file upload
    var form = new formidable.IncomingForm();
		form.uploadDir = '.';
		form.keepExtensions = true;
form.on('progress', function(bytesReceived, bytesExpected) {
  var progress = {
    type: 'progress',
    bytesReceived: bytesReceived,
    bytesExpected: bytesExpected
  };

  console.log(JSON.stringify(progress));
});

    form.parse(req, function(err, fields, files) {
      res.writeHead(200, {'content-type': 'text/plain'});
      res.write('received upload:\n\n');
      res.end(sys.inspect({fields: fields, files: files}));
    });
    return;
  }

  // show a file upload form
  res.writeHead(200, {'content-type': 'text/html'});
  res.end(
    '<form action="/upload" enctype="multipart/form-data" method="post">'+
//    '<input type="text" name="title"><br>'+
    '<input type="file" name="upload" multiple="multiple"><br>'+
    '<input type="submit" value="Upload">'+
    '</form>'
  );
});


serv.listen(80);
