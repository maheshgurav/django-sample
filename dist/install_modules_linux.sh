echo "This script will install required modules for running home test"
python get-pip.py
sudo pip install nltk
sudo pip install distance
sudo pip install sortedcontainers
sudo pip install django
sudo pip install djangorestframework
python module_checker.py