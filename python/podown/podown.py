import feedparser
import urllib2
import threading
from BeautifulSoup import BeautifulSoup

#cww_feed_url = "http://chanceswithwolves.blogspot.com/feeds/posts/default"
cww_feed_url = "file:///home/saul/dev/playing/python/podown/100.xml"
#cww_feed_url = "file:///home/saul/dev/playing/python/podown/normal.xml"

provider = "http://www.eastvillageradio.com"

class Episode_Downloader(threading.Thread):
    def __init__(self, url_base):
        return

    def download_episode(url_base, file_path):
        ep_url = get_mp3_url( url_base )
        url = urllib2.urlopen( ep_url )
        f = open(file_path, 'w')
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = url.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
        f.close()

def get_mp3_url(url_base):
    u = urllib2.urlopen(url_base)
    return u.read()

def get_filename_from_item(item):
    if "Episode" in item["title"] :
        return "yes!"
    return "no"

def create_ep_list(feed):
    return

feed = feedparser.parse( cww_feed_url )

print( feed[ "channel" ][ "title" ] )

for item in feed[ "items" ]:
    html_content = item[ "content" ][0][ "value" ]
    #print html_content
    soup = BeautifulSoup( html_content )
    for a in soup.findAll( "a" ):
        href = a.get( "href" )
        if (href.startswith(provider) and "PlayListID" in href) :
            print( item[ "title" ] )
            print( get_filename_from_item(item) )
            print( href )
            #download_episode( href )
            print
