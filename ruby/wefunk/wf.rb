# Get sockets from stdlib
require 'socket'              

# 
require 'net/http'              

# Provides RSS parsing capabilities
require 'rss'

# Allows open to access remote files
require 'open-uri'

# What feed are we parsing?
rss_feed = "http://www.wefunkradio.com/rss-news.xml"

# Variable for storing feed content
rss_content = ""

# constants
url_stream = "http://www.wefunkradio.com/mirror/stream/"
#url_files = "http://wf.digvm.com/"
url_files = "wefunk.xcrit.com"

# Read the feed into rss_content
open(rss_feed) do |f|
   rss_content = f.read
end

# Parse the feed, dumping its contents to rss
rss = RSS::Parser.parse(rss_content, false)

# Output the feed title and website URL
puts "Title: #{rss.channel.title}"
puts "RSS URL: #{rss.channel.link}"
puts "Total entries: #{rss.items.size}"

rss.items.each do |item|
	#retrieve the episode's url
	ep_num = item.title.split(':')[0].split(' ')[1]	
	ep_link = item.link
	ep_date = ep_link[ep_link.rindex('/') + 1, ep_link.size]
	ep_file = "WeFunk_Show_" + ep_num + '_' + ep_date + ".mp3"
	ep_url = "http://" + url_files + "/" + ep_file 
	puts ep_url
	head = Net::HTTP.new(url_files, 80).request_head('/' + ep_file)
  item.enclosure = RSS::Rss::Channel::Item::Enclosure.new(ep_url, head.content_length, head.content_type)
end

server = TCPServer.new(2000)  # Socket to listen on port 2000
loop {                         # Servers run forever
  client = server.accept       # Wait for a client to connect
  headers = "HTTP/1.1 200 OK\r\nDate: Tue, 14 Dec 2010 10:48:45 GMT\r\nServer: Ruby\r\nContent-Type: text/xml; charset=iso-8859-1\r\n\r\n"
  client.puts headers  # Send the time to the client
  client.puts rss.to_s
  client.close                 # Disconnect from the client
}
