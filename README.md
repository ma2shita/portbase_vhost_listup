PortBase vhost Listup CGI
=========================

Overview
--------

ApacheでポートベースのVirtualHostを構築している例は多いと思いますが、
どのポートで何が動いているのか、わからなくなる事があります。

ファイル名から`Listen`をピックアップして、リストアップする単純なCGIです。

Environments
------------

1ファイル1vhost定義として、`/etc/apache2/site-available/`に配置されてる前提です。

例： `/etc/apache2/sites-available/scaffoh1`

	NameVirtualHost *:4001
	Listen 4001
	<VirtualHost *:4001>
	  RackEnv development
	  DocumentRoot /home/obdo/app/scaffoh1/public

	  <Directory "/home/obdo/app/scaffoh1/public">
		Options -MultiViews
		Order allow,deny
		Allow from all
	  </Directory>

### Requirements ###

* ruby 1.8.7 or higher
* hostname command


License
-------

under the MIT license (MIT-LICENSE.txt)

[EoF]
