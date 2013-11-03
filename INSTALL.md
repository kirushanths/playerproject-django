##### Download playerproject vagrant .box file
https://www.dropbox.com/s/6d3g7s7v5e9s64u/package.box

##### Edit Host File
```
sudo echo -e '10.30.0.2 develop.theplayerproject.com' >> /etc/hosts
```

##### Vagrant setup commands on host machine

```
vagrant box add djangotpp package.box
vagrant init djangotpp
vagrant up
vagrant ssh
# (you are in the ubuntu vagrant box now)
```

Output should look like this:
```
Successfully added box 'djangotpp' with provider 'virtualbox'!
A 'Vagrantfile' has been placed in this directory …
Bringing machine 'default' up with 'virtualbox' provider
… (a lot of text)
```

##### In Vagrant:

```
tpp
(alias shortcut, takes you right to the mounted folder and actiavtes virtual env 
```

##### Development Server
- When server is running you can access the dev site through your host machine browser using `develop.theplayerproject.com`
