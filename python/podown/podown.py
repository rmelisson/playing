import feedparser

#cww_feed_url = "http://chanceswithwolves.blogspot.com/feeds/posts/default"
cww_feed_url = "file://home/saul/Downloads/cww.xml"

feed = feedparser.parse( cww_feed_url )

print( feed[ "channel" ][ "title" ] )

for item in feed[ "items" ]:
    print( item[ "title" ] )
