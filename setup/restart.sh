#alias tpp='cd /var/www/local/'
#alias tpp_restart='f=$(pwd); cd /var/www/local/setup/; sudo bash /var/www/local/setup/restart.sh; cd $f'

fuser -k 80/tcp
/etc/init.d/nginx restart
/etc/init.d/php5-fpm restart

#cd ../public/nodejs
#sudo bash start_cottonmouth.sh