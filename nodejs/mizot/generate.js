var fs = require('fs');
var jade = require('jade');
var util = require('util');
var util = require('util')
var exec = require('child_process').exec;

var root_dir = '/tmp/mizot';

function puts(error, stdout, stderr) { util.puts(stdout) }

jade.renderFile('./views/layout.jade', function(err, html) {
	if (err) {
		console.log(err);
	} else {
		// we create the directory and flush html code into an index.html
		fs.mkdir(root_dir, 0777 );
		fs.writeFile(root_dir + "/index.html", html, function(err) {
    	if (err) {
					console.log(err);
    	}
		}); 

		// we copy all the public files to the root directory
		exec("cp -R ./public/* " + root_dir, puts);
		console.log('... done');
	}
});
