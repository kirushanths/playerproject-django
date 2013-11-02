sudo apt-get update
sudo aptitude upgrade

## install nginx and extras
sudo apt-get install nginx

## install PHP and essentials
sudo apt-get install php5
sudo aptitude install php5-cli php5-common php5-mysql php5-suhosin php5-gd
sudo aptitude install php5-fpm php5-cgi php-pear php5-memcache php-apc

sudo apt-get install mysql-server
sudo apt-get install php5-mysql

sudo echo "extension=mysqli.so" > /etc/php5/fpm/php.ini

## dump sql tables
mysql -u <username> -p auth_users < dumpfile.sql

## install PHP GD/ Imagick
sudo apt-get install php5-gd
sudo apt-get install libmagickwand-dev libmagickcore4 libmagickwand4
sudo aptitude install php5-imagick

## install phpredis
## http://ricochen.wordpress.com/2012/03/25/install-phpredis-on-ubuntu/
sudo apt-get install php5-dev
cd /etc/ 
git clone git://github.com/nicolasff/phpredis.git
cd phpredis
phpize
./configure
make && make install
echo "extension=redis.so" > /etc/php5/conf.d/redis.ini

## install GIT
sudo apt-get install git

## install nodejs
sudo apt-get install nodejs
sudo apt-get install npm

sudo apt-get install rabbitmq-server

# https://github.com/remy/nodemon
# -g required cause nodemon is a commandline script
npm install nodemon -g

npm install rabbit.js -dg
npm install amqp -dg
npm install sockjs -dg
npm install rbytes -dg



