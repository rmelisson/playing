var fs = require('fs');
var jade = require('jade');

jade.renderFile('./views/layout.jade', function(err, html) {
	if (err) {
		console.log(err);
	} else {
		fs.mkdir('/tmp/mizot', 0777 );
		fs.mkdir('/tmp/mizot/javascript/', 0777 );
		fs.mkdir('/tmp/mizot/style/', 0777 );
		fs.writeFile("/tmp/mizot/index.html", html, function(err) {
    	if (err) {
					console.log(err);
    	}
		}); 
		
		var is = fs.createReadStream('./public/style/')
		var os = fs.createWriteStream('destination_file');

	}
});
