vagrant box add djangotpp djangotpp.box
# Successfully added box 'djangotpp' with provider 'virtualbox'!

vagrant init djangotpp
# A `Vagrantfile` has been placed in this directory …

vagrant up
# Bringing machine 'default' up with 'virtualbox' provider
# … (a lot of text)

vagrant ssh


[sudo]
apt-get install python-pip
pip install virtualenv
pip install Django