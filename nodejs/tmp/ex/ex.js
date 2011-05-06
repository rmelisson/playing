var http = require('http');
var PORT = process.env.VMC_APP_PORT || 3000;
var HOST= Number(process.env.VCAP_APP_HOST || 'localhost');



http.createServer(function (req, res) {

  res.writeHead(200, {'Content-Type': 'text/plain'});

  res.end('Hello World\n');

}).listen(PORT, HOST);

console.log('Server running on port ' + PORT);
