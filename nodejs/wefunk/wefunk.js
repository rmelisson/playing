var rss = require('./node-rss');
var fs = require('fs');
var http = require('http');

var url_show = "http://www.wefunkradio.com/show/";
var url_stream = "http://www.wefunkradio.com/mirror/stream/";

var feed_file = __dirname + "/custom_funk_feed.xml";

//var last_article;
var wf_url = "http://www.wefunkradio.com/rss-news.xml"

// we publish our rss feed
generateFeed = function(episodes){
	var feed = '<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0" xmlns:amp="http://www.adobe.com/amp/1.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Custom We funk</title>'

	for (i=0; i<episodes.length;i++){
		episode = episodes[i];
		feed += '<item><title>' + episode.article.title+ '</title>';
		feed += '<pubDate>' + episode.article.pubdate  + '</pubDate>'
		feed += '<enclosure url="' + episode.url  + '" type="audio/mpeg"/></item>'
	}	

	feed += '</channel></rss>'

	fs.writeFileSync(feed_file, feed, 'utf8');

	console.log("Feed updated at " + (new Date()).toString());
}


getEpisodeNumberFromTitle = function(title){
	return title.substring(5,title.indexOf(':'));
}

generateEpisodeURLFromRSSArticle = function(article) {
	link = article.link;
	num = getEpisodeNumberFromTitle(article.title);
	ep_date = link.substring(link.lastIndexOf('/')+1, link.length);
	
	return url_stream + ep_date + '/' + num
}

myfunc = function(articles) {
	episodes = [];
	for (i=0; i<articles.length;i++){
		article = articles[i]
		url = generateEpisodeURLFromRSSArticle(article);
		num = getEpisodeNumberFromTitle(article.title);

		episodes.push({'num' : num, 'url' : url, 'article' : article});	
	}

	generateFeed(episodes);
}


updateFeed = function() {
	rss.parseURL(wf_url, myfunc);
};

var server = http.createServer(
	function(req, res){
		res.writeHead(
			200,
			{ "Content-Type": "text/xml" }
		);
	
	// we open the feed file and send its content
	res.end(fs.readFileSync(feed_file, 'utf8'));
});
updateFeed();
setInterval(updateFeed, 1000*5)
server.listen(process.env.VMC_APP_PORT || 3000);

// {
    //sys.puts(articles.length);
//	blabla = articles[articles.length - 1].title;
    /*for(i=0; i<articles.length; i++) {
	console.log(articles[i].title;
	sys.puts(
		"Article: "+i+", "+
		articles[i].title+"\n"+
		articles[i].link+"\n"+
		articles[i].description+"\n"+
		articles[i].content
	);
    }*/
//});


// if there is a new one, we retrieve its url and we add it to our feed



