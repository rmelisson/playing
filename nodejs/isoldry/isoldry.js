var express = require("express")

var app = express.createServer() 
app.set('view engine', 'jade');
app.set('views', __dirname + '/views');

var pub = __dirname + '/public'
app.use(express.static(pub));
app.use(express.bodyParser());

app.get('/', function(req, res) {
	res.render('layout');
});

app.listen(process.env.VMC_APP_PORT || 8000);
