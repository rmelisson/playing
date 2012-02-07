import feedparser
from BeautifulSoup import BeautifulSoup

#cww_feed_url = "http://chanceswithwolves.blogspot.com/feeds/posts/default"
cww_feed_url = "file:///home/saul/dev/playing/python/podown/100.xml"
#cww_feed_url = "file:///home/saul/dev/playing/python/podown/normal.xml"

provider = "http://www.eastvillageradio.com"

feed = feedparser.parse( cww_feed_url )

print( feed[ "channel" ][ "title" ] )

for item in feed[ "items" ]:
    html_content = item[ "content" ][0][ "value" ]
    #print html_content
    soup = BeautifulSoup( html_content )
    for a in soup.findAll( "a" ):
	    #if a['href'].contains
	    href = a.get( "href" )
	    if (href.startswith(provider) and "PlayListID" in href) :
		print( item[ "title" ] )
	    	print( href )
		print
