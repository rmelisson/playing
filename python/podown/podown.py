import feedparser
import urllib2
import threading
import os
from BeautifulSoup import BeautifulSoup

#cww_feed_url = "http://chanceswithwolves.blogspot.com/feeds/posts/default"
cww_feed_url = "file:///home/saul/dev/playing/python/podown/100.xml"
#cww_feed_url = "file:///home/saul/dev/playing/python/podown/normal.xml"

provider = "http://www.eastvillageradio.com"

tmp_directory = "/tmp/podown/"
if not os.path.exists(tmp_directory):
    os.makedirs(tmp_directory)

final_directory = "./down/"
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

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
    return

def get_mp3_url(url_base):
    u = urllib2.urlopen(url_base)
    return u.read()

def get_filename_from_item(item):
    title = item["title"]
    if "EPISODE" in title.upper() :
        for word in title.split():
            if word.startswith('#') and len(word) > 1:
                return word.strip('#') + '.mp3'
            elif word.isdigit():
                return word + '.mp3'
    return '_'.join(title.strip('!)(').split()) + '.mp3'

def get_title_list(html_content):
    l = ""
    titles = html_content.split('<br />')
    # see problem with ep 182
    if len(titles) < 10 :
        titles = html_content.split('<div><span>')

    for i in titles:
        if not i.startswith('<') and i != "" :
            t,_,div = i.partition('div')
            l += t
            l += '\n'
    return l

def is_already_there(item):
    file_name = get_filename_from_item(item)
    return file_name in os.listdir(final_directory)

def create_ep_list(feed):
    ep_list = []
    #print( feed[ "channel" ][ "title" ] )
    for item in feed[ "items" ]:
        if not is_already_there(item):
            html_content = item[ "content" ][0][ "value" ]
            soup = BeautifulSoup( html_content )
            for a in soup.findAll( "a" ):
                href = a.get( "href" )
                if (href.startswith(provider) and "PlayListID" in href) :
                    ep_list.append( ( 
                             get_filename_from_item(item),
                             get_mp3_url(href),
                             get_title_list(html_content) ) )
    return ep_list

feed = feedparser.parse( cww_feed_url )
for (filename, mp3_url, titles) in create_ep_list(feed):
    print filename
    print mp3_url
    print titles
    print
