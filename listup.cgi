#!/usr/bin/env ruby

sites = Dir.glob('/etc/apache2/sites-available/*').map{|i|[File.basename(i), (open(i).read.match(/^Listen ([0-9]+)$/)[1] rescue nil)]}.reject{|i|i.last.nil?}
list = sites.map do |i|
  url = sprintf('http://%s:%s', `hostname -f`.strip, i.last)
  sprintf('<li>%s <a href="%s">%s</a></li>', url, url, i.first)
end

require 'cgi'
title = "#{`hostname -s`.strip} services"
cgi = CGI.new('html4Tr')
cgi.out {
	cgi.html {
		cgi.head {
			cgi.title { title } +
			cgi.body {
				cgi.h1 { title } +
				cgi.ul { list.sort.join("\n") }
			}
		}
	}
}
