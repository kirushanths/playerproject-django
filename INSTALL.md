
##### Download playerproject vagrant .box file

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
$$ tpp
(alias shortcut, takes you right to the mounted folder and actiavtes virtual env 
```

